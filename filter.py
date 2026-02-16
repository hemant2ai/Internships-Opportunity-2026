import pandas as pd
import argparse
from datetime import datetime

def load_data():
    df = pd.read_csv("internships.csv")
    return df

def filter_data(df, keyword=None, country=None, category=None, show_expired=False):
    if not show_expired:
        df = df[df["status"] == "Active"]

    if keyword:
        df = df[df.apply(lambda row: keyword.lower() in str(row).lower(), axis=1)]

    if country:
        df = df[df["country"].str.lower() == country.lower()]

    if category:
        df = df[df["category"].str.lower() == category.lower()]

    return df

def sort_by_deadline(df):
    df["deadline"] = pd.to_datetime(df["deadline"], errors="coerce")
    return df.sort_values(by="deadline")

def main():
    parser = argparse.ArgumentParser(description="Filter Internship Listings")

    parser.ad
