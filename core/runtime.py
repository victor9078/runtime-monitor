"""
Runtime Monitor
"""

import time
from monitors.process_monitor import ProcessMonitor
from config.configuration import Configuration
from runtime_event import RuntimeEvent
from core.registry import Registry
from snapshots.runtime_snapshot import RuntimeSnapshot
from monitors.disk_monitor import DiskMonitor
from core.logger import info



class Runtime:

    def __init__(self):
        
        
        self.configuration = Configuration()
        
        self.previous_snapshot = None
        
        self.running = False
        
        self.registry = Registry()

    def initialize(self):

        info("Initializing Runtime...")

        self.configuration.load()

        processes = self.configuration.get_processes()

        process_monitor = ProcessMonitor(processes)

        process_monitor.initialize()

        self.registry.register(process_monitor)

        drives = self.configuration.get_drives()

        disk_monitor = DiskMonitor(drives)

        disk_monitor.initialize()

        self.registry.register(disk_monitor)

        self.running = True
    
    def run(self):

        info("Runtime running...")

        try:

            while self.running:

                self.tick()

                time.sleep(5)

        except KeyboardInterrupt:

            info("Runtime interrupted (Ctrl+C)")

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
                info(str(change))

        self.previous_snapshot = current_snapshot

    def compare_snapshots(self, previous, current):

        changes = []

        previous_processes = previous.get_monitor_snapshot("ProcessMonitor")
        current_processes = current.get_monitor_snapshot("ProcessMonitor")
        previous_disks = previous.get_monitor_snapshot("DiskMonitor")
        current_disks = current.get_monitor_snapshot("DiskMonitor")

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

        for drive in current_disks:

            old = previous_disks.get(drive)
            new = current_disks.get(drive)
            
            if old is None or new is None:
                continue

            if round(old["percent"]) != round(new["percent"]):

                changes.append(
                    RuntimeEvent(
                        component=drive,
                        field="percent",
                        old=old["percent"],
                        new=new["percent"]
                    )
                )
        
        return changes
            

    def shutdown(self):

        info("Stopping Runtime...")

        for monitor in self.registry.get_monitors():
            monitor.shutdown()

        self.running = False