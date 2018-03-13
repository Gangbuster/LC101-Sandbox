def get_initials(fullname):
    fullname = fullname.split()
    initials = ""
    for char in fullname:
        initials = initials + char[0]

    return initials.upper()


def main():
    get_fullname = input("What is your full name?")

    print(get_initials(get_fullname))


if __name__ == '__main__':
    main()