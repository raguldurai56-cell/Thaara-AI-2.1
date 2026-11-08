"""Optional authentication adapters."""


class _Recognizer:
    @staticmethod
    def AuthenticateFace():
        # Camera-based authentication is optional and must never grant access by default.
        return 0, None


recoganize = _Recognizer()
