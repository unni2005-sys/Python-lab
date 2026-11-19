filename = input("Enter a file name: ")
parts = filename.rsplit(".", 1)
if len(parts) > 1:
    extension = parts[1].strip()
    print("Extension:", extension)
else:
    print("Extension: None found")
