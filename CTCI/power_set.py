#!/bin/python3

def get_subsets(arr, idx):
    all_subsets = []
    if len(arr) == idx:
        all_subsets.append([])
    else:
        all_subsets = get_subsets(arr, idx+1)
        item = arr[idx]
        more_subsets = []
        for subset in all_subsets:
            new_subset = []
            new_subset += subset
            new_subset.append(item)
            more_subsets.append(new_subset)
        all_subsets += more_subsets
    return all_subsets

if __name__ == '__main__':

    lst = lst = list(map(int, input().split()))

    result = get_subsets(lst, 0)
    
    print(sorted(result))