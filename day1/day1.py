from collections import Counter

def main() -> None:
    with open('day1/input.txt', 'r') as f:
        data = [line.strip().split('   ') for line in f.readlines()]
        col1 = sorted([int(value[0]) for value in data])
        col2 = sorted([int(value[1]) for value in data])

        distances = [abs(col1_val-col2_val) for col1_val, col2_val in zip(col1, col2)]

        answer1 = sum(distances)
        
        col1_count = { k:0 for k in col1}
        counter_1 = Counter(col1_count)
        counter_1.update(col2)

        answer2 = 0
        
        for key, value in counter_1.items():
            if key in col1:
                answer2 += key * value

        print(f"Answer 1: {answer1}")
        print(f"Answer 2: {answer2}")




if __name__ == "__main__":
    main()