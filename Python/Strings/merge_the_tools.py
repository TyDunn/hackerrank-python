if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

def merge_the_tools(string, k):
    for sub in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in sub if c not in d]))