# Day 10 - Linux Users and Groups 👨‍💻

Today I learned how Linux manages users, groups, permissions, and administrator access.

---

# Topics Covered

## Linux Users

Linux is a multi-user operating system.

Learned:
- user accounts
- home directories
- user identification
- user management

Commands practiced:

```bash
whoami
id
echo $HOME
echo $USER

Linux Groups

Groups help manage permissions for multiple users.

Commands practiced:

groups
cat /etc/group
sudo Privileges

Learned how sudo provides administrator access securely.

Example:
sudo apt update
User Management

Created and managed a new user account.

Commands practiced:

sudo adduser devopsuser

su - devopsuser

exit

sudo deluser devopsuser
Automation Script

Created:

user-info.sh

The script displays:

current user
user ID
home directory
user groups

#Key Learning

Today I understood how Linux handles users, permissions, and access control — concepts that are extremely important in DevOps, cloud systems, SSH access, and server administration.