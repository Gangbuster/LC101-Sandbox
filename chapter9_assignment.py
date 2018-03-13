def analyze_text(text):
    letter_count = 0
    num_e = 0
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_only = ""
    for c in text:
        if c in alpha:
            alpha_only = alpha_only + c
    for c in alpha_only:
        letter_count = letter_count + 1
        if c == "e" or c == "E" in text:
            num_e = num_e + 1
    percent = (num_e / letter_count) * 100
    return "The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(letter_count, num_e, percent)

def main():
    text1 = "Blueberries are tasteee!"
    print(analyze_text(text1))

if __name__ == "__main__":
    main()