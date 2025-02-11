# change_base.py

## Description

`change_base.py` is a Python script that allows users to convert numbers between different bases using a **dotted notation** representation. The script prompts the user for:

1. A **source base** (the original base of the number)
2. A **number in dotted notation** (e.g., `1.2.3` for base representation)
3. A **target base** (the base to convert the number into)

The script then converts the given number from the source base to the target base and prints the result.

---

## How It Works

The script performs the following steps:
- Parses the **dotted notation** number into an integer using the given source base.
- Converts the integer into the desired target base while maintaining the dotted notation format.
- Outputs the converted number in the new base.

---

## Installation & Usage

### Prerequisites
Ensure you have **Python 3** installed on your system.

### Running the Script
1. Open a terminal or command prompt.
2. Navigate to the directory containing `change_base.py`.
3. Run the script:
   ```sh
   python change_base.py
