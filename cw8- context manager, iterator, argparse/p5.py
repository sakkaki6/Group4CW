import argparse

parser = argparse.ArgumentParser(description='Create a script basic_parser.py that accepts two command-line arguments',
                                 epilog='End...!')


parser.add_argument('--file_name', '-fn',required=True)
parser.add_argument('--verbose', '-v',action='store_true')

parser.add_argument('--text', '-t',default='''With the online text generator you can process your personal Lorem Ipsum enriching it with html elements that define its structure,
with the possibility to insert external links, but not only.
Now to compose a text Lorem Ipsum is much more fun!''')

parser.add_argument('--mode', '-m', choices=['r', 'w', 'a'], required=True,
                    help='Write your name between choices', type=str)

arguments = parser.parse_args()
print(arguments)

match arguments.mode:
    case 'w' | 'a':
        with open(arguments.file_name, arguments.mode) as w:
            if arguments.verbose:
                w.write(arguments.text)
    case 'r': 
        with open(arguments.file_name, arguments.mode) as r:
            if arguments.verbose:
                a = r.read()
                print(a)