import pbfetch.parse_funcs.parse_uptime as uptime
import pbfetch.parse_funcs.parse_os as pos
import pbfetch.parse_funcs.parse_temp as temp
import pbfetch.parse_funcs.parse_cpu as cpu
import pbfetch.parse_funcs.parse_mem as mem
import pbfetch.parse_funcs.parse_login as login
import pbfetch.parse_funcs.parse_kernel as kernel
import pbfetch.parse_funcs.parse_hostname as hostname
# import pbfetch.parse_funcs.parse_cpu_usage as cpu_usage

import subprocess, platform, psutil
from os import uname, statvfs


def stats():
    # constant for checking cpu usage (in seconds)
    DELAY = 0.2



    ################################
    #####         STATS        #####
    ################################



    # uname = tuple(platform.uname())
    _uname = tuple(uname())
    system = _uname[0]
    stat_user = login.parse_login()
    stat_host = _uname[1]
    stat_kernel_ver = _uname[2]
    stat_architecture = _uname[4]
    stat_hostname = f"{stat_user}@{stat_host}"
    # stat_hostname = f"{login.parse_login()}@{hostname.parse_hostname()}"
    stat_os = pos.parse_os()
    # stat_arch = platform.machine()
    stat_kernel = kernel.parse_kernel_release()
    stat_uptime = uptime.parse_uptime()
    stat_cpu_percent = f"{round(psutil.cpu_percent(DELAY))}%"
    # stat_cpu_percent = f"{cpu_usage.parse_cpu_usage()}%"
    stat_cpu_temp = f"{temp.parse_temp()}°c" 
    stat_cpu_name = cpu.parse_cpu()
    ram_total, ram_used = mem.parse_mem()
    stat_arch = platform.machine()
    stat_ram = str(
        f"{round(ram_used/1024)}/"
        f"{round(ram_total/1024)}"
        " MB"
    ) if ram_total and ram_used else None
    stat_packages = f"{len(
        str(
            subprocess.check_output(["pacman", "-Q"])
        ).split(" ")
    )} (pacman)"
    stat_vfs = statvfs("/")
    total_disk_size_in_bytes = stat_vfs.f_frsize * stat_vfs.f_blocks
    total_disk_size_in_gb = round(
        total_disk_size_in_bytes / (1024.0 ** 2)
    )
    disk_free_space_gb = round(
        stat_vfs.f_frsize * stat_vfs.f_bfree / (1024.0 ** 2)
    )
    total_disk_size_used = total_disk_size_in_gb - disk_free_space_gb
    stat_disk_total_and_used = (
        f"{total_disk_size_used}/{total_disk_size_in_gb} MB"
    )

    # TODO: add easter egg stats for fun dynamic things
    # init stats using keywords for configuration in .conf
    stats = {
        # "$UNAME": _uname,
        "$HOST": stat_hostname,
        "$SYS": stat_os,
        # "$ARCH": stat_arch,
        "$ARCH": stat_architecture,
        "$KER": stat_kernel,
        "$MEM": stat_ram,
        "$UP": stat_uptime,
        "$PAC": stat_packages,
        "$CPU": stat_cpu_name,
        "$TEM": stat_cpu_temp,
        "$PT": stat_cpu_percent,
        "$DISK": stat_disk_total_and_used,
    }



        ################################
        #####     END OF STATS     #####
        ################################



    return stats
