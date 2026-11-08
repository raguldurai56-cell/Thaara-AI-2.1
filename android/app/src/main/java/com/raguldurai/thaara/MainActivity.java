package com.raguldurai.thaara;

import android.Manifest;
import android.app.Activity;
import android.content.ContentResolver;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.os.Bundle;
import android.provider.CallLog;
import android.speech.tts.TextToSpeech;
import android.view.Gravity;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import java.util.Locale;

public class MainActivity extends Activity {
    private TextToSpeech tts;
    private TextView status;

    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL); root.setPadding(32, 48, 32, 32);
        root.setGravity(Gravity.CENTER_HORIZONTAL); root.setBackgroundColor(0xff080b14);
        TextView title = new TextView(this); title.setText("THAARA AI\nAndroid Companion");
        title.setTextColor(0xffff5368); title.setTextSize(28); title.setGravity(Gravity.CENTER);
        root.addView(title, new LinearLayout.LayoutParams(-1, -2));
        status = new TextView(this); status.setText("Ready. Female voice + phone alerts.");
        status.setTextColor(0xffe8ecff); status.setTextSize(17); status.setPadding(0, 36, 0, 36);
        root.addView(status, new LinearLayout.LayoutParams(-1, -2));
        Button permissions = new Button(this); permissions.setText("Allow phone permissions");
        permissions.setOnClickListener(v -> requestPhonePermissions()); root.addView(permissions);
        Button test = new Button(this); test.setText("Test Thaara voice");
        test.setOnClickListener(v -> speak("Hello boss. Thaara is ready.")); root.addView(test);
        TextView note = new TextView(this); note.setText("Battery below 10%: charge reminder\nMissed calls: spoken alert when permissions are allowed\nPC sync: secure endpoint will be added next");
        note.setTextColor(0xffb8c4df); note.setTextSize(15); note.setPadding(0, 30, 0, 0); root.addView(note);
        setContentView(root); initTts();
    }

    private void initTts() {
        tts = new TextToSpeech(this, result -> { if (result == TextToSpeech.SUCCESS) {
            tts.setLanguage(Locale.US); tts.setSpeechRate(0.9f); tts.setPitch(1.08f);
            for (android.speech.tts.Voice voice : tts.getVoices()) {
                String n = (voice.getName() == null ? "" : voice.getName()).toLowerCase();
                if (n.contains("female") || n.contains("samantha") || n.contains("zira") || n.contains("en-us-x-sfg")) { tts.setVoice(voice); break; }
            }
        }});
    }

    private void speak(String text) { if (tts != null) tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, "thaara"); status.setText(text); }

    private void requestPhonePermissions() {
        if (android.os.Build.VERSION.SDK_INT >= 23) requestPermissions(new String[]{Manifest.permission.READ_CALL_LOG, Manifest.permission.READ_PHONE_STATE}, 9);
        if (android.os.Build.VERSION.SDK_INT >= 33) requestPermissions(new String[]{Manifest.permission.POST_NOTIFICATIONS}, 10);
    }

    @Override protected void onResume() { super.onResume(); checkMissedCalls(); }

    private void checkMissedCalls() {
        if (checkSelfPermission(Manifest.permission.READ_CALL_LOG) != PackageManager.PERMISSION_GRANTED) return;
        Cursor c = getContentResolver().query(CallLog.Calls.CONTENT_URI, new String[]{CallLog.Calls.NUMBER, CallLog.Calls.DATE}, CallLog.Calls.TYPE + "=?", new String[]{String.valueOf(CallLog.Calls.MISSED_TYPE)}, CallLog.Calls.DATE + " DESC");
        if (c != null && c.moveToFirst()) { String number = c.getString(0); speak("Boss, you have a missed call from " + number); c.close(); }
    }

    @Override protected void onDestroy() { if (tts != null) { tts.stop(); tts.shutdown(); } super.onDestroy(); }
}
