import argparse

parser = argparse.ArgumentParser(
                    prog='HexToASCII',
                    description='This tool is used to transform string format vulnerability result into humain readable character')

parser.add_argument('-x', '--hex',action="store_true",help="Print result as hex value not the ASCII value", required=False)      # option that takes a value
parser.add_argument('-d', '--delimiter',help="Choose a specific delimiter for printing result",required=False)      # option that takes a value
subparsers = parser.add_subparsers()
parser.add_argument('-if', '--input-file',help="Choose a specific  input file",required=True)      # option that takes a value
args = parser.parse_args()
print(args)

if(args.input_file != None):
    try:
        with open(args.input_file,"r") as f:
            string_result = f.read()
    except:
        print("Error when opening the file")

string_result = string_result.split('-')

if args.hex:
    for i in string_result:
        for k in reversed(range(0,len(i),2)):
            if(i[k:k+2] != '\n'):
                if(args.delimiter):
                    print(i[k:k+2],end=args.delimiter)
                else:
                    print(i[k:k+2],end=' ')
else :
    for i in string_result:
        for k in reversed(range(0,len(i),2)):
            if(i[k:k+2] != '\n'):
                if(args.delimiter):
                    print(chr(int('0x'+i[k:k+2],16)),end=args.delimiter)
                else:
                    print(chr(int('0x'+i[k:k+2],16)),end=' ')

    
