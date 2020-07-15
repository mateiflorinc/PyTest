# exercise1: reverse order of a = [1,2,3,4,5]
a = [1, 2, 3, 4, 5, 8, 0, 11, 6]
print('The reversed order of', a, 'is:')
a.reverse()
print(a, '\n')

# exercise2: no of occurrences of var b in array a
a = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 2]
b = 3
print('The number of occurrences of var:', b, 'in the a array is: ', a.count(b), '\n')

# exercise3: no of words in string
a = 'The greatest glory in living lies not in never falling, but in rising every time we fall'
print('The number of words in the sentence: "', a, '" is:', len(a.split()), '\n')