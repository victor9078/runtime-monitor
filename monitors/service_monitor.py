"""
Service Monitor
"""

from core.monitor import Monitor
import psutil
from core.logger import info


class ServiceMonitor(Monitor):

    def __init__(self, services):

        super().__init__("Service Monitor")

        self.services = services
        self.snapshot = {}

    def initialize(self):

        info(f"{self.name} initialized.")

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
        # print("self.services =", self.services)
        # print(type(self.services))

        for service in self.services:

            status = self.find_process(service["match"])

            self.snapshot[service["name"]] = {
                **status,
                "required": service["required"]
            }

    def get_snapshot(self):
         return self.snapshot
        

    def shutdown(self):
        info(f"{self.name} stopped.")