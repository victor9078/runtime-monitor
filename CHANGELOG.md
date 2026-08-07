# Changelog

## v1.0.0 - 2026-08-06

### Architecture
- Introduced a registry-driven monitoring framework.
- Added Monitor base class and extensible monitor architecture.
- Added RuntimeSnapshot for aggregating monitor state.
- Added RuntimeEvent for representing runtime state changes.
- Added centralized timestamped logging.

### Monitors
- Added ServiceMonitor (formerly ProcessMonitor).
- Added DiskMonitor.
- Added configuration-driven monitor registration.

### Runtime
- Runtime now aggregates snapshots from multiple monitors.
- Snapshot comparison generates RuntimeEvents.
- Runtime manages monitor lifecycle through the Registry.
- Runtime performs graceful shutdown of registered monitors.

### Configuration
- Added runtime.yaml configuration.
- Added Configuration loader.
- Service definitions are configuration-driven.
- Drive monitoring is configuration-driven.

### Status
Version 1 establishes the monitoring framework. Future releases will add heartbeat monitoring, recovery policies, and additional monitor types.

## v0.1.0 - 2026-07-26

- Initial Runtime framework
- Runtime lifecycle
- Monitor base class
- ProcessMonitor stub
- Git repository initialized