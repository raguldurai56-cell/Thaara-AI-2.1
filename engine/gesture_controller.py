"""Optional webcam gesture tracking for Thaara's animated assistant.

OpenCV is used when available. MediaPipe adds hand/face landmarks when installed;
without either dependency, the app remains fully functional in offline mode.
"""
import json
import threading
import time
from pathlib import Path


class GestureController:
    def __init__(self, state_file="gesture_state.json"):
        self.state = {"face": False, "hand": "none", "expression": "idle", "timestamp": 0}
        self.state_file = Path(state_file)
        self.running = False
        self._thread = None

    def update(self, face=False, hand="none", expression="idle"):
        self.state = {"face": bool(face), "hand": str(hand), "expression": str(expression), "timestamp": time.time()}
        try:
            self.state_file.write_text(json.dumps(self.state), encoding="utf-8")
        except OSError:
            pass
        return dict(self.state)

    def get_state(self):
        return dict(self.state)

    def process_frame(self, frame):
        """Process one BGR frame; returns a state without raising on missing extras."""
        face = False
        hand = "none"
        try:
            import cv2
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            face = len(cascade.detectMultiScale(gray, 1.1, 5)) > 0
        except Exception:
            pass
        try:
            import mediapipe as mp
            hands = mp.solutions.hands.Hands(static_image_mode=True, max_num_hands=1)
            result = hands.process(frame[:, :, ::-1])
            if result.multi_hand_landmarks:
                hand = "open" if self._is_open_hand(result.multi_hand_landmarks[0]) else "fist"
            hands.close()
        except Exception:
            pass
        expression = "alert" if face or hand != "none" else "idle"
        return self.update(face, hand, expression)

    @staticmethod
    def _is_open_hand(landmarks):
        tips = [8, 12, 16, 20]
        joints = [6, 10, 14, 18]
        return sum(landmarks.landmark[t].y < landmarks.landmark[j].y for t, j in zip(tips, joints)) >= 3

    def start(self, camera_index=0):
        if self.running:
            return False
        try:
            import cv2
            camera = cv2.VideoCapture(camera_index)
            if not camera.isOpened():
                camera.release()
                return False
        except Exception:
            return False
        self.running = True

        def loop():
            try:
                while self.running:
                    ok, frame = camera.read()
                    if ok:
                        self.process_frame(frame)
                    time.sleep(0.15)
            finally:
                camera.release()
                self.update(False, "none", "idle")

        self._thread = threading.Thread(target=loop, name="ThaaraGestureTracker", daemon=True)
        self._thread.start()
        return True

    def stop(self):
        self.running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1)
        return True


gesture_controller = GestureController()
