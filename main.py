import sys

"""
# 명령어 사용법
## 형식:
python main.py <input_file> <output_file> <mode>

## 설명:
- <input_file>: 입력 파일 경로 (텍스트 또는 모스 부호 포함)
- <output_file>: 변환된 내용을 저장할 출력 파일 경로
- <mode>: 변환 모드, 아래 중 하나 선택
  - 'to_morse': 텍스트를 모스 부호로 변환
  - 'to_text': 모스 부호를 텍스트로 변환

## 예제:
1. 텍스트 -> 모스 부호 변환
   python main.py input_text.txt output_morse.txt to_morse

2. 모스 부호 -> 텍스트 변환
   python main.py input_morse.txt output_text.txt to_text

## 특수 상황 처리:
1. 잘못된 문자 또는 모스 부호:
   - 경고 메시지 출력 및 공백으로 처리

2. 파일이 없거나 경로가 잘못된 경우:
   - "[ERROR] 입력 파일을 찾을 수 없습니다." 출력

3. 잘못된 모드 입력:
   - "[ERROR] 모드가 잘못되었습니다. 'to_morse' 또는 'to_text'를 사용하십시오." 출력
"""

# 모스 부호 매핑
to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/',

    # 특수 문자 매핑
    '.': '.-.-.-',  # 마침표
    ',': '--..--',  # 쉼표
    '?': '..--..',  # 물음표
    "'": '.----.',  # 작은따옴표
    '!': '-.-.--',  # 느낌표
    '/': '-..-.',  # 슬래시
    '(': '-.--.',  # 왼쪽 괄호
    ')': '-.--.-',  # 오른쪽 괄호
    '&': '.-...',  # 앰퍼샌드
    ':': '---...',  # 콜론
    ';': '-.-.-.',  # 세미콜론
    '=': '-...-',  # 등호
    '+': '.-.-.',  # 더하기
    '-': '-....-',  # 빼기
    '_': '..--.-',  # 밑줄
    '"': '.-..-.',  # 큰따옴표
    '$': '...-..-',  # 달러 기호
    '@': '.--.-.'  # 골뱅이
}
from_morse = {value: key for key, value in to_morse.items()}


# 텍스트를 모스 부호로 변환
def text_to_morse(text):
    text = text.upper()
    result = []
    for char in text:
        if char in to_morse:
            result.append(to_morse[char])
        else:
            print(f"[DEBUG] 변환되지 않는 문자: {char}")
            result.append('/')
    return ' '.join(result)


# 모스 부호를 텍스트로 변환
def morse_to_text(morse):
    result = ''
    for code in morse.split():
        if code in from_morse:
            result += from_morse[code]
        else:
            print(f"[WARNING] 변환되지 않는 모스 부호: {code}")
            result += ' '
    return result


# 파일 처리 함수
def process_file(input_file, output_file, mode):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"[DEBUG] 입력 파일 내용: {content}")

        if mode == 'to_morse':
            result = text_to_morse(content)
        elif mode == 'to_text':
            result = morse_to_text(content)
        else:
            raise ValueError("Invalid mode. Use 'to_morse' or 'to_text'.")

        print(f"[DEBUG] 변환 결과: {result}")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"[INFO] 변환 결과가 {output_file}에 저장되었습니다.")
    except FileNotFoundError:
        print("[ERROR] 입력 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"[ERROR] 파일 처리 중 오류 발생: {e}")


# 명령줄 인터페이스
def main():
    if len(sys.argv) == 4:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        mode = sys.argv[3]
        if mode not in ['to_morse', 'to_text']:
            print("[ERROR] 모드가 잘못되었습니다. 'to_morse' 또는 'to_text'를 사용하십시오.")
        else:
            process_file(input_file, output_file, mode)
    else:
        print("Usage: python morse_converter.py <input_file> <output_file> <mode>")
        print("Modes: to_morse, to_text")


# 테스트 케이스 실행
def run_tests():
    test_cases = [
        ("Hello World", ".... . .-.. .-.. --- / .-- --- .-. .-.. -..", "to_morse"),
        ("123", ".---- ..--- ...--", "to_morse"),
        ("... --- ...", "SOS", "to_text"),
        (".... . .-.. .-.. --- / ... --- ...", "HELLO SOS", "to_text"),
        ("Hello, World!", ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--", "to_morse")
    ]

    for i, (input_text, expected, mode) in enumerate(test_cases):
        if mode == "to_morse":
            result = text_to_morse(input_text)
        elif mode == "to_text":
            result = morse_to_text(input_text)
        else:
            print(f"[ERROR] 잘못된 변환 모드: {mode}")
            continue

        assert result == expected, f"Test {i + 1} failed: {result} != {expected}"
        print(f"Test {i + 1} passed.")


# 스크립트 실행
if __name__ == "__main__":
    main()
    # 테스트 실행 주석 해제 시
    # run_tests()



