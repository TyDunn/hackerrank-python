import string

alpha = string.ascii_lowercase

def print_rangoli(size):
    for i in range(size - 1, 0, -1):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = alpha[j + i]
            row[size - 1 + j] = alpha[j + i]
        print("-".join(row))

    for i in range(0, size):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = alpha[j + i]
            row[size - 1 + j] = alpha[j + i]
        print("-".join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)