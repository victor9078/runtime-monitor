"""
Monitor Registry
"""


class Registry:

    def __init__(self):
        self.monitors = []

    def register(self, monitor):
        self.monitors.append(monitor)

    def get_monitors(self):
        return self.monitors