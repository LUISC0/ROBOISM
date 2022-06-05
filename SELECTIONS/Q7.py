def high_frequency(array):
    return max(set(array), key = array.count)

var = [4,4,4,4,4,1,4,5,6,7,8,65,4,33,]
print(high_frequency(var))
