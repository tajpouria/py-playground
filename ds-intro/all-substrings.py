s = "Geeks"
subs = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        subs.append(s[i:j])

print(subs)
