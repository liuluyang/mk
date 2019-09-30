

s = 'aaabbccd'

data = [[s[0], 0]]

for i in s:
    d = data[-1]
    if i == d[0]:
        d[1] += 1
    else:
        data.append([i, 1])

print(data, ''.join([d[0] + str(d[1]) for d in data]))