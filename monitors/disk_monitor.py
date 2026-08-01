import psutil


class DiskMonitor:

    def __init__(self, drives):
        
        self.drives = drives
        self.snapshot = {}

    def initialize(self):
        print(f"{self.__class__.__name__} initialized.")

    def sample(self):
        
        self.snapshot = {}
        print(self.drives)
        for drive in self.drives:

            try:
                usage = psutil.disk_usage(drive + "\\")

                self.snapshot[drive] = {
                    "total": usage.total,
                    "used": usage.used,
                    "free": usage.free,
                    "percent": usage.percent
                }

            except FileNotFoundError:

                self.snapshot[drive] = {
                    "available": False
                }
            print(self.snapshot)
    def get_snapshot(self):
        return self.snapshot

    def shutdown(self):
        print(f"{self.__class__.__name__} stopped.")