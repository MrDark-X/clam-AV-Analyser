import re
import os
import openpyxl

def analyze_log(log_file):
    if not os.path.isfile(log_file):
        print("Invalid path or file does not exist.")
        return

    # Open the log file
    with open(log_file, 'r') as file:
        log_data = file.read()

    # Extract the infected file paths from the log
    pattern = r'Infected files: (\d+)'
    match = re.search(pattern, log_data)
    if match:
        num_infected_files = int(match.group(1))
        print(f"Number of infected files: {num_infected_files}")
    else:
        print("No infected files found.")
        return

    # Extract the list of infected files
    pattern = r'(?m)^(.+):(.+ FOUND)$'
    matches = re.findall(pattern, log_data)
    if matches:
        infected_files = [(file.strip(), status.strip()) for file, status in matches]
        print("Infected files:")
        for file, status in infected_files:
            print(f"- {file} ({status})")
    else:
        print("No infected files found.")
        return

    # Create a new Excel workbook and add data to it
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "ClamAV Scan Report"
    sheet["A1"] = "Infected File"
    sheet["B1"] = "Status"
    for row, (file, status) in enumerate(infected_files, start=2):
        sheet[f"A{row}"] = file
        sheet[f"B{row}"] = status

    # Save the workbook
    excel_file = os.path.splitext(log_file)[0] + ".xlsx"
    wb.save(excel_file)
    print(f"Scan report saved to {excel_file}")

    # Perform additional analysis as per your requirements
    # You can add more patterns and extract relevant information from the log

# Take the path to the ClamAV log file as user input
log_file_path = input("Enter the path to the ClamAV log file: ")

# Call the log analyzer function
analyze_log(log_file_path)
