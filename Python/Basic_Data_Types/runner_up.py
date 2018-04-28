if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    first = max(arr)
    while max(arr) == first:
        arr.remove(max(arr))
    print(max(arr))