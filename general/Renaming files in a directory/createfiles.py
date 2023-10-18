import os
import string
import random

def create_files(directory, num_files, string_length):
    # Create the directory if it doesn't already exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Loop through and create the files
    for _ in range(num_files):
        # Generate a random string of letters and digits
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=string_length))

        # Add the .txt extension to the file name
        file_name += ".txt"

        # Create the file in the directory if it's a directory
        if os.path.isdir(directory):
            with open(os.path.join(directory, file_name), "w") as f:
                f.write("This is a test file.")

# Define the number of files to create
num_files = 10

# Define the length of the random string to generate
string_length = 8

# Define the directories where the files will be created
# directory1 = "./helloworld/"
# directory2 = "./images/"

# Create the files in the first directory
# create_files(directory1, num_files, string_length)

# Create the files in the second directory
# create_files(directory2, num_files, string_length)

# Define the parent directory
parent_directory = "./"

# Loop through all the directories in the parent directory
for directory in os.listdir(parent_directory):
    # Create the files in the directory
    create_files(os.path.join(parent_directory, directory), num_files, string_length)
