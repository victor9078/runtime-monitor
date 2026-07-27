"""
Process Monitor
"""

from core.monitor import Monitor
import psutil


class ProcessMonitor(Monitor):

    def __init__(self, processes):

        super().__init__("Process Monitor")

        self.processes = processes
        self.snapshot = {}

    def initialize(self):

        print(f"{self.name} initialized.")

    def find_process(self, match):
        """
        Find a running process whose command line contains the
        configured match string.
        """

        for proc in psutil.process_iter(["pid", "name", "cmdline"]):

            try:
                cmdline = proc.info.get("cmdline")

                if not cmdline:
                    continue

                cmdline_text = " ".join(cmdline)

                if match.lower() in cmdline_text.lower():

                    return {
                        "running": True,
                        "pid": proc.info["pid"],
                        "name": proc.info["name"],
                        "cmdline": cmdline_text
                    }

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                continue

        return {
            "running": False,
            "pid": None,
            "name": None,
            "cmdline": None
        }    

    def sample(self):

        self.snapshot = {}

        for process in self.processes:

            status = self.find_process(process["match"])

            self.snapshot[process["name"]] = {
                **status,
                "required": process["required"]
            }

    def get_snapshot(self):
         return self.snapshot
        

    def shutdown(self):
        print(f"{self.name} stopped.")