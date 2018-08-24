def minion_game(string):
    vowels = 'AEIOU'
    
    kevin_score = 0
    stuart_score = 0
    
    for idx in range(len(string)):
        if string[idx] in vowels:
            kevin_score += (len(string)-idx)
        else:
            stuart_score += (len(string)-idx)
    
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")