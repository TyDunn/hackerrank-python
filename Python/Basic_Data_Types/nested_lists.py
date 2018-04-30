if __name__ == '__main__':
    gradebook = []
    for _ in range(int(input())):
        gradebook.append([input(), float(input())])
    sec_high = sorted(list(set([grade for name, grade in gradebook])))[1]
    print('\n'.join([name for name, grade in sorted(gradebook) if grade == sec_high]))
