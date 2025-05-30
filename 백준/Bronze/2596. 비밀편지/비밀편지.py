def check(received_list):
    check_list = {
        "A": "000000", "B": "001111", "C": "010011", "D": "011100",
        "E": "100110", "F": "101001", "G": "110101", "H": "111010"
    }
    
    result = []
    for i, code in enumerate(received_list, 1):
        # 정확히 일치하는 문자 확인
        for char, pattern in check_list.items():
            if code == pattern:
                result.append(char)
                break
        else:
            # 1글자 다른 문자 확인
            candidates = []
            for char, pattern in check_list.items():
                if sum(c1 != c2 for c1, c2 in zip(code, pattern)) == 1:
                    candidates.append(char)
            if len(candidates) == 1:
                result.append(candidates[0])
            else:
                return i
    return "".join(result)

n = int(input())
code = input().strip()
received_list = [code[i:i+6] for i in range(0, n*6, 6)][:n]
print(check(received_list))