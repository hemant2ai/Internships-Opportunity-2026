import pandas as pd
from datetime import datetime

FILE_NAME = "internships.csv"   # Make sure this matches your actual file name exactly

def update_expired_status():
    try:
        df = pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        print(f"Error: {FILE_NAME} not found.")
        return

    # Ensure deadline column exists
    if "deadline" not in df.columns:
        print("Error: 'deadline' column not found in CSV.")
        return

    if "status" not in df.columns:
        print("Error: 'status' column not found in CSV.")
        return

    today = datetime.today()

    # Convert deadline to datetime
    df["deadline"] = pd.to_datetime(df["deadline"], errors="coerce")

    # Track changes
    expired_count = 0

    for index, row in df.iterrows():
        deadline = row["deadline"]

        if pd.notnull(deadline):
            if deadline < today and row["status"] == "Active":
                df.at[index, "status"] = "Expired"
                expired_count += 1

    # Save updated file
    df.to_csv(FILE_NAME, index=False)

    print("\nUpdate Complete.")
    print(f"Expired internships marked: {expired_count}")
    print(f"File updated: {FILE_NAME}")

if __name__ == "__main__":
    update_expired_status()

