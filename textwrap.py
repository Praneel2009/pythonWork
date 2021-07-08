# https://www.hackerrank.com/challenges/text-wrap/problem
def wrap(string, max_width):
    # make into slices
    result = []
    idx = 0
    while idx < len(string):
        part = string[idx: idx + max_width]
        result.append(part)
        idx = idx + max_width

    return "\n".join(result)


if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)
