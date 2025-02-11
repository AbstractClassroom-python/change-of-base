def base_convert(number_str, source_base, target_base):
    """
    Convert a number from source_base to target_base.
    :param number_str: Number in dotted notation (e.g., "1.2.3")
    :param source_base: The base of the input number
    :param target_base: The base to convert to
    :return: The converted number in dotted notation
    """
    # Convert dotted notation to an integer
    number_parts = number_str.split(".")
    decimal_value = sum(int(part) * (source_base ** i) for i, part in enumerate(reversed(number_parts)))
    
    # Convert integer to the target base in dotted notation
    converted_parts = []
    while decimal_value:
        converted_parts.append(str(decimal_value % target_base))
        decimal_value //= target_base
    
    return ".".join(reversed(converted_parts)) if converted_parts else "0"


def main():
    # Get user input
    source_base = int(input("Enter the source base: "))
    number_str = input(f"Enter the number in base {source_base} (dotted notation, e.g., 1.2.3): ")
    target_base = int(input("Enter the target base: "))
    
    # Convert and display result
    result = base_convert(number_str, source_base, target_base)
    print(f"The number {number_str} in base {source_base} is {result} in base {target_base}.")


if __name__ == "__main__":
    main()
