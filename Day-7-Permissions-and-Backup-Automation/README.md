# Day 7 - Linux Permissions and Ownership 🚀

Today I learned about Linux file permissions, ownership, chmod, and basic backup automation.

---

## Topics Covered

### Linux File Permissions

Linux controls file access using permissions.

Permission Types:
- r -> read
- w -> write
- x -> execute

Permission Groups:
- owner
- group
- others

Example:
```bash
-rwxr-xr-x

Permission Commands

Commands practiced:

ls -l
chmod +x filename

Learned how Linux secures files and controls access.

chmod Command

Used chmod to modify file permissions.
Examples:

chmod +x testfile.txt
chmod 755 script.sh
File Ownership

Learned that Linux files have:

owners
groups

Commands practiced:

ls -l

Backup Automation Script

Created:

backup.sh

The script:

creates backup folder
copies files automatically
simulates basic backup automation

#Key Learning

Today I learned how Linux permissions and ownership work. These concepts are essential for Linux security, shell scripting, DevOps automation, and cloud infrastructure management.