import argparse

parser = argparse.ArgumentParser(description='Create a script multi_parser.py that accepts a list of filenames and a flag for recursive processing.',
                                 epilog='End...!')

parser.add_argument()

arguments = parser.parse_args()
print(arguments)