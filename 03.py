def rank(arr):
    arr.sort()
    cards = [{'value': i % 13, 'type': i // 13} for i in arr]

    def is_rank_1():
        t = cards[0]['type']
        for i in cards:
            if i['type'] != t:
                return False
        return cards[-1]['value'] - cards[0]['value'] == 4 or sorted([i['value'] for i in cards]) == [0, 9, 10, 11, 12]
    
    def is_rank_2():
        values = {}
        for i in cards:
            if i['value'] in values:
                values[i['value']] += 1
            else:
                values[i['value']] = 1
        return max(values.values()) == 4
    
    def is_rank_3():
        values = {}
        for i in cards:
            if i['value'] in values:
                values[i['value']] += 1
            else:
                values[i['value']] = 1
        return max(values.values()) == 3 and min(values.values()) == 2
    
    def is_rank_4():
        t = cards[0]['type']
        for i in cards:
            if i['type'] != t:
                return False
        return True
    
    def is_rank_5():
        return cards[-1]['value'] - cards[0]['value'] == 4 or sorted([i['value'] for i in cards]) == [0, 9, 10, 11, 12]
    
    def is_rank_6():
        values = {}
        for i in cards:
            if i['value'] in values:
                values[i['value']] += 1
            else:
                values[i['value']] = 1
        return max(values.values()) == 3
    
    def is_rank_7():
        values = {}
        for i in cards:
            if i['value'] in values:
                values[i['value']] += 1
            else:
                values[i['value']] = 1
        return max(values.values()) == 2 and list(values.values()).count(2) == 2
    
    def is_rank_8():
        values = {}
        for i in cards:
            if i['value'] in values:
                values[i['value']] += 1
            else:
                values[i['value']] = 1
        return max(values.values()) == 2 and list(values.values()).count(2) == 1
    
    if is_rank_1():
        return 'Rank 1'
    elif is_rank_2():
        return 'Rank 2'
    elif is_rank_3():
        return 'Rank 3'
    elif is_rank_4():
        return 'Rank 4'
    elif is_rank_5():
        return 'Rank 5'
    elif is_rank_6():
        return 'Rank 6'
    elif is_rank_7():
        return 'Rank 7'
    elif is_rank_8():
        return 'Rank 8'
    else:
        return 'Rank 9'
    

if __name__ == '__main__':
    arr1 = [26, 27, 28, 29, 30]
    arr2 = [6, 19, 32, 45, 46]
    arr3 = [5, 18, 31, 34, 47]
    arr4 = [26, 27, 32, 36, 38]
    arr5 = [9, 23, 37, 38, 39]
    arr6 = [6, 19, 32, 43, 7]
    arr7 = [5, 18, 34, 8, 43]
    arr8 = [5, 18, 28, 3, 43]
    arr9 = [5, 19, 33, 8, 49]

    print(arr1, '->', rank(arr1))
    print(arr2, '->', rank(arr2))
    print(arr3, '->', rank(arr3))
    print(arr4, '->', rank(arr4))
    print(arr5, '->', rank(arr5))
    print(arr6, '->', rank(arr6))
    print(arr7, '->', rank(arr7))
    print(arr8, '->', rank(arr8))
    print(arr9, '->', rank(arr9))