# PMT (Performance Monitoring Tool) 

PMT is a Python library specifically designed for monitoring and gathering performance metrics on Linux systems. With PMT, you can easily access vital information about your system's resources such as CPU usage, RAM usage, network bandwidth, storage, and more.

## Features

- Retrieve operating system information (version and distribution)
- Get system architecture (32-bit or 64-bit)
- Access the Linux kernel version
- Retrieve the hostname
- Monitor network bandwidth usage
- Get system uptime
- Check CPU load and usage
- Count the number of running processes
- Get RAM details
- Conduct ping tests to Google and Cloudflare
- Retrieve storage and inode usage

## Installation

To use PMT, you need to have Python installed on your machine. Download the `pmt.py` file and include it in your project.

To install the required package, run:
```bash
pip install psutil
```

## Usage

### Importing the Library

First, import the library:
```python
from pmt import pmt
```

### Creating an Instance

Create an instance of the `pmt` class:
```python
monitor = pmt()
```

### Method Explanations

1. **`getOs()`**
   - Returns the operating system name and version.
   - **Usage:**
     ```python
     print(monitor.getOs())
     ```

2. **`getArch()`**
   - Returns the system architecture (e.g., x86_64).
   - **Usage:**
     ```python
     print(monitor.getArch())
     ```

3. **`getKernel()`**
   - Returns the Linux kernel version.
   - **Usage:**
     ```python
     print(monitor.getKernel())
     ```

4. **`getHostname()`**
   - Returns the hostname of the machine.
   - **Usage:**
     ```python
     print(monitor.getHostname())
     ```

5. **`getBandwidthUsage()`**
   - Monitors network bandwidth by tracking upload and download data.
   - Returns a dictionary with download and upload amounts in bytes.
   - **Usage:**
     ```python
     print(monitor.getBandwidthUsage())
     ```

6. **`getUptime()`**
   - Returns the system uptime in a human-readable format.
   - **Usage:**
     ```python
     print(monitor.getUptime())
     ```

7. **`getCpu()`**
   - Returns CPU statistics, including the number of cores, load average, and CPU usage percentage.
   - **Usage:**
     ```python
     print(monitor.getCpu())
     ```

8. **`getProcess()`**
   - Returns the count of currently running processes.
   - **Usage:**
     ```python
     print(monitor.getProcess())
     ```

9. **`getRam()`**
   - Returns RAM usage details including total, used, available memory, and usage percentage.
   - **Usage:**
     ```python
     print(monitor.getRam())
     ```

10. **`getPing()`**
    - Performs a ping test to Google and Cloudflare, returning the latency time.
    - **Usage:**
      ```python
      print(monitor.getPing())
      ```

11. **`getStorage()`**
    - Provides information about disk usage, including size, used, available space, and mount points.
    - Returns a dictionary where each key is a filesystem.
    - **Usage:**
      ```python
      print(monitor.getStorage())
      ```

12. **`getInode()`**
    - Returns inode usage statistics for each filesystem.
    - **Usage:**
      ```python
      print(monitor.getInode())
      ```

### Example

Here’s a simple example that demonstrates how to use the PMT library:

```python
from pmt import pmt

monitor = pmt()

print("Operating System:", monitor.getOs())
print("CPU Details:", monitor.getCpu())
print("Memory Usage:", monitor.getRam())
print("Network Bandwidth Usage:", monitor.getBandwidthUsage())
print("Disk Usage:", monitor.getStorage())
print("Ping to Google:", monitor.getPing()['google ping'])
```

## Requirements

- Python 3.x
- `psutil` library (install with `pip install psutil`)

## Contributing

Contributions are welcome! If you have suggestions or find bugs, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.