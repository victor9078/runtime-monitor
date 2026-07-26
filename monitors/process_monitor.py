"""
Process Monitor
"""

from core.monitor import Monitor


class ProcessMonitor(Monitor):

    def __init__(self, processes):

        super().__init__("Process Monitor")

        self.processes = processes

    def initialize(self):

        print(f"{self.name} initialized.")

        for process in self.processes:
            print(f"  {process['name']}")

    def sample(self):
        print(f"{self.name} sample.")

    def get_snapshot(self):
        return {
            "status": "OK"
        }

    def shutdown(self):
        print(f"{self.name} stopped.")