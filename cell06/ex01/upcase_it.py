import sys

def downcase_it(string):
    """Convert the given string to uppercase and return it."""
    return string.upper()

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        print(downcase_it(param))