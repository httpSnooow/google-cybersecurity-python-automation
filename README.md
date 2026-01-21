# Python Automation: Access Control List Update Algorithm

> **Project Context:** Google Cybersecurity Professional Certificate

<div align="center">

  ![Google](https://img.shields.io/badge/Google-Cybersecurity-4285F4?style=for-the-badge&logo=google&logoColor=white)
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Security Automation](https://img.shields.io/badge/Security-Automation-2E8B57?style=for-the-badge&logo=automationanywhere&logoColor=white)
  ![Access Control](https://img.shields.io/badge/Access-Control-00BFFF?style=for-the-badge&logo=securityscorecard&logoColor=white)

</div>

---

## Project Overview

**Scenario:** In a healthcare organization, access to restricted patient data is managed through an IP address "allow list." As employees cycle through roles or leave the organization, this list must be updated to maintain security. 

This project documents the development of a **Python-based automation algorithm** designed to cross-reference the active `allow_list.txt` against a `remove_list`. The algorithm identifies unauthorized IP addresses and removes them from the system, ensuring that the **Principle of Least Privilege** is consistently applied without manual error.

---

## Technical Implementation: The Algorithm

The script utilizes fundamental Python programming concepts to handle file I/O operations and data manipulation.

### 1. File Handling & Data Ingestion
The algorithm opens the restricted access file using a `with` statement to ensure secure resource management.
* **Opening Files:** Used the `open()` function with the `"r"` argument for reading.
* **String Conversion:** Applied the `.read()` method to convert the file content into a readable string format.
* **Data Structuring:** Utilized the `.split()` method to transform the string into a list of individual IP addresses, making them easier to manipulate.

### 2. The Logic Engine (Iteration & Removal)
To clean the list, the algorithm iterates through a predefined list of addresses marked for removal.
* **Iterative Loops:** Implemented a `for` loop to cycle through every element in the `remove_list`.
* **Conditional Logic:** Built an `if` statement to verify if a restricted IP exists within the current allow list before attempting removal.
* **Dynamic Updating:** Employed the `.remove()` method to strike unauthorized addresses from the list in real-time.

### 3. File Finalization
Once the list is updated, the algorithm must write the changes back to the permanent storage.
* **String Reconstruction:** Used the `.join()` method (with `"\n"` as a separator) to convert the list back into a structured string format.
* **Overwriting:** Opened the file in `"w"` (write) mode to replace the old content with the secured, updated list.

---

## Python Toolkit & Methods Applied

| Method/Function | Security Application |
| :--- | :--- |
| **`with open()`** | Manages file resources safely, preventing data corruption or leaks during I/O operations. |
| **`.split()`** | Breaks down large datasets (IP strings) into manageable chunks for granular analysis. |
| **`for...in`** | Automates the repetitive task of checking hundreds of access logs or permission entries. |
| **`.remove()`** | Precisely executes access revocation without affecting the rest of the authorized dataset. |
| **`.join()`** | Re-formats data for storage after security processing is complete. |

---

## Key Takeaways

* **Automation for Compliance:** Manual updates to access lists are prone to human error; Python automation ensures that revocation happens consistently and accurately.
* **Scalability in SOC:** This script serves as a foundation for more complex security automation, such as blocking IPs identified by an IDS or SIEM in real-time.
* **Least Privilege Enforcement:** Regularly running this algorithm hardens the network perimeter by ensuring only currently authorized devices can access sensitive patient records.

---

<div align="center">
  <sub><i>Disclaimer: This is a fictional case study completed for educational purposes as part of the Google Cybersecurity Certificate.</i></sub>
</div>
