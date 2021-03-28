def permute(arr=[]):
    res = []

    l = len(arr)
    d = arr.copy()

    def _permute(d, i):
        if i == l - 1:
            res.append(''.join(d))
    

        for j in range(i, l):
            d[i], d[j] = d[j], d[i]
            _permute(d, i+1)
            d[i], d[j] = d[j], d[i]

    _permute(d, 0)

    return res


print(permute(list('abc')))
