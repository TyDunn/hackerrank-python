if __name__ == '__main__':
    n = int(input())
    if n % 2 == 0:
        if n > 5 and n < 21:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")