import re

def main() -> None:
    with open('input.txt', 'r') as f:
        content = f.read()  # Read the entire file content

        # Part 1
        answer_1 = 0
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        matches = re.findall(pattern, content)

        for x, y in matches:
            answer_1 += int(x)*int(y)
        
        print(f"Answer 1: {answer_1}")

        # Part 2
        answer_2 = 0

        mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)') # Pattern for mul(X,Y)
        dont_pattern = re.compile(r"don't\(\)")                 # Pattern for don't()
        do_pattern = re.compile(r'do\(\)')                      # Pattern for do()

        is_enabled = True  # Start with capturing enabled

        # Split the input into tokens (based on matches for mul, don't, and do)
        tokens = re.split(r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))", content)

        for token in tokens:
            if not token:  # Ignore empty tokens
                continue
            if dont_pattern.fullmatch(token):  # If "don't()" is encountered
                is_enabled = False
            elif do_pattern.fullmatch(token):  # If "do()" is encountered
                is_enabled = True
            elif is_enabled and mul_pattern.fullmatch(token):  # If "mul(X,Y)" and capturing is enabled
                match = mul_pattern.fullmatch(token)
                answer_2 += int(match.group(1)) * int(match.group(2))

        print(f"Answer 2: {answer_2}")


if __name__ == "__main__":
    main()