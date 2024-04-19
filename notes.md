## Platform CTF Writeup: Box

![Header](images/box-1.png)

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


# Walkthrough

### Summary

The <Platform> room is a virtual machine that simulates a scenario where a server is being used.

<Box> is a <Difficulty> machine that teaches <basic penetration testing concepts by guiding users through a series of challenges focused on a fictitious company's insecure web application>.

On this machine, users are tasked with exploiting vulnerabilities in a <Linux-based web server running outdated software versions, weak authentication mechanisms, and misconfigured access controls>.

The goal is to demonstrate how a hacker can leverage these vulnerabilities to gain unauthorized access and exfiltrate sensitive data (capture the flags). Throughout the room, various attack techniques are exploited.

---
## 1. Enumeration

### 1.1 Nmap:

We begin our reconnaissance by running an initial Nmap scan checking default scripts and testing for vulnerabilities. 

**Nmap scan results**:

```
```

### 1.2 Web Discovery:

Summary results.

SCREENSHOT HERE

WAPPALYZER HERE

As we currently <text>, we can conclude our initial enumeration and proceed with <attack-vector> for an initial foothold.


---
## 2 Initial Foothold - <exploit>


### 2.1 Vulnerability Explanation:


**Vulnerability Fix**:


**Severity**:


### 2.2 Steps to reproduce the attack:


**Proof of Concept Code**:
   (Modifications to the existing exploit are highlighted)

**User Flag**:

```
whoami && hostname && ip addr && cat user.txt 
```

SCREENSHOT

Now that we have an initial shell on this machine as user, we can further enumerate the machine and escalate our privileges.

---
## 3. Privilege Escalation - <exploit>

### 3.1 Vulnerability Explanation:


**Vulnerability Fix**:


**Severity**:


### 3.2 Steps to reproduce the attack:
   (Screenshot: whoami)

**Proof of Concept Code**:
   (Modifications to the existing exploit are highlighted)

**Root Flag**:

As you see we have successfully elevated our privileges to System and completing the task. Once again I used the command `dir "root.txt" /s` to search for the root flag.	

```
whoami && hostname && ip addr && cat user.txt 
```

SCREENSHOT

---
## 4. Post Exploitation

### 4.1 Maintaining Access:

Maintaining access to a system is important to us as attackers, ensuring that we can get back into a system after it has been exploited is invaluable.
The maintaining access phase of the penetration test focuses on ensuring that once the focused attack has occurred, we have administrative access over the system again.
Many exploits may only be exploitable once and we may never be able to get back into a system after we have already performed the exploit.

### 4.2 House Cleaning:

The house cleaning portions of the assessment ensures that remnants of the penetration test are removed.
Often fragments of tools or user accounts are left on an organization's computer which can cause security issues down the road.
Ensuring that we are meticulous and no remnants of our penetration test are left over is important.

After collecting trophies from the exam network was completed, I removed all created user accounts, passwords, as well as any binaries downloaded on the system.

---
## 5. Remediation 

It's important to note that remediating vulnerabilities requires an ongoing effort and it's important to keep the system up to date and review it regularly for new vulnerabilities. It's also important to give clear instructions and guidelines for the staff, and to establish a plan of action in case of a security breach.

### 5.1 Vulnerabilities found:

1. **Weak password policy**: The password policy is weak and does not meet the minimum requirements for strong passwords.
2. **Vuln**: explanation.

### 5.2 Recommendations:

https://tcm-sec.com/wp-content/uploads/2021/10/TCMS-Demo-Corp-Security-Assessment-Findings-Report.pdf

To obtain a CVSS score, we can review the CVE in a vulnerability database, or if there is no CVE assigned, we can use a [CVSS calculator](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)

The following tables illustrate the vulnerabilities found by impact and recommended remediations:

| Critical / C | High / H | Moderate / M | Low / L | Info / I |
|----------|------|----------|-----|-----|
| <p align="center">:red_circle: x1</p> | <p align="center">:orange_circle: x1</p> | <p align="center">:yellow_circle: x1</p> | <p align="center">:green_circle: x1</p> | <p align="center">:large_blue_circle: x1</p> |

| Finding | Severity | Recommendation |
|---------|----------|----------------|
| Finding | <p align="center">:red_circle: C</p> | Recommendation. |
| Finding | <p align="center">:orange_circle: H</p> | Recommendation. |
| Finding | <p align="center">:yellow_circle: M</p> | Recommendation. |
| Finding | <p align="center">:green_circle: L</p> | Recommendation. | 
| Finding | <p align="center">:large_blue_circle: I</p> | Recommendation. |


---
## 6. Conclusion 


---
## References
1. link
2. link
3. link
4. link
