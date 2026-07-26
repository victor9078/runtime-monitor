"""
Process Monitor
"""

from core.monitor import Monitor


class ProcessMonitor(Monitor):

    def __init__(self):
        super().__init__("Process Monitor")

    def initialize(self):
        print(f"{self.name} initialized.")

    def sample(self):
        print(f"{self.name} sample.")

    def get_snapshot(self):
        return {
            "status": "OK"
        }

    def shutdown(self):
        print(f"{self.name} stopped.")