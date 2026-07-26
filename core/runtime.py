"""
Runtime Monitor
"""

import time
from monitors.process_monitor import ProcessMonitor
from config.configuration import Configuration


class Runtime:

    def __init__(self):
        self.process_monitor = None
        
        self.configuration = Configuration()
        
        self.running = False

    def initialize(self):

        print("Initializing Runtime...")

        self.configuration.load()

        self.processes = self.configuration.get_processes()

        self.process_monitor = ProcessMonitor(processes)

        self.process_monitor.initialize()

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
        self.process_monitor.sample()
        #print("Heartbeat")        

    def shutdown(self):
        print("Stopping Runtime...")
        self.process_monitor.shutdown()
        self.running = False