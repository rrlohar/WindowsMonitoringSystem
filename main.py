import psutil
from plyer import notification


"""Measure CPU Time"""
def monitor_cpu_times():
    print("\n** CPU TIMES **")
    cpu_times = psutil.cpu_times()
    user_time = round(cpu_times.user / 3600)
    system_time = round(cpu_times.system / 3600)
    idle_time = round(cpu_times.idle / 3600)
    print("Time Spent on Processes by the User : {}".format(user_time))
    print("Time Spent on Processes by the System : {}".format(system_time))
    print("Time Spent on Processes by Idle : {}".format(idle_time))


"""Measure CPU Util"""
def monitor_cpu_util():
    print("\n** CPU UTIL **")
    print(psutil.cpu_percent())


"""Count CPU Working Cores"""
def monitor_cpu_cores():
    print("\n** CPU CORES **")
    print(psutil.cpu_count())


"""Measure CPU Frequencies"""
def monitor_cpu_freq():
    print("\n** CPU FREQUENCIES **")
    print("{} MHz".format(psutil.cpu_freq().current))


"""Monitor RAM Usage"""
def monitor_ram():
    print("\n** RAM USAGE **")
    virtual_memory = psutil.virtual_memory()
    print("Total Memory {} Bytes".format(virtual_memory.total))
    print("Available Memory {} 'Bytes".format(virtual_memory.available))
    print("Used Memory {} Bytes".format(virtual_memory.used))
    print("Percent Used {} %".format(virtual_memory.percent))
    ram_per = virtual_memory.percent
    if ram_per >= 90:
        notification.notify(
            title = "RAM Usage Warning..!",
            message = "Hey User You Have Almost "+str(ram_per) + "% RAM Used Please Close Unnecessary Tasks",
            app_icon = "C:\\Users\\rrlon\\Downloads\\Iconsmind-Outline-Ram.ico",
            timeout = 20)


"""Disk Utilization"""
def monitor_disk_usage():
    print("\n** DISK USAGE **")
    disk_usage = psutil.disk_usage('/')
    print("Total Memory {} Bytes".format(disk_usage.total))
    print("Free Memory {} Bytes".format(disk_usage.free))
    print("Used Memory {} Bytes".format(disk_usage.used))
    print("Percent Used {} %".format(disk_usage.percent))


"""Monitor Network Requests"""
def monitor_network():
    print("\n** NETWORK REQUESTS **")
    io_stats = psutil.net_io_counters()
    print("Total Bytes Sent {}".format(io_stats.bytes_sent))
    print("Total Bytes Received {}".format(io_stats.bytes_recv))


"""Monitor Battery Usage"""
def monitor_battery():
    print("\n** BATTERY DETAILS **")
    battery_info = psutil.sensors_battery()
    print("Battery Percent {} %".format(battery_info.percent))
    print("Seconds Left {}".format(battery_info.secsleft))
    battery_per = battery_info.percent
    if battery_per <= 20:
        notification.notify(
            title = "Low Battery..!",
            message = "Hey User You Have Almost " + str(battery_per) + "% Battery Used Please Connect Charger",
            timeout=10,
            app_icon="C:\\Users\\rrlon\\Downloads\\Custom-Icon-Design-Pretty-Office-9-Battery-1.ico")
    elif battery_per == 100:
        notification.notify(
            title = "Battery Fully Charged..!",
            message = "Hey User You Have " + str(battery_per) + "% Battery Charged Please Unplugged the Charger",
            timeout=10,
            app_icon="C:\\Users\\rrlon\\Downloads\\Oxygen-Icons.org-Oxygen-Status-battery-charging.ico")


if __name__ == '__main__':
    monitor_cpu_times()
    monitor_cpu_util()
    monitor_cpu_cores()
    monitor_cpu_freq()
    monitor_ram()
    monitor_disk_usage()
    monitor_network()
    monitor_battery()
