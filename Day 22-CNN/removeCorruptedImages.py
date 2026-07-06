from PIL import Image
import os

dataset_folder = "dataset/train"

deleted = 0

print("Checking images...\n")

for root, dirs, files in os.walk(dataset_folder):

    for file in files:

        path = os.path.join(root, file)

        try:
            # Open image
            img = Image.open(path)

            # Verify image
            img.verify()

        except Exception as e:

            print(f"Deleting: {path}")

            print("Reason:", e)

            os.remove(path)

            deleted += 1

print("\n--------------------------------")

print("Total Corrupted Images Deleted:", deleted)

print("--------------------------------")