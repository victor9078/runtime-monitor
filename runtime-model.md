# Runtime Model

## Purpose

The Runtime Model defines the logical objects used by the Runtime Monitor.

It describes the information the Runtime maintains about the operating environment, monitored processes, storage devices, system resources, and operational events.

The Runtime Model is implementation-independent and serves as the authoritative reference for developers and future system components.

## Design Principle

Runtime Monitor is an observation system.

Monitors collect observations.

The Runtime maintains current state.

Events are generated from changes in state, not from observations themselves.

Actions (logging, notifications, restarts, dashboards) respond to events rather than interacting directly with monitors.

## Core Objects 

### Runtime
Represents the Runtime service itself.
| Field         | Type     | Description                |
| ------------- | -------- | -------------------------- |
| RuntimeID     | String   | Unique instance identifier |
| Version       | String   | Runtime version            |
| Hostname      | String   | Computer name              |
| OS            | String   | Operating system           |
| PythonVersion | String   | Python runtime version     |
| StartTime     | DateTime | When Runtime started       |
| CurrentTime   | DateTime | Current timestamp          |
| Uptime        | Duration | Runtime uptime             |
| LastHeartbeat | DateTime | Last successful loop       |

### Process
Represents one monitored process.
| Field       | Type     | Description               |
| ----------- | -------- | ------------------------- |
| Name        | String   | Friendly process name     |
| PID         | Integer  | Process ID                |
| ParentPID   | Integer  | Parent process            |
| Status      | Enum     | Running, Stopped, Unknown |
| StartTime   | DateTime | Process start time        |
| Uptime      | Duration | Process uptime            |
| CPUPercent  | Float    | CPU usage                 |
| MemoryBytes | Integer  | Memory consumption        |
| ThreadCount | Integer  | Number of threads         |
| Executable  | String   | Executable path           |
| CommandLine | String   | Launch command            |


### Disk
One logical drive.
| Field               | Type    |
| ------------------- | ------- |
| DriveLetter         | String  |
| Label               | String  |
| FileSystem          | String  |
| TotalBytes          | Integer |
| UsedBytes           | Integer |
| FreeBytes           | Integer |
| PercentUsed         | Float   |
| ReadBytesPerSecond  | Float   |
| WriteBytesPerSecond | Float   |

### Resource
Overall system resources.
| Field           | Type    |
| --------------- | ------- |
| CPUPercent      | Float   |
| MemoryTotal     | Integer |
| MemoryUsed      | Integer |
| MemoryAvailable | Integer |
| DiskQueueLength | Float   |
| NetworkSent     | Integer |
| NetworkReceived | Integer |

### Event
Everything important becomes an Event.
| Field        | Type     |
| ------------ | -------- |
| EventID      | String   |
| Timestamp    | DateTime |
| Severity     | Enum     |
| Category     | Enum     |
| Source       | String   |
| Message      | String   |
| Details      | Object   |
| Acknowledged | Boolean  |


## Enumerations

### Process Status
Running
Stopped
Unknown

###Severity 
Information
Warning
Error
Critical

### Event Category 
Process
Disk
CPU
Memory
Network
Runtime
Configuration

## Relationships
Runtime
 ├── Processes (0..*)
 ├── Disks (1..*)
 ├── Resources (1)
 └── Events (0..*)
 
 ## Design Principles
 
 ### Immutable
 These never change.
 
Hostname
RuntimeID
StartTime

###Dynamic
Updated continuously.

CPUPercent
MemoryBytes
FreeBytes
LastHeartbeat

### Derived
Calculated.

Uptime
PercentUsed
MemoryPercent

## Future Objects

Network Interface
Scanner
Audio Feed
Service
Scheduled Task
Database
Alert
Notification
Health Check

 
 