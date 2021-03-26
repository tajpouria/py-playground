def lcs(a, b):
	len_a , len_b = len(a), len(b)
	m = [[0] * (len_b + 1)  for i in range(len_a + 1)]

	for i in range(len_a + 1):
		for j in range(len_b + 1):
			if i == 0 or j == 0:
				m[i][j] = 0
			elif a[i-1] == b[j-1]:
				m[i][j] = m[i-1][j-1] + 1
			else:
				m[i][j] = max(m[i-1][j], m[i][j-1])

	return m, m[len_a][len_b]

t, res = lcs("AGGTAB", "GXTXAYB")

for i in t:
	print(i)	
print(res)
