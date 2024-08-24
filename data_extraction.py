import os

# Get the current working directory
current_directory = os.getcwd()

# Initialize a dictionary to store file information
file_info = {}

# List all files in the current working directory
for entry in os.listdir(current_directory):
    # Get the full path of the entry
    full_path = os.path.join(current_directory, entry)
    
    # Check if it's a file
    if os.path.isfile(full_path):
        # Get file size in bytes
        file_size = os.path.getsize(full_path)
        # Store the information in the dictionary
        file_info[entry] = {
            "path": full_path,
            "size": file_size
        }
# Print the dictionary containing file names with their paths and sizes
for info in file_info.values():
    print({f"path: {info['path']}, size: {info['size']} bytes"})
   
    




