# https://www.hackerrank.com/challenges/text-wrap/problem
#
def wrap(string, max_width):
    # make into slices
    parts = [string[idx: idx + max_width] for idx in range(0, len(string), max_width)]
    return "\n".join(parts)

if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)
