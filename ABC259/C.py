def char_count(s):
    result = []
    c_tmp = s[0]
    c_count = 0
    for i in s:
        if c_tmp == i:
            c_count += 1
        else:
            result.append((c_tmp, c_count))
            c_tmp = i
            c_count = 1
    result.append((c_tmp, c_count))
    return result

S = input()
T = input()

s = char_count(S)
t = char_count(T)

if len(s) != len(t):
    print("No")
    exit()

for (s_char, s_count), (t_char, t_count) in zip(s, t):
    if s_char != t_char:
        print("No")
        exit()
    if s_count > t_count:
        print("No")
        exit()
    if s_count == 1 and t_count > 1:
        print("No")
        exit()
print("Yes")
