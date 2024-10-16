N = int(input())
record = []

for n in range(N):
    record.append(input())

M = int(input())
candidates = []

for m in range(M):
    candidates.append(input())

if "?" in record:
    i = record.index("?")
    if i == 0:
        first_char = ""
    else:
        first_char = record[i - 1][-1]

    if i == len(record) - 1:
        last_char = ""
    else:
        last_char = record[i + 1][0]

    for word in candidates:
        if word not in record:
            if (not first_char or word[0] == first_char) and (not last_char or word[-1] == last_char):
                print(word)