import psutil
from core.logger import info


class DiskMonitor:

    def __init__(self, drives):
        
        self.drives = drives
        self.snapshot = {}

    def initialize(self):
        info(f"{self.__class__.__name__} initialized.")

    def sample(self):
        
        self.snapshot = {}
        
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
            
    def get_snapshot(self):
        return self.snapshot

    def shutdown(self):
        info(f"{self.__class__.__name__} stopped.")