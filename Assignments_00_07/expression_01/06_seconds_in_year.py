
DAYS_PER_YEAR : int = 365
HOURS_PER_DAY : int = 24
MIN_PER_DAY : int = 60
SEC_PER_MIN : int = 60

def main():

    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_DAY * SEC_PER_MIN

    print(f"there are {total_seconds} seconds in a year")

if __name__ == "__main__":
    main()