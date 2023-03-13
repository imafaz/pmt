import os
import re
import time
import subprocess
import requests


token = '5579225190:AAGjX-VQxqSixEEFTDuHdbHBgtMzjAL8Kk8'
chat_id = 1826312667

def bot(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=data)
    return response.json()
    
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
            output += key + KEY + '\n' + tree(value, depth + 1)
        else:
            output += key + KEY + str(value) + '\n'
        current += 1

    return output


def get_memory_usage():
    with open('/proc/meminfo', 'r') as f:
        meminfo = f.read()
    total = int(re.findall(r'MemTotal:\s+(\d+)', meminfo)[0])
    available = int(re.findall(r'MemAvailable:\s+(\d+)', meminfo)[0])
    used = total - available
    free = available
    return {
        'total memory': str(round(total / 1024 / 1024, 2)) + 'GB',
        'free memory': str(round(free / 1024 / 1024, 2)) + 'GB',
        'used memory': str(round(used / 1024 / 1024, 2)) + 'GB',
    }


def get_cpu_load():
    load1, load5, load15 = os.getloadavg()
    return {
        'Current load': load1,
        '5 minutes ago load': load5,
        '15 minutes ago load': load15,
    }


def get_network_traffic():
    output = subprocess.check_output(["ifconfig"])
    output = output.decode("utf-8")
    match = re.search(r"^(\w+):", output, re.MULTILINE)
    if match:
        interface_name = match.group(1)
    else:
        return "network interface noy found"
    stats_path = f"/sys/class/net/{interface_name}/statistics"
    if not os.path.exists(stats_path):
        print(f"Interface {interface_name} does not exist.")
        return {}

    with open(os.path.join(stats_path, "rx_bytes"), "r") as f:
        rx_bytes_1 = int(f.read())
    with open(os.path.join(stats_path, "tx_bytes"), "r") as f:
        tx_bytes_1 = int(f.read())
    time.sleep(1)
    with open(os.path.join(stats_path, "rx_bytes"), "r") as f:
        rx_bytes_2 = int(f.read())
    with open(os.path.join(stats_path, "tx_bytes"), "r") as f:
        tx_bytes_2 = int(f.read())

    in_traffic = (rx_bytes_2 - rx_bytes_1) / 1024**2
    out_traffic = (tx_bytes_2 - tx_bytes_1) / 1024**2
    total_received = rx_bytes_2 / 1024**2
    total_sent = tx_bytes_2 / 1024**2

    return {
        "in coming traffic": f"{in_traffic:.2f} MB",
        "out going traffic": f"{out_traffic:.2f} MB",
        "Total recieved": f"{total_received:.2f} MB",
        "Total sent": f"{total_sent:.2f} MB",
    }


def get_ping_times():
    localhost_ping = os.popen('ping -c 1 localhost').read()
    google_ping = os.popen('ping -c 1 google.com').read()
    telegram_ping = os.popen('ping -c 1 api.telegram.org').read()
    return {
        'localhost ping': re.findall(r'time=(.+)', localhost_ping)[0],
        'google.com ping': re.findall(r'time=(.+)', google_ping)[0],
        'api.telegram.org ping': re.findall(r'time=(.+)', telegram_ping)[0],
    }

while True:
    with open('/etc/os-release', 'r') as f:
        os_info = {}
        for line in f:
            if line.startswith('PRETTY_NAME='):
                os_info['os'] = line.strip()[13:-1]
            elif line.startswith('VERSION_ID='):
                os_info['os'] = line.strip()[12:-1]
    data = {
        'hostname': os.uname().nodename,
        'os': os_info['os'],
        'uptime': os.popen('uptime -p').read().strip(),
        'traffic': get_network_traffic(),
        'memory': get_memory_usage(),
        'cpu load': get_cpu_load(),
        'ping': get_ping_times(),
        'time': {'watch': time.strftime('%H:%M:%S')},
    }

    bot(token, chat_id,tree(data))
    time.sleep(10)
