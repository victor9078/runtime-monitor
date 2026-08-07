"""
Runtime Configuration
"""

from pathlib import Path

import yaml


class Configuration:

    def __init__(self):

        self.config = {}

    def load(self):

        config_file = Path(__file__).parent / "runtime.yaml"

        with open(config_file, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    def get_services(self):
        return self.config.get("services", [])
        
    def get_drives(self):
        return self.config.get("drives", [])
        
    def get_system_health_webhook(self):
        return self.config.get("discord", {}).get("system_health_webhook")
        
    def get_alert_mention(self):
        return self.config.get("discord", {}).get("alert_mention", "")