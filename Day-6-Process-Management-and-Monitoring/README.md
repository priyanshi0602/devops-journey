# Day 6 - Linux Processes and Monitoring 🚀

Today I learned about Linux processes, system monitoring, aliases, environment variables, and process management.

---

## Topics Covered

### Linux Processes

Commands practiced:

```bash
ps
ps aux
Learned how Linux manages running applications and services.
System Monitoring

Commands used:

top
free -h
df -h
uptime

These commands help monitor:

CPU usage
Memory usage
Disk usage
System uptime
Background Processes

Started a background process:

sleep 300 &

Checked running jobs:

jobs

Found process ID:

ps aux | grep sleep

Killed process:

kill PID
Linux Aliases

Created shortcut command:

alias ll='ls -la'
Environment Variables

Commands practiced:

echo $HOME
echo $USER
echo $PATH

Learned how Linux stores system configuration and command locations.

Bash Monitoring Script

Created:

system-health.sh

The script displays:

current user
uptime
memory usage
disk usage
top processes
Key Learning

Today I learned how Linux handles running processes and system monitoring. These concepts are important for DevOps, cloud infrastructure, automation, and troubleshooting production systems.