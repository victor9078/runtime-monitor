"""
Base Monitor class.
"""


class Monitor:

    def __init__(self, name):
        self.name = name

    def initialize(self):
        pass

    def sample(self):
        pass

    def get_snapshot(self):
        return {}

    def shutdown(self):
        pass