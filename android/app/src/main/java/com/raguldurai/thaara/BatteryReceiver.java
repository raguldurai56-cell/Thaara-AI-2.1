package com.raguldurai.thaara;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.BatteryManager;
import android.speech.tts.TextToSpeech;
import java.util.Locale;

public class BatteryReceiver extends BroadcastReceiver {
    @Override public void onReceive(Context context, Intent intent) {
        if (!Intent.ACTION_BATTERY_CHANGED.equals(intent.getAction())) return;
        int level = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1);
        if (level >= 0 && level <= 10) {
            final TextToSpeech[] holder = new TextToSpeech[1];
            holder[0] = new TextToSpeech(context.getApplicationContext(), result -> {
                if (result == TextToSpeech.SUCCESS) { TextToSpeech tts = holder[0]; tts.setLanguage(Locale.US); tts.setSpeechRate(0.9f); tts.speak("Boss, battery is below ten percent. Please charge the phone.", TextToSpeech.QUEUE_FLUSH, null, "low-battery"); }
            });
        }
    }
}
