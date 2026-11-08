"""Portable system status helpers."""
import os
import platform


def getSystemStats():
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "cpu_count": os.cpu_count() or 1,
    }
