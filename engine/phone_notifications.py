class PhoneMonitor:
    def __init__(self):
        self.monitoring = False

    def start_monitoring(self):
        self.monitoring = True
        return True

    def stop_monitoring(self):
        self.monitoring = False
        return True


phone_monitor = PhoneMonitor()
