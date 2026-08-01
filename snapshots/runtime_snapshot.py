class RuntimeSnapshot:

    def __init__(self):
        self.monitors = {}

    def add_monitor_snapshot(self, name, snapshot):
        self.monitors[name] = snapshot

    def get_monitor_snapshot(self, name):
        return self.monitors.get(name)