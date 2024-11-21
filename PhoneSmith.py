"""
Phonesmith: The ultimate tool for crafting phone numbers in various formats.
Author: PiHiker
GitHub: https://github.com/PiHiker/PhoneSmith
"""

import argparse


def generate_phone_numbers(area_code, output_file):
    """
    Generate all possible phone numbers for the given area code
    and save them to the specified output file in multiple formats.
    """
    with open(output_file, "w") as file:
        for i in range(10000000):  # Generate numbers from 0000000 to 9999999
            num = f"{str(i).zfill(7)}"
            # Basic formats
            file.write(f"{area_code}{num}\n")            # Example: 721xxxxxxx
            file.write(f"1+{area_code}{num}\n")          # Example: 1+721xxxxxxx
            file.write(f"1{area_code}{num}\n")           # Example: 1721xxxxxxx

            # Dashed formats
            file.write(f"{area_code}-{num[:3]}-{num[3:]}\n")   # Example: 721-xxx-xxxx
            file.write(f"1-{area_code}-{num[:3]}-{num[3:]}\n") # Example: 1-721-xxx-xxxx
            file.write(f"1+{area_code}-{num[:3]}-{num[3:]}\n") # Example: 1+721-xxx-xxxx

            # Parentheses formats
            file.write(f"({area_code}) {num[:3]}-{num[3:]}\n")       # Example: (721) xxx-xxxx
            file.write(f"1 ({area_code}) {num[:3]}-{num[3:]}\n")     # Example: 1 (721) xxx-xxxx

            # International formats
            file.write(f"+1 {area_code} {num[:3]} {num[3:]}\n")      # Example: +1 721 xxx xxxx

            # Local format (7-digit dialing)
            file.write(f"{num}\n")                                   # Example: xxxxxxx


def main():
    """
    Parse command-line arguments and initiate the phone number generation process.
    If no area code is provided via the CLI, prompt the user for it.
    Dynamically set the default output file based on the area code.
    """
    parser = argparse.ArgumentParser(
        description="Phonesmith: Generate formatted phone number wordlists.",
        usage="python3 PhoneSmith.py [area_code] [--output OUTPUT]",
        epilog="If no area code is provided, you will be prompted to enter it."
    )

    parser.add_argument(
        "area_code",
        type=str,
        nargs="?",  # Makes this argument optional
        help="The 3-digit area code for the phone numbers (e.g., 721)."
    )
    parser.add_argument(
        "--output",
        type=str,
        help="The output file to save the wordlist. Defaults to '<area_code>-wordlist.txt'."
    )
    args = parser.parse_args()

    # Prompt for the area code if not provided
    area_code = args.area_code
    if not area_code:
        area_code = input("Please enter a 3-digit area code: ").strip()

    # Validate the area code
    if not area_code.isdigit() or len(area_code) != 3:
        print("Error: Area code must be a 3-digit number.")
        return

    # Set the default output file if not provided
    output_file = args.output if args.output else f"{area_code}-wordlist.txt"

    print(f"Phonesmith is crafting phone numbers for area code {area_code}...")
    generate_phone_numbers(area_code, output_file)
    print(f"Wordlist saved to {output_file}")


if __name__ == "__main__":
    main()
