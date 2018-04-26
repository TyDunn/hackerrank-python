if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    input_list = [int(x) for x in integer_list]
    print(hash(tuple(input_list)))