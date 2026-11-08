import unittest

from engine.command import allCommands, get_continuous_listen_status, start_continuous_listen, stop_continuous_listen
from engine.dual_ai import get_simple_response
from engine.system_monitor import getSystemStats


class CoreTests(unittest.TestCase):
    def test_command_returns_response(self):
        self.assertIn("hello", allCommands("hello").lower())

    def test_system_status_is_portable(self):
        stats = getSystemStats()
        self.assertIn("platform", stats)
        self.assertGreaterEqual(stats["cpu_count"], 1)

    def test_listening_state(self):
        stop_continuous_listen()
        self.assertEqual(get_continuous_listen_status(), "Disabled")
        start_continuous_listen()
        self.assertEqual(get_continuous_listen_status(), "Enabled")
        stop_continuous_listen()

    def test_offline_ai_fallback(self):
        self.assertIn("Offline mode", get_simple_response("test"))


if __name__ == "__main__":
    unittest.main()
