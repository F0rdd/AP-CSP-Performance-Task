import time

class RomanNumeralConversion:
    def __init__(self):
        # Initialize Roman numeral mappings and values for conversion
        self.romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        self.roman_values = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50),
                             ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

    def is_roman(self, s: str) -> bool:
        # Check if a string is a valid Roman numeral
        for char in s:
            if char in self.romans:
                continue
            else:
                return False
        return True

    def roman_to_int(self, l: list) -> list:
        # Convert a list of Roman numerals to integers
        output_list = []
        for s in l:
            output = 0
            skip_index = None
            for i, char in enumerate(s):
                try:
                    if i != skip_index:
                        if self.romans[s[i + 1]] > self.romans[char]:
                            # Handle cases where a smaller numeral precedes a larger numeral
                            value = self.romans[s[i + 1]] - self.romans[char]
                            skip_index = i + 1
                        else:
                            value = self.romans[char]
                        output += value
                except IndexError:
                    output += self.romans[char]
            output_list.append(output)
        return output_list

    def int_to_roman(self, l: list) -> list:
        # Convert a list of integers to Roman numerals
        output_list = []
        for num in l:
            if num > 3999:
                output_list.append(f"{TextColors.RED}[!]{TextColors.STANDARD} Larger than 3999.")
                continue
            result = []
            for roman, value in self.roman_values:
                while num >= value:
                    result.append(roman)
                    num -= value
            output_list.append("".join(result))
        return output_list


class TextColors:
    # Define text colors for console output
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    YELLOW = '\033[93m'
    STANDARD = '\033[0m'


# Create an instance of RomanNumeralConversion
RNC = RomanNumeralConversion()


def check_roman():
    # Function to check if a string is a valid Roman numeral
    user_string = input(
        f"\n{TextColors.BLUE}(1){TextColors.STANDARD} Enter the string you would like to check below:\n\n")
    is_roman = RNC.is_roman(user_string)

    if is_roman:
        print(f"\n{TextColors.BLUE}(1){TextColors.STANDARD} The string '{user_string}' is a Roman Numeral!")
        time.sleep(0.5)
    else:
        print(f"\n{TextColors.BLUE}(1){TextColors.STANDARD} The string '{user_string}' is not a Roman Numeral!")
        time.sleep(0.5)


def convert_roman_list():
    # Function to convert a list of Roman numerals to integers
    roman_list = []

    try:
        num = int(input(
            f"\n{TextColors.YELLOW}(2){TextColors.STANDARD} How many Roman Numerals would you like to convert?\n\n"))

        for i in range(num):
            user_roman = input(f"\n{TextColors.YELLOW}(2){TextColors.STANDARD} Enter Roman Numeral #{i + 1}:\n\n")
            roman_list.append(user_roman)

        try:
            output = RNC.roman_to_int(roman_list)
            print("\n")

            for i, roman in enumerate(output):
                print(f"{TextColors.YELLOW}(2){TextColors.STANDARD} '{roman_list[i]}': {roman}")

        except KeyError:
            print(
                f"\n{TextColors.RED}[!]{TextColors.STANDARD} One or more of the values entered is not a Roman Numeral!")
            time.sleep(0.5)

    except ValueError:
        print(f"\n{TextColors.RED}[!]{TextColors.STANDARD} The value you have entered is not an integer.")
        time.sleep(0.5)

    time.sleep(0.5)


def convert_int_list():
    # Function to convert a list of integers to Roman numerals
    int_list = []
    time.sleep(0.5)

    print(f"\n{TextColors.GREEN}[✓]{TextColors.STANDARD} Only enter integers less than 3999!")

    try:
        num = int(input(
            f"\n{TextColors.MAGENTA}(3){TextColors.STANDARD} How many integers would you like to convert?\n\n"))

        for i in range(num):
            user_int = int(input(f"\n{TextColors.MAGENTA}(3){TextColors.STANDARD} Enter integer #{i + 1}:\n\n"))
            int_list.append(user_int)

        output = RNC.int_to_roman(int_list)
        print("\n")

        for i, roman in enumerate(output):
            print(f"{TextColors.MAGENTA}(3){TextColors.STANDARD} '{int_list[i]}': {roman}")

    except ValueError:
        print(f"\n{TextColors.RED}[!]{TextColors.STANDARD} The value you have entered is not an integer.")

    time.sleep(0.5)


def main():
    # Main function to provide user options and execute corresponding functions
    print(f"Welcome to the Roman Numeral Conversion Script.")

    while True:
        try:
            user_choice = int(input(
                f"\nWould you like to:\n{TextColors.BLUE}(1){TextColors.STANDARD} Check if a string is a Roman Numeral\n{TextColors.YELLOW}(2){TextColors.STANDARD} Convert a list of Roman Numeral strings to integers\n{TextColors.MAGENTA}(3){TextColors.STANDARD} Convert a list of integers to Roman Numerals\n{TextColors.RED}(-1){TextColors.STANDARD} Exit\n\n"))
        except ValueError:
            print(f"\n{TextColors.RED}[!]{TextColors.STANDARD} The value you have entered is not an integer.")
            time.sleep(0.5)
            continue

        if user_choice == 1:
            time.sleep(0.5)
            check_roman()

        elif user_choice == 2:
            time.sleep(0.5)
            convert_roman_list()

        elif user_choice == 3:
            time.sleep(0.5)
            convert_int_list()

        elif user_choice == -1:
            time.sleep(0.5)
            print(f"\n{TextColors.GREEN}[✓]{TextColors.STANDARD} Exiting the loop...")
            time.sleep(0.5)
            break

        else:
            print(f"\n{TextColors.RED}[!]{TextColors.STANDARD} The entered choice is not an option.")


if __name__ == "__main__":
    main()
