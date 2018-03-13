def is_leap(year):
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year != 1900 and year !=1800:
        return True
    else:
        return False

def main():
    n = int(input("Enter a year:"))
    leap = is_leap(n)
    print("Is the year", n,"a leap year?", leap)

if __name__ == "__main__":
    main()
