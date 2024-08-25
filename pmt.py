import platform
import time
import psutil
import os
import re
import socket
import subprocess


class pmt:

    def __init__(self):
        try:
            if platform.system() != "Linux":
                exit("The detected operating system is not Linux.")
        except Exception as error:
            exit("The detected operating system is not Linux: " + str(error))

    def getOs(self):
        os = platform.linux_distribution()
        return os[0] + " " + os[1]

    def getArch(self):
        return platform.machine()

    def getKernel(self):
        return platform.uname().release

    def getHostname(self):
        return socket.gethostname()

    def getAddr(self):
        return socket.gethostbyname(self.getHostname())

    def getBandwidthUsage(self):
        counter = psutil.net_io_counters()
        lastUpload = counter.bytes_sent
        lastDownload = counter.bytes_recv
        time.sleep(1)
        counter = psutil.net_io_counters()
        upload = counter.bytes_sent
        download = counter.bytes_recv
        return {
            "download": (download - lastDownload) * 8,
            "upload": (upload - lastUpload) * 8,
        }

    def getUptime(self):
        return os.popen("uptime -p").read().strip()

    def getCpu(self):
        cpuCount = os.cpu_count()
        loadAvg = os.getloadavg()[0]
        use = (loadAvg / cpuCount) * 100
        return {"cores": cpuCount, "loadAvg": loadAvg, "use": round(use)}

    def getProcess(self):
        return len(psutil.pids())

    def getRam(self):
        memory = psutil.virtual_memory()
        total = memory.total
        available = memory.available
        used = ((total - available) / total) * 100
        return {
            "total": total,
            "used": total - available,
            "available": available,
            "use": round(used),
        }


    def getPing(self):

        try:

            google = subprocess.check_output(
                ["ping", "-c", "1", "8.8.8.8"],
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

            googleTime = re.findall(r"time=(\d+\.?\d*) ms", google)

            googleResult = googleTime[0] if googleTime else "Unknown"

        except subprocess.CalledProcessError as e:

            googleResult = e.output.strip()

        try:

            cloudflare = subprocess.check_output(
                ["ping", "-c", "1", "1.1.1.1"],
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

            cloudflareTime = re.findall(r"time=(\d+\.?\d*) ms", cloudflare)

            cloudflareResult = cloudflareTime[0] if cloudflareTime else "Unknown"

        except subprocess.CalledProcessError as e:

            cloudflareResult = e.output.strip()
            
        if re.match(r"^-?\d+(\.\d+)?$", googleResult):

            googleResult = int(round(float(googleResult)))

        elif googleResult.isdigit():

            googleResult = int(googleResult)
        else:
            googleResult = googleResult.replace("\n"," ")


        if re.match(r"^-?\d+(\.\d+)?$", cloudflareResult):

            cloudflareResult = int(round(float(cloudflareResult)))

        elif cloudflareResult.isdigit():

            cloudflareResult = int(cloudflareResult)
        else:
            cloudflareResult = cloudflareResult.replace("\n"," ")

        return {"google": googleResult, "cloudflare": cloudflareResult}



    def getStorage(self):
        df = os.popen("df -h").read()
        disks = df.strip().split("\n")
        result = {}
        for line in disks[1:]:
            columns = line.split()
            if len(columns) >= 6:
                filesystem = columns[0]
                size = columns[1]
                used = columns[2]
                available = columns[3]
                usePercent = columns[4]
                mountPoint = columns[5]

                result[filesystem] = {
                    "size": size,
                    "used": used,
                    "available": available,
                    "use": usePercent,
                    "mountpoint": mountPoint,
                }
        return result

    def getInode(self):
        df = os.popen("df -i").read()
        disks = df.strip().split("\n")
        result = {}
        for line in disks[1:]:
            columns = line.split()
            if len(columns) >= 6:
                filesystem = columns[0]
                inodes = columns[1]
                used = columns[2]
                available = columns[3]
                usePercent = columns[4]
                mountPoint = columns[5]

                result[filesystem] = {
                    "Inodes": inodes,
                    "IUsed": used,
                    "IFree": available,
                    "use": usePercent,
                    "mountpoint": mountPoint,
                }
        return result
