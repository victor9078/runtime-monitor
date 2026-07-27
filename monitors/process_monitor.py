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

        

    def sample(self):
        import psutil

        for proc in psutil.process_iter(["pid", "name", "cmdline"]):

            info = proc.info

            cmdline = info.get("cmdline")

            if not cmdline:
                continue

            cmdline_text = " ".join(cmdline)

            if ".py" in cmdline_text.lower():
                print(info)

    def get_snapshot(self):
        return {
            "status": "OK"
        }

    def shutdown(self):
        print(f"{self.name} stopped.")