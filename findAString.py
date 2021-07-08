def count_substring(string, sub_string):
    lN = len(string)
    l2 = len(sub_string)
    counts = 0
    for idx in range(lN - l2 + 1):
        if string[idx: idx + l2] == sub_string:
            counts = counts + 1
    return counts


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)