"""
PhoneSmith: The ultimate tool for crafting phone numbers in various formats.
Author: PiHiker
GitHub: https://github.com/PiHiker/PhoneSmith
"""

import argparse
from pathlib import Path

LINES_PER_NUMBER = 10
WRITE_BUFFER_SIZE = 1000


def validate_area_code(value):
    if not value.isdigit() or len(value) != 3:
        raise ValueError("Area code must be a 3-digit number.")
    return value


def resolve_output_path(area_code, output_file):
    filename = output_file or f"{area_code}-wordlist.txt"
    path = Path(filename)
    if path.exists() and path.is_dir():
        raise ValueError("Output path must be a file, not a directory.")
    if path.parent != Path("."):
        path.parent.mkdir(parents=True, exist_ok=True)
    return path


def format_numbers(area_code, num):
    return [
        f"{area_code}{num}",
        f"1+{area_code}{num}",
        f"1{area_code}{num}",
        f"{area_code}-{num[:3]}-{num[3:]}",
        f"1-{area_code}-{num[:3]}-{num[3:]}",
        f"1+{area_code}-{num[:3]}-{num[3:]}",
        f"({area_code}) {num[:3]}-{num[3:]}",
        f"1 ({area_code}) {num[:3]}-{num[3:]}",
        f"+1 {area_code} {num[:3]} {num[3:]}",
        f"{num}",
    ]


def generate_phone_numbers(area_code, output_path, limit):
    """
    Generate all possible phone numbers for the given area code
    and save them to the specified output file in multiple formats.
    """
    buffer = []
    with output_path.open("w", encoding="utf-8") as file:
        for i in range(limit):  # Generate numbers from 0000000 to limit
            num = f"{i:07d}"
            buffer.extend(format_numbers(area_code, num))
            if len(buffer) >= WRITE_BUFFER_SIZE * LINES_PER_NUMBER:
                file.write("\n".join(buffer) + "\n")
                buffer.clear()
        if buffer:
            file.write("\n".join(buffer) + "\n")


def main():
    """
    Parse command-line arguments and initiate the phone number generation process.
    If no area code is provided via the CLI, prompt the user for it.
    Dynamically set the default output file based on the area code.
    """
    parser = argparse.ArgumentParser(
        description="PhoneSmith: Generate formatted phone number wordlists.",
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
    parser.add_argument(
        "--limit",
        type=int,
        default=10000000,
        help="Limit how many 7-digit numbers to generate (default: 10000000)."
    )
    args = parser.parse_args()

    # Prompt for the area code if not provided
    area_code = args.area_code
    if not area_code:
        area_code = input("Please enter a 3-digit area code: ").strip()

    try:
        area_code = validate_area_code(area_code)
        if args.limit <= 0:
            raise ValueError("Limit must be a positive integer.")
        output_path = resolve_output_path(area_code, args.output)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print(f"PhoneSmith is crafting phone numbers for area code {area_code}...")
    generate_phone_numbers(area_code, output_path, args.limit)
    print(f"Wordlist saved to {output_path}")


if __name__ == "__main__":
    main()
