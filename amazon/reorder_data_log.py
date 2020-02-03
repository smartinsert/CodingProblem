from typing import List


def reorder_log_files(logs: List[str]) -> List[str]:
    result_1, result_2 = [], []

    for log in logs:
        if (log.split()[1]).isdigit():
            result_2.append(log)
        else:
            result_1.append(log.split())

    result_1.sort(key=lambda x: x[0])
    result_1.sort(key=lambda x:x[1:])

    for i in range(len(result_1)):
        result_1[i] = ' '.join(result_1[i])

    result_1.extend(result_2)

    return result_1


if __name__ == '__main__':
    print(reorder_log_files(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))