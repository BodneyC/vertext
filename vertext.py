import sys

text = str.split(sys.stdin.readline())
l_len = len(max(text, key = len))

by_index = []

for i in range(l_len):
    tmp_string = ""
    for word in text:
        if i < len(word):
            tmp_string += word[i] + " "
        else:
            tmp_string += "  "
    by_index.append(tmp_string)

for line in by_index:
    print(line)
