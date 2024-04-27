def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Line 1: This is a text file.\n")
            file.write("Line 2: It contains a mix of strings and numbers.\n")
            file.write("Line 3: 12345\n")
        print("File 'my_file.txt' created successfully.")
    except PermissionError:
        print("Permission denied to create the file.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print("File creation process completed.")


def read_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line.strip())  # Remove trailing newline characters
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print("An error occurred:", str(e))


def append_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("Line 4: Appended line 1.\n")
            file.write("Line 5: Appended line 2.\n")
            file.write("Line 6: Appended line 3.\n")
        print("Content appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print("File appending process completed.")


# Task 1: Create a new text file
create_file()

# Task 2: Read and display the contents of the file
read_file()

# Task 3: Append additional content to the file
append_file()
