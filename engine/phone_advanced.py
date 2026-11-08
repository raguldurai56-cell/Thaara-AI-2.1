class PhoneAdvanced:
    def __init__(self):
        self.sms_monitoring = False
        self.call_monitoring = False

    def start_sms_monitoring(self):
        self.sms_monitoring = True
        return True

    def stop_sms_monitoring(self):
        self.sms_monitoring = False
        return True

    def start_call_monitoring(self):
        self.call_monitoring = True
        return True

    def stop_call_monitoring(self):
        self.call_monitoring = False
        return True


phone_advanced = PhoneAdvanced()
