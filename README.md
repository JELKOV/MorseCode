# Morse Code Converter

This project is a Python-based Morse Code Converter. It allows you to convert text to Morse code and vice versa. You can process files with the converter, and it supports various special characters as well.

---

## Features
- Convert **text to Morse code**.
- Convert **Morse code to text**.
- Supports **special characters** like commas, periods, and more.
- Includes a command-line interface (CLI).
- Handles invalid inputs gracefully with debug messages.

---

## How to Use

### Command Format
```bash
python main.py <input_file> <output_file> <mode>
```

### Arguments
- `<input_file>`: Path to the input file (text or Morse code).
- `<output_file>`: Path to save the converted result.
- `<mode>`: Conversion mode.
  - `to_morse`: Converts text to Morse code.
  - `to_text`: Converts Morse code to text.

### Example Usage
1. **Convert text to Morse code**:
   ```bash
   python main.py input_text.txt output_morse.txt to_morse
   ```

2. **Convert Morse code to text**:
   ```bash
   python main.py input_morse.txt output_text.txt to_text
   ```

### Special Situations
1. **Invalid characters**:
   - Displays a debug message and replaces them with `/`.

2. **File not found**:
   - Displays: `[ERROR] 입력 파일을 찾을 수 없습니다.`

3. **Invalid mode**:
   - Displays: `[ERROR] 모드가 잘못되었습니다. 'to_morse' 또는 'to_text'를 사용하십시오.`

---

## Supported Special Characters
The following special characters are supported in Morse code:

| Character | Morse Code  |
|-----------|-------------|
| `.`       | `.-.-.-`    |
| `,`       | `--..--`    |
| `?`       | `..--..`    |
| `'`       | `.----.`    |
| `!`       | `-.-.--`    |
| `/`       | `-..-.`     |
| `(`       | `-.--.`     |
| `)`       | `-.--.-`    |
| `&`       | `.-...`     |
| `:`       | `---...`    |
| `;`       | `-.-.-.`    |
| `=`       | `-...-`     |
| `+`       | `.-.-.`     |
| `-`       | `-....-`    |
| `_`       | `..--.-`    |
| `"`       | `.-..-.`    |
| `$`       | `...-..-`   |
| `@`       | `.--.-.`    |

---

## Running Tests

This project includes built-in test cases to verify the functionality of the converter.

### Steps to Run Tests
1. Open the `main.py` file.
2. Uncomment the `run_tests()` function in the `if __name__ == "__main__":` block:
   ```python
   if __name__ == "__main__":
       # main()
       run_tests()
   ```
3. Run the script:
   ```bash
   python main.py
   ```

### Test Output
- If all tests pass:
  ```
  Test 1 passed.
  Test 2 passed.
  Test 3 passed.
  Test 4 passed.
  Test 5 passed.
  ```
- If a test fails, it will show the expected and actual results for debugging.

---

## File Structure
```
Morse Code Converter
│
├── main.py         # Main script for the converter
├── input_text.txt  # Example input file (text)
├── input_morse.txt # Example input file (Morse code)
├── output_morse.txt # Example output file (Morse code)
├── output_text.txt # Example output file (text)
└── README.md       # Project documentation
```

---

## Requirements
- Python 3.6 or higher

---

## Contributing
If you have suggestions or improvements, feel free to submit a pull request or open an issue in the repository.

---

## License
This project is open-source and available under the MIT License.

---

## Contact
For questions or support, please contact:
- **Email**: [ajh4234@gmail.com](ajh4234.gmail.com)
- **GitHub**: [https://github.com/JELKOV](https://github.com/JELKOV)

