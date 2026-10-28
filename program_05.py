
import os
import sys

# Display current directory
print("Current Directory:", os.getcwd())

# List files and folders
print("\nFiles and Folders:")
print(os.listdir())

# Create a new folder
folder = "MyWorkspace"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("\nWorkspace folder created successfully.")
else:
    print("\nWorkspace folder already exists.")

# Navigate to the new folder
os.chdir(folder)
print("Current Directory After Navigation:", os.getcwd())

# Create and read a text file using command-line argument
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "log.txt"

# Write data into the file
with open(filename, "w") as file:
    file.write("Welcome to File Management Utility!")

print("\nFile created successfully.")

# Read the file
with open(filename, "r") as file:
    print("File Content:", file.read())

# List text files
print("\nText Files in Current Directory:")
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)
