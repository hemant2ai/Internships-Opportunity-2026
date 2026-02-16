import pandas as pd


def load_data():
    return pd.read_csv("internships.csv")


def filter_data(df, country=None, industry=None, category=None, keyword=None):
    if country:
        df = df[df["country"].str.contains(country, case=False, na=False)]

    if industry:
        df = df[df["industry"].str.contains(industry, case=False, na=False)]

    if category:
        df = df[df["category"].str.contains(category, case=False, na=False)]

    if keyword:
        df = df[df["role"].str.contains(keyword, case=False, na=False)]

    return df


def main():
    print("\n=== Internship Opportunities 2026 ===\n")

    df = load_data()

    country = input("Filter by Country (or press Enter to skip): ")
    industry = input("Filter by Industry (or press Enter to skip): ")
    category = input("Filter by Category (or press Enter to skip): ")
    keyword = input("Search by Role Keyword (or press Enter to skip): ")

    result = filter_data(df, country, industry, category, keyword)

    if result.empty:
        print("\nNo matching internships found.\n")
    else:
        print("\nMatching Opportunities:\n")
        print(result[["organization", "role", "location", "deadline"]].to_string(index=False))


if __name__ == "__main__":
    main()
