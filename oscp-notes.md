System Information:
Web-Technology:
Hostname: 

IP: 

USERS/CREDENTIALS:


=========================================================================

To-Try LIST:

*
*
*

=========================================================================

**TIP: Make screenshots and dump them here, saving time while backtracking findings and writing the report. Time management and maintaining your workflow is key.**

Screenshot dump:


=========================================================================

NMAP RESULTS:


=========================================================================

Web Services Enumeration:


=========================================================================

OTHER / PRIVILEGE-ESCALATION:

# Enumeration


# Initial Foothold - <exploit>
- Vulnerability Explanation:


- Vulnerability Fix:


- Severity:


- Steps to reproduce the attack:
   (Screenshot: whoami)

- Proof of Concept Code:
   (Modifications to the existing exploit are highlighted)
	

# Privilege Escalation - <exploit>
- Vulnerability Explanation:


- Vulnerability Fix:


- Severity:


- Steps to reproduce the attack:
   (Screenshot: id > whoami)

- Proof of Concept Code:
Original:


Modifications to the existing exploit:
	

# Post Exploitation
- Maintaining Access:
   (Screenshot: )

- House Cleaning:


=========================================================================

# Flags
Each local.txt and proof.txt found must be shown in a screenshot that includes:
- interactive shell
- Full path + contents of the file
- id / whoami
- hostname
- ip a, ipconfig, ifconfig or ip addr

# Local.txt


# Proof.txt


=========================================================================

Submission Checklist:
* [ ] Initial Access Screenshot 
* [ ] Privesc Screenshot 
* [ ] Local Screenshot
* [ ] Proof Screenshot
* [ ] Proof exploit modifications
