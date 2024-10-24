# HexToASCII

This is a Python script that transforms string format vulnerability results into human-readable characters. It takes a hexadecimal string as input, either from a file or directly as an argument, and outputs the corresponding ASCII characters. This tool is not robust and is used for fast debugging

## Usage

```
python hexToASCII.py -if <input_file> [-x] [-d <delimiter>]
```

## Arguments

- `-if`, `--input-file`: The path to the input file containing the hexadecimal string. This argument is required.
- `-x`, `--hex`: An optional flag that, when present, causes the output to be in hexadecimal format instead of ASCII.
- `-d`, `--delimiter`: An optional argument that specifies a delimiter to be used when printing the output. If not provided, a space character is used as the delimiter.

## Input Format

The input file should contain the result of a string format vulnerability in which the format "%08x-" has been used . Bytes should be separated by hyphens (`-`). For example:

```
00000020-0804B160-0804853D-00000009-BFFFF55C-B7E19679
```


## Output Format

By default, the output is the ASCII representation of the input string, with each character separated by a space. If the `-x` flag is provided, the output is the hexadecimal representation of the input string, with each byte separated by a space. If the `-d` argument is provided, the specified delimiter is used instead of a space.

## Error Handling

If there is an error when opening the input file, the script will print the message "Error when opening the file" and exit.