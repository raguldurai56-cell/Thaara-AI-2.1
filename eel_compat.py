class _EelFallback:
    def init(self, web_dir):
        return None

    def expose(self, func=None):
        if func is None:
            return lambda f: f
        return func

    def start(self, *args, **kwargs):
        print("Eel is not installed; Thaara is running in headless mode.")

    def __getattr__(self, name):
        return lambda *args, **kwargs: None


eel = _EelFallback()
