import csv
from datetime import datetime

INPUT_FILE = "internships.csv"
OUTPUT_FILE = "internships_updated.csv"

today = datetime.today().date()

with open(INPUT_FILE, newline='', encoding="utf-8") as infile, \
     open(OUTPUT_FILE, 'w', newline='', encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        deadline = row["Deadline"]

        if deadline and deadline != "Rolling" and deadline != "TBD":
            try:
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
                if deadline_date < today:
                    row["Status"] = "Expired"
                else:
                    row["Status"] = "Active"
            except:
                row["Status"] = "Unknown"

        writer.writerow(row)

print("Internships updated successfully.")
