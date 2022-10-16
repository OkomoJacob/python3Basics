from pathlib import Path

# Absolute path: Start from the root of our harddisk e.g from C:\Programs\MyCodes\.. or /usr/local/bin
# Relative path: Start from the pwd e.g from ecommerce
# Create a path oject from Path class to reference a directory from our computer

path = Path("../junk")
'''
To create a directory called emails:

emails = Path("emails")
emails.mkdir()

To remove a directory called emails:
emails = Path("emails")
emails.rmdir()
'''

print(path.exists())
