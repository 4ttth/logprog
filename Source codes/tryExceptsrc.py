jpy = 0.50
usd = 52.00
aed = 14.50
try:
    php = float(input("Enter a value in Philippine Peso: ₱"))

except ValueError:
    print("Your entered value must be a numerical value.")

else:
    try:
        print("Conversion choices: ")
        print("Press:   A for Japanese Yen")
        print("         B for US Dollar")
        print("         C for UAE Dirham")
        conversion_choice = str(input("Enter your choice: ")).upper()


    except ValueError:
        print("Kindly input either A, B, or C.")

    else:
        if conversion_choice == 'A':
            converted = php * jpy
            print(f'₱{php:.2f} Philippine peso is equal to ¥{jpy:.2f} Japanese Yen.')

        elif conversion_choice == 'B':
            converted = php * usd
            print(f'₱{php:.2f} Philippine peso is equal to ${usd:.2f} US Dollars.')

        elif conversion_choice == 'C':
            converted = php * aed
            print(f'₱{php:.2f} Philippine peso is equal to AED {aed:.2f} UAE Dirhams.')

        else:
            print("Please input only: [A], [B], or [C].")
finally:
    print("\n Thank you for using this conversion!")