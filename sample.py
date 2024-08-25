from pmt import pmt

monitor = pmt()


def tree(data, depth=0):
    FINAL = " └ "
    ENTRY = " ├ "
    SKIP = " ┊ "
    KEY = ": "
    output = ""

    if not isinstance(data, dict):
        return data

    final = len(data) - 1
    current = 0

    for key, value in data.items():
        for i in range(depth):
            output += SKIP
        output += FINAL if current == final else ENTRY
        if isinstance(value, dict):
            output += key + KEY + "\n" + tree(value, depth + 1)
        else:
            output += key + KEY + str(value) + "\n"
        current += 1

    return str(output)


def BandwidthToReadable(B):
    KB = float(1024)
    MB = float(KB**2)  # 1,048,576
    GB = float(KB**3)  # 1,073,741,824
    TB = float(KB**4)  # 1,099,511,627,776
    B = float(B)
    if B < KB:
        return f"{B} bit"
    elif KB <= B < MB:
        return f"{B/KB:.2f} kb"
    elif MB <= B < GB:
        return f"{B/MB:.2f} mb"
    elif GB <= B < TB:
        return f"{B/GB:.2f} gb"
    elif TB <= B:
        return f"{B/TB:.2f} tb"


def BytesToReadable(B):
    KB = float(1024)
    MB = float(KB**2)  # 1,048,576
    GB = float(KB**3)  # 1,073,741,824
    TB = float(KB**4)  # 1,099,511,627,776
    B = float(B)
    if B < KB:
        return f"{B} Byte"
    elif KB <= B < MB:
        return f"{B/KB:.2f} KB"
    elif MB <= B < GB:
        return f"{B/MB:.2f} MB"
    elif GB <= B < TB:
        return f"{B/GB:.2f} GB"
    elif TB <= B:
        return f"{B/TB:.2f} TB"


ram = monitor.getRam()
bandwidth = monitor.getBandwidthUsage()
data = {
    "addr": monitor.getAddr(),
    "os": monitor.getOs(),
    "arch": monitor.getArch(),
    "kernel": monitor.getKernel(),
    "hostname": monitor.getHostname(),
    "bandwidth": {
        "download": BandwidthToReadable(bandwidth["download"]),
        "upload": BandwidthToReadable(bandwidth["upload"]),
    },
    "uptime": monitor.getUptime(),
    "cpu usage": monitor.getCpu(),
    "ram usage": {
        "total": BytesToReadable(ram["total"]),
        "used": BytesToReadable(ram["used"]),
        "available": BytesToReadable(ram["available"]),
        "use": str(ram["use"]) + "%",
    },
    "ping": monitor.getPing(),
    "process count": monitor.getProcess(),
    "storage": monitor.getStorage(),
    "inode": monitor.getInode(),
}

print(tree(data))
