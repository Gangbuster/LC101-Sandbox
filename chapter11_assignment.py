def sort_contacts(contacts):
    sorted_contacts = sorted(contacts.keys())
    final_contacts = []

    for i in sorted_contacts:
        final_contacts.append((i, contacts.get(i)[0], contacts.get(i)[1]))

    return final_contacts


def main():
    contacts = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}
    print(sort_contacts(contacts))


if __name__ == '__main__':
    main()