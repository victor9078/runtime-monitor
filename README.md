# Runtime

## Purpose

Runtime provides centralized operational monitoring for the ALERTS ecosystem.

Runtime continuously monitors infrastructure services and system resources by collecting snapshots from one or more monitors, comparing those snapshots over time, and generating RuntimeEvents whenever monitored state changes.

Runtime is infrastructure.

It does not:
- Process scanner audio
- Generate incidents
- Publish operational data
- Monitor scanner heartbeats (handled by Watchdog)

Instead, Runtime monitors the health of supporting infrastructure while Watchdog continues to monitor scanner application health.

---

## Current Features (v1)

- Registry-based monitor architecture
- ServiceMonitor
- DiskMonitor
- RuntimeSnapshot
- RuntimeEvent
- Centralized logging
- Discord notification support
- Configuration-driven services
- Configuration-driven disk monitoring
- Configuration-driven Discord webhook
- Configuration-driven alert mention
- Graceful startup and shutdown

---

## Architecture

RRuntime
    ↓
Registry
    ↓
ServiceMonitor
DiskMonitor
    ↓
RuntimeSnapshot
    ↓
RuntimeEvent
    ↓
Logger
DiscordNotifier

---

## Current Monitors

### ServiceMonitor

Monitors configured long-running infrastructure services.

Current examples:

- JSON Publisher
- Sheet Watcher
- Internet Health
- FFmpeg (optional)

Generates RuntimeEvents whenever a service changes between Running and Stopped.

---

### DiskMonitor

Monitors configured drives.

Currently tracks:

- Total space
- Used space
- Free space
- Percent utilized

Generates RuntimeEvents whenever utilization changes.

Disk threshold configuration has been added for future alerting.

---

## Notifications

Runtime can send Discord notifications for RuntimeEvents.

Current notification types:

- Service stopped
- Service running

Notifications support:

- Configurable webhook
- Optional Discord user mention

---

## Relationship to Watchdog

Runtime and Watchdog serve different purposes.

Runtime monitors:

- Infrastructure services
- System resources

Watchdog monitors:

- Scanner monitor heartbeats
- Transcript freshness
- Automatic scanner restarts

Runtime currently complements Watchdog rather than replacing it.

## Repository Layout

============
tree

runtime-monitor/
│
├── README.md
├── LICENSE
├── requirements.txt
├── runtime.py
│
├── config/
│   ├── __init__.py
│   ├── configuration.py
│   ├── schema.py
│   └── runtime.yaml
│
├── core/
│   ├── runtime.py
│   ├── monitor.py          # Base monitor class/interface
│   ├── scheduler.py
│   └── registry.py
│
├── monitors/
│   ├── process_monitor.py
│   ├── cpu_monitor.py
│   ├── memory_monitor.py
│   ├── disk_monitor.py
│   ├── network_monitor.py
│   └── file_monitor.py
│
├── events/
│   ├── event.py
│   ├── event_logger.py
│   ├── alert_engine.py
│   └── event_types.py
│
├── snapshots/
│   ├── snapshot_service.py
│   └── snapshot_writer.py
│
├── storage/
│   ├── sqlite_store.py
│   ├── retention.py
│   └── history.py
│
├── logs/
│
└── tests/

## Roadmap

Version 1.1
- HeartbeatMonitor
- Threshold events
- Log levels

Version 2
- Recovery policies
- Additional monitors
- Dashboard integration