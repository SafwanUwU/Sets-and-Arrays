import array as arr
arrayNum = arr.array('i', [1,3,5,3,7,9,3,5,3,3,3,3,])
print("Original Array:", arrayNum)
print(arrayNum.count(3))
arrayNum.reverse()
print(arrayNum)