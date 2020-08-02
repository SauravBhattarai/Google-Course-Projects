
#!/usr/bin/env/python

import shutil as sh
import psutil as ps

limit_free_space = 5
limit_cpu_percent = 50

def check_disk_usage(disk):
    du = sh.disk_usage(disk)
    free_space_percent = du.free/du.total * 100
    return free_space_percent > limit_free_space
    
def check_cpu_usage():
    usage = ps.cpu_percent(0.1)
    return usage < limit_cpu_percent

if not check_disk_usage("/") and not check_cpu_usage():
    print("ERROR!")
elif not check_disk_usage("/") and check_cpu_usage():
    print("Disk is low on space")
elif not check_cpu_usage() and check_disk_usage("/"):
    print("CPU is taking a toll.")
else:
    print("Everything is OK.")