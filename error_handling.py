def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

try:
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    # Open and read the content
    with open(input_filename, "r") as infile:
        content = infile.read()

    # Modify the content
    modified_content = modify_content(content)

    # Write to a new file
    output_filename = "modified_" + input_filename
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"Modified content written to '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except IOError:
    print(f"Error: Unable to read or write the file.")
