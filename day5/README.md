# Day 5 - SSH, Ports and Cron Jobs 🚀

Today I learned about Linux networking, users, and task automation.

---

## Topics Covered

### SSH (Secure Shell)
SSH is used to securely access remote Linux servers.

Basic syntax:
```bash
ssh username@server-ip
#for example:
ssh ubuntu@192.168.1.10
#Networking Ports

#Common ports:

22 -> SSH
80 -> HTTP
443 -> HTTPS

#Commands practiced:
ss -tuln
ss -tuln | grep 80
Users and Groups

#Commands practiced:

whoami
id
groups

#Learned how Linux manages user identities and permissions.

#Cron Jobs (Task Automation)

#Commands practiced:
crontab -e
#Created my first automated cron job that runs every 2 minutes and writes output into a file.

#example:
*/2 * * * * echo "Cron job running" >> ~/cron-test.txt