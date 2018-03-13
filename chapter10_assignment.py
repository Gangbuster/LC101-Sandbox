def get_country_codes(prices):
    code_mod = list(prices)
    bad_code = ['$', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_code = []
    for i in code_mod:
        if i not in bad_code:
            new_code.append(i)
    return "".join(new_code)

def main():
    orig_code = "NZ$300, KR$1200, DK$5"
    print(get_country_codes(orig_code))

if __name__ == '__main__':
    main()