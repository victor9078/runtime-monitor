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

    def get_processes(self):

        return self.config.get("processes", [])