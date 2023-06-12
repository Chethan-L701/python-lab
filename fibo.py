def fibo(num: int, fmap: dict = {}) -> int:
    if (num <= 1):
        return num
    if num in fmap.keys():
        return fmap[num]
    fmap[num] = fibo(num-1, fmap)+fibo(num-2, fmap)
    return fmap[num]


li = [10, 20, 30, 40, 22, 33, 4, 5, 7]

for i in li:
    print("{} : {}".format(i, fibo(i)))
