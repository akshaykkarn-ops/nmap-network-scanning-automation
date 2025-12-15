import nmap
from datetime import datetime

# Initialize scanner
scanner = nmap.PortScanner()

# Get target from user
target = input("Enter target IP or hostname: ")

# Perform SYN scan
scanner.scan(hosts=target, arguments='-sS')

# Create report file
report_file = "scan_report.txt"

with open(report_file, "w") as report:
    report.write("Nmap Scan Report\n")
    report.write(f"Scan Time: {datetime.now()}\n")
    report.write(f"Target: {target}\n\n")
    report.write("Open Ports and Services:\n")
    report.write("---------------------------------\n")

    for host in scanner.all_hosts():
        report.write(f"Host: {host}\n")
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]['name']
                version = scanner[host][proto][port].get('version', 'N/A')
                report.write(f"Port {port}/{proto} - {service} {version}\n")

    report.write("\nScan completed successfully.\n")

print("Scan completed. Report saved as scan_report.txt")
