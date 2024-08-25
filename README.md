# pmt - Python Monitoring Tool

## Overview

`pmt` is a Python library designed to provide easy access to system monitoring functionalities on Linux-based operating systems. It allows users to retrieve various system metrics, including CPU usage, memory usage, network statistics, uptime, disk storage, and more.

## Features

- **Comprehensive System Monitoring**: Easily access information about operating system, architecture, and kernel version.
- **Network Monitoring**: Track network bandwidth usage and ping response times to major DNS servers.
- **Resource Usage**: Check CPU load, memory usage, process count, and inode usage.
- **Disk Storage Insights**: Get detailed information about disk space and inode availability.

## Installation

To install `pmt`, clone the repository and install the required dependencies listed in `requirements.txt`:

```bash
git clone https://github.com/yourusername/pmt.git
cd pmt
pip install -r requirements.txt
```

## Usage

For a quick start, refer to the sample file provided in the repository. Below is a simple example of how to use the `pmt` library:

```python
from pmt import pmt

monitor = pmt()
# see sample.py
```

## Functions

### `getOs()`
- **Output**: Returns the name and version of the operating system (e.g., "Ubuntu 20.04").

### `getArch()`
- **Output**: Returns the system architecture (e.g., "x86_64").

### `getKernel()`
- **Output**: Returns the kernel version (e.g., "5.4.0-42-generic").

### `getHostname()`
- **Output**: Returns the system hostname (e.g., "my-computer").

### `getAddr()`
- **Output**: Returns the system's IP address (e.g., "192.168.1.2").

### `getBandwidthUsage()`
- **Output**: Returns upload and download bandwidth usage (e.g., `{"download": 50000, "upload": 120000}`).

### `getUptime()`
- **Output**: Returns the system's uptime (e.g., "up 5 hours, 20 minutes").

### `getCpu()`
- **Output**: Returns CPU core count and load information (e.g., `{"cores": 4, "loadAvg": 0.75, "use": 18}`).

### `getProcess()`
- **Output**: Returns the count of running processes (e.g., `42`).

### `getRam()`
- **Output**: Returns RAM total, used, available, and usage percentage (e.g., `{"total": 16000000000, "used": 8000000000, "available": 8000000000, "use": 50}`).

### `getPing()`
- **Output**: Returns the ping time to Google and Cloudflare (e.g., `{"google": 18, "cloudflare": 16}`).

### `getStorage()`
- **Output**: Returns storage usage statistics for all mounted filesystems (e.g., `{"filesystem": {"size": "100G", "used": "50G", "available": "50G", "use": "50%"}}`).

### `getInode()`
- **Output**: Returns inode usage statistics for all mounted filesystems (e.g., `{"filesystem": {"Inodes": "1000000", "IUsed": "500000", "IFree": "500000", "use": "50%"}}`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to `pmt`, please open an issue or submit a pull request.