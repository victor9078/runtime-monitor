"""
Runtime Monitor
"""

import time
from monitors.process_monitor import ProcessMonitor
from config.configuration import Configuration
from runtime_event import RuntimeEvent
from core.registry import Registry
from snapshots.runtime_snapshot import RuntimeSnapshot



class Runtime:

    def __init__(self):
        
        
        self.configuration = Configuration()
        
        self.previous_snapshot = None
        
        self.running = False
        
        self.registry = Registry()

    def initialize(self):

        print("Initializing Runtime...")

        self.configuration.load()

        processes = self.configuration.get_processes()

        process_monitor = ProcessMonitor(processes)

        process_monitor.initialize()

        self.registry.register(process_monitor)

        self.running = True
    
    def run(self):

        print("Runtime running...")

        try:

            while self.running:

                self.tick()

                time.sleep(5)

        except KeyboardInterrupt:

            print("\nRuntime caught Ctrl+C")

            self.running = False
            
    def tick(self):

        current_snapshot = RuntimeSnapshot()

        for monitor in self.registry.get_monitors():

            monitor.sample()

            current_snapshot.add_monitor_snapshot(
                monitor.__class__.__name__,
                monitor.get_snapshot()
            )

        if self.previous_snapshot is not None:

            changes = self.compare_snapshots(
                self.previous_snapshot,
                current_snapshot
            )

            for change in changes:
                print(change)

        self.previous_snapshot = current_snapshot

    def compare_snapshots(self, previous, current):

        changes = []

        previous_processes = previous.get_monitor_snapshot("ProcessMonitor")
        current_processes = current.get_monitor_snapshot("ProcessMonitor")

        for name in current_processes:

            old = previous_processes[name]
            new = current_processes[name]

            if old["running"] != new["running"]:

                changes.append(
                    RuntimeEvent(
                        component=name,
                        field="running",
                        old=old["running"],
                        new=new["running"]
                    )
                )

        return changes
            

    def shutdown(self):

        print("Stopping Runtime...")

        for monitor in self.registry.get_monitors():
            monitor.shutdown()

        self.running = False