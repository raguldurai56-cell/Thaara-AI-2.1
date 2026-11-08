"""Optional Android fingerprint adapter."""


class FingerprintAuth:
    def register(self):
        return False

    def authenticate(self):
        return False
