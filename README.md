# kc303va1 - Kilian Code 303 Version Alpha 1

## Overview

`kc303va1` is a minimalistic programming language designed for simplicity and ease of use. It uses a unique syntax with delimiters and a minimal set of keywords to perform basic computations and control flow.

## Features

- **Function Definitions**: Define functions with input and output parameters.
- **Variables**: Input, output, and local variables.
- **Control Flow**: Conditional statements (`if`, `else`), looping constructs (`while`, `for`).
- **Operators**: Arithmetic, comparison, and logical operators.
- **Comments**: Multiline comments using `/* ... */`.

## Getting Started

### Prerequisites

- Python 3.x
- ANTLR 4
- ANTLR Python runtime

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/kc303va1.git
   cd kc303va1
Install dependencies:


sudo apt-get install antlr4
pip install antlr4-python3-runtime
Generate the parser:


antlr4 -Dlanguage=Python3 KilianCode303va1.g4
Usage
Run the interpreter:


python interpreter.py example.kc303va1
Example Code:


§§f§main
§xo§BACKUP_FOLDER = "autominibackups"
§xo§CONFIG_FILE = "autominibackups_file_watch_config.txt"

mkdir -p §xo§BACKUP_FOLDER

if [ ! -f §xo§CONFIG_FILE ]; then
echo "# Enter files to watch (one per line):" > §xo§CONFIG_FILE
echo "# Example: /path/to/file1.txt" >> §xo§CONFIG_FILE
echo " >> §xo§CONFIG_FILE"
echo "# LEAVE THIS AS THE LAST LINE PLEASE" >> §xo§CONFIG_FILE
echo "Config file created. Please add files to watch in §xo§CONFIG_FILE and run the script again."
exit 0
fi

if ! command -v entr &> /dev/null; then
echo "entr is not installed. Please install it and run the script again."
exit 1
fi

§§f§is_file_readable
§xi§file = §xi§1
if [ ! -f §xi§file ]; then
echo "Warning: File '§xi§file' does not exist. Skipping."
return 1
elif [ ! -r §xi§file ]; then
echo "Warning: File '§xi§file' is not readable. Skipping."
return 1
fi
return 0

§§f§watch_file
§xi§file = §xi§1
if §f§is_file_readable §xi§file; then
echo "Watching §xi§file"
filename="\${§xi§file##*/}"
extension="\${filename##*.}"
filename_no_ext="\${filename%.*}"
timestamp=\$(date +'%y%m%d%H%M%S')
backup_filename="${filename_no_ext}_autominibackup${timestamp}.\${extension}"
echo §xi§file | entr -p sh -c "cp '§xi§file' '§xo§BACKUP_FOLDER/§xo§backup_filename'" &
fi

while IFS= read -r file; do
if [ -n §xi§file ] && [[ ! §xi§file =~ ^\s*# ]]; then
§f§watch_file §xi§file
fi
done < §xo§CONFIG_FILE

echo "File watching started. Press Ctrl+C to stop."
wait
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.