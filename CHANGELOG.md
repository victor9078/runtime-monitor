# Changelog


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

### Changed
- ProcessMonitor now receives its configuration from Runtime instead of relying on hardcoded values.
- Runtime initialization sequence now loads configuration before creating monitors.

## v0.1.0 - 2026-07-26

- Initial Runtime framework
- Runtime lifecycle
- Monitor base class
- ProcessMonitor stub
- Git repository initialized