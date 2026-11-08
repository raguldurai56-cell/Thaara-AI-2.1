# Thaara Android companion

This free Android companion targets Moto G67 Power 5G and currently provides:

- Female Android Text-to-Speech voice.
- Low-battery reminder when battery is 10% or lower.
- Missed-call reading after call-log permission is granted.
- A permission screen and voice test button.

## Build

From the repository root:

```bash
cd android
./gradlew assembleDebug
```

The APK is written to `app/build/outputs/apk/debug/app-debug.apk`.

The PC sync bridge, Gmail/Calendar OAuth, and secure outside-network endpoint
are intentionally separate next steps; this first APK is a safe phone-alert
foundation and does not upload call data anywhere.
