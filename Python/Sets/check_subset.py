for _ in range(int(input())):    
    _, A = input(), set(input().split())
    _, B = input(), set(input().split())
    print(not bool(A.difference(B)))