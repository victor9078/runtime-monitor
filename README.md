Operations Runtime

Runtime Monitor

Purpose

Provide centralized health monitoring for the Incident Engine ecosystem.

The Runtime Monitor observes the health of monitored processes, storage, network connectivity, system resources, and supporting services. It records operational events, detects abnormal conditions, and provides a single source of truth for overall system status.

It does not process scanner audio, publish incidents, or restart services.

Primary Components
Runtime Service
Process Monitor
Storage Monitor
Resource Monitor
Network Monitor
Event Engine
Alert Engine
Historical Storage
Future Components
Web Dashboard
Discord Health Status
REST API
Service Control
Metrics Export

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