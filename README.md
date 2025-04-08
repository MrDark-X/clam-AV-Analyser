# 🛡️ ClamAV Log Analyzer

A Python-based tool that parses ClamAV antivirus scan logs, extracts infected file information, and generates a structured Excel report for further analysis and record-keeping.

---

## 📌 Overview

ClamAV Log Analyzer is a lightweight and efficient script designed to analyze ClamAV log files. It automatically extracts details about infected files and compiles them into a clean and organized Excel report.

This tool is useful for system administrators, SOC analysts, and cybersecurity professionals who regularly use ClamAV for malware scanning and want to automate reporting or integrate scan results into further analysis workflows.

---

## 🔧 Features

- ✅ Parses ClamAV antivirus scan logs.
- 📋 Extracts infected file paths and status.
- 📊 Generates Excel (`.xlsx`) reports using `openpyxl`.
- 🧠 Simple logic and modular design.
- 🐍 Written in Python – no external dependencies apart from `openpyxl`.

---

## 📂 How the Tool Works

### ✅ Workflow

1. **Input**: User provides the path to a ClamAV log file.
2. **Validation**: Script checks if the file exists.
3. **Log Parsing**:
    - Extracts the number of infected files using regex.
    - Parses all lines containing `FOUND` to retrieve file path and infection type.
4. **Reporting**:
    - Displays the infected files on the terminal.
    - Saves the report into an Excel file with the same name as the log file.

---

## 🚀 Usage

### 🔁 Prerequisites

- Python 3.x
- `openpyxl` module

Install `openpyxl` using pip:
```bash
pip install openpyxl
```
---
### 📌 Run the Tool
```python
python clamanalyzer.py
```
You will be prompted to enter the path to your ClamAV scan log:
``` cmd
Enter the path to the ClamAV log file: /path/to/clamav.log
```
### 🌟 Pros
- ✅ Automation: Reduces manual effort in analyzing logs.
- 📈 Professional Reports: Converts raw logs into structured reports.
- 🧩 Modular: Easy to integrate into existing security workflows.
- ⚡ Lightweight: No bloated dependencies.
- 🧪 Extendable: You can easily add more features such as:
-- Parsing clean files
-- Emailing reports
-- Adding timestamp columns
