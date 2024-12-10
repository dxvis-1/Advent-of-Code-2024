def is_safe(report):
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    follows_adjacent_rule = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

    return follows_adjacent_rule and (is_increasing or is_decreasing)


def main() -> None:
    with open('input.txt', 'r') as f:
        input = [[int(level) for level in line.strip().split(' ')] for line in f]

        answer_1 = 0
        answer_2 = 0

        for report in input:
            if is_safe(report):
                answer_1 += 1
                answer_2 += 1
            else:
                sub_reports = [report[:i] + report[i+1:] for i in range(len(report))]   # Generate sub-reports  
                if any(is_safe(sub_report) for sub_report in sub_reports):
                    answer_2 += 1
        
        print(f"Answer 1: {answer_1}")
        print(f"Answer 2: {answer_2}")


if __name__ == "__main__":
    main()