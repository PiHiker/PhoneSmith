PhoneSmith
==========

PhoneSmith is a Python tool for generating and formatting phone numbers in multiple styles. Whether you're working on dialing, data analysis, or penetration testing, PhoneSmith crafts comprehensive wordlists of phone numbers for a specified area code.

Features
--------
- Generate phone numbers in a variety of formats:
  - Plain formats: 721xxxxxxx, 1+721xxxxxxx
  - Dashed formats: 721-xxx-xxxx, 1-721-xxx-xxxx
  - Parentheses formats: (721) xxx-xxxx, 1 (721) xxx-xxxx
  - International formats: +1 721 xxx xxxx
  - Shortened local formats: xxxxxxx (local dialing)
- Supports dynamic area code input for flexibility.
- Memory-efficient: Writes generated phone numbers directly to a file without overwhelming system resources.

Installation
------------
Clone the repository to your local machine:
git clone https://github.com/PiHiker/PhoneSmith.git
cd PhoneSmith

Usage
-----
Run PhoneSmith using the command line:
python phonesmith.py <area_code> [--output <output_file>]

Replace <area_code> with the desired 3-digit area code. The --output argument is optional; if not provided, the default output file is phone_number_wordlist.txt.

Examples
--------
1. Generate phone numbers for area code 721 and save to the default file:
   python phonesmith.py 721

2. Generate phone numbers for area code 123 and save to my_wordlist.txt:
   python phonesmith.py 123 --output my_wordlist.txt

Output
------
The generated file will contain all possible phone numbers in the specified formats, for example:
7210000000
1+7210000000
1-721-000-0000
(721) 000-0000
+1 721 000 0000
...

Contributing
------------
Contributions are welcome! Feel free to fork the project and create a pull request.

License
-------
PhoneSmith is licensed under the Apache License, Version 2.0. See the LICENSE file for details.
