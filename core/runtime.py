"""
Runtime Monitor
"""

import time
from monitors.process_monitor import ProcessMonitor
from config.configuration import Configuration
from runtime_event import RuntimeEvent
from core.registry import Registry



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

        for monitor in self.registry.get_monitors():

            monitor.sample()

            current_snapshot = monitor.get_snapshot()

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

        for name in current:

            old = previous[name]
            new = current[name]
            if old["running"] != new["running"]:
                old_state = "Running" if old["running"] else "Stopped"
                new_state = "Running" if new["running"] else "Stopped"

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

        if self.process_monitor:
            self.process_monitor.shutdown()

        self.running = False