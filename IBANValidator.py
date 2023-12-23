# IBAN Validator
import csv

print("Welcome to the IBAN Validator!")
print("This program checks if an entered International Bank Account Number (IBAN) is valid.")
print("Please follow these guidelines when entering an IBAN:")
print("1. Enter the IBAN as a continuous string without spaces or separators.")
print("2. Ensure the IBAN contains only alphanumeric characters (letters and numbers).")
print("3. The IBAN should start with a two-letter country code followed by numbers (and possibly more letters).")
print("For example: GB82WEST12345698765432")


# Load country code lengths from a CSV file
country_code_lengths = {}
with open('YOUR_PATH_HERE/Resources/country_length.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        country_code_lengths[row[0]] = row[1]

# Prompt for IBAN input
iban = input("Please enter the IBAN you want to validate: ").replace(' ', '')
country_code = iban[:2]

if len(iban) < 2:
    print("The entered IBAN is too short to determine the country code. Please enter a complete IBAN.")
else:
    country_code = iban[:2]
    if not iban.isalnum():
        print("The entered IBAN contains invalid characters. Please enter an IBAN using only letters and numbers.")
    elif country_code not in country_code_lengths:
        print(f"The entered IBAN's country code '{country_code}' is not recognized. Please enter a valid IBAN.")
    elif len(iban) < int(country_code_lengths.get(country_code, 0)):
        print(f"The entered IBAN is too short for the country code {country_code}. Please check and re-enter.")
    elif len(iban) > int(country_code_lengths.get(country_code, 0)):
        print(f"The entered IBAN is longer than expected for the country code {country_code}. Please check and re-enter.")
    else: 
        # Rearrange the IBAN: move the four initial characters to the end
        rearranged_iban = iban[4:] + iban[:4]

        # Convert all letters to numbers (A = 10, B = 11, ..., Z = 35)
        numeric_iban = ''
        for ch in rearranged_iban:
            if ch.isdigit():
                numeric_iban += ch
            else:
                numeric_iban += str(ord(ch) - 55)  # Convert letters to numbers

        # Perform the mod-97 operation
        if int(numeric_iban) % 97 == 1:
            print("The entered IBAN is valid. Thank you for using the IBAN Validator.")
        else:
            print("The entered IBAN is invalid. Please check for any errors and try again.")

