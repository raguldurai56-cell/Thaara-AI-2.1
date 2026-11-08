"""Reliable Thaara AI 2.1 launcher."""
import sys


def start_jarvis():
    from main import start
    start()


def main():
    print("Starting Thaara AI 2.1...")
    try:
        start_jarvis()
    except KeyboardInterrupt:
        print("\nThaara stopped.")
        return 130
    except Exception as exc:
        print(f"Startup failed: {exc}", file=sys.stderr)
        return 1
    print("Thaara stopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
