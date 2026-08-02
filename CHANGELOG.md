# Changelog

## Unreleased

### Changed
- Snapshot comparison now returns RuntimeEvent objects instead of printing directly.
- Runtime consumes RuntimeEvent objects and is responsible for presenting changes.

### Added
- Introduced the RuntimeEvent model to represent runtime state changes.

## Unreleased

### Added
- Created the Configuration class to load settings from `runtime.yaml`.
- Runtime now loads configuration during initialization.
- Process definitions are passed from Runtime to ProcessMonitor.
- Established dependency injection between Runtime and ProcessMonitor.
### Added
- ProcessMonitor now builds structured process snapshots.
- Runtime captures running status, PID, executable name, and command line for configured processes.
- Optional and required process metadata are included in snapshots.

## Unreleased

### Added
- Runtime detects process running/stopped state changes between polling intervals.
- Process state transitions are reported to the console in a human-readable format.

### Changed
- ProcessMonitor now receives its configuration from Runtime instead of relying on hardcoded values.
- Runtime initialization sequence now loads configuration before creating monitors.

### RuntimeSnapshot Integration

- Integrated RuntimeSnapshot into the Runtime execution pipeline.
- Runtime now aggregates monitor snapshots into a single RuntimeSnapshot.
- compare_snapshots() now compares RuntimeSnapshots instead of individual monitor snapshots.
- Runtime shutdown now iterates over the Registry instead of directly managing ProcessMonitor.
- Completed transition to a registry-driven monitoring architecture.

### Disk Monitor

- Added DiskMonitor.
- Added drive configuration support.
- DiskMonitor collects total, used, free, and percentage used.
- Runtime now hosts multiple monitor types through the Registry.

## v0.1.0 - 2026-07-26

- Initial Runtime framework
- Runtime lifecycle
- Monitor base class
- ProcessMonitor stub
- Git repository initialized