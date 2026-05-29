# Day 14 - Linux Logs & Monitoring 🚀

Today I learned how Linux logs work and how system monitoring is performed using log files and monitoring commands.

---

# Topics Covered

## Linux Logs

Logs store:
- system activity
- errors
- warnings
- security events

Common log location:

```bash
/var/log/

Monitoring Commands

Learned monitoring tools:

top
tail
head
journalctl

These help administrators monitor server activity and troubleshoot issues.

head and tail Commands

Commands practiced:

head server.log

tail server.log

Real-time monitoring:

tail -f server.log
Real-Time Log Monitoring

Created and monitored a sample log file live using:

tail -f

Learned how production systems are monitored continuously.

System Logs

Viewed real Linux logs using:

sudo tail /var/log/syslog
Automation Script

Created:

log-monitor.sh

The script:

displays recent system logs
automates monitoring tasks
demonstrates Linux log analysis basics

#Key Learning

Today I understood how Linux logs and monitoring work, and how DevOps engineers use logs to monitor servers, debug systems, and track production issues.