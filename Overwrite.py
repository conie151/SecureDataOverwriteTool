import os
import random

def overwrite_with_random(file_path):
    with open(file_path, 'wb') as file:
        # Generate random binary data (0s and 1s)
        data = bytearray(os.path.getsize(file_path))
        random.seed()
        random.choice([0, 255])  # Warm up the random generator
        for i in range(len(data)):
            data[i] = random.choice([0, 255])

        # Overwrite the file with random data
        file.write(data)

def secure_delete(trash_bin_path):
    if not os.path.exists(trash_bin_path):
        print("Trash bin not found.")
        return

    for root, dirs, files in os.walk(trash_bin_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Overwrite the file with random data
            overwrite_with_random(file_path)
            
            # Delete the file
            os.remove(file_path)
            print(f"Securely deleted: {file_path}")

if __name__ == "__main__":
    trash_bin_path = os.path.expanduser("~\Recycle.Bin")  # Default trash bin path

    # You can customize the trash bin path if needed
    # trash_bin_path = "C:\\path\\to\\your\\trash\\bin"

    secure_delete(trash_bin_path)
