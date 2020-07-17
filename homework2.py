# exercise1 - extract pairs of characters from one string
def extract_pairs(value):
    a = []
    if len(x) % 2 == 0:
        for i in range(0, len(x) - 1, 2):
            a.append(f'{x[i]}{x[i + 1]}')
    else:
        for i in range(0, len(x) // 2, 1):
            a.append(x[i] + x[i + 1])
        a.append(x[len(x) - 1] + '_')
    print(a, '\n')


x = 'abcdf'
print("#Excercise 1")
extract_pairs(x)


# exercise2 - invert each word in a sentence
def word_reverse(value):
    a = value.split()
    phr = ''
    for i in range(0, len(a), 1):
        for j in range(len(a[i]), 0, -1):
            phr += a[i][j - 1]
        phr += ' '
    print(phr,"\n")


x = 'This is an example!'
print('#Exercise 2')
word_reverse(x)



# exercise3 - Adam&Eve
class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    pass


class Woman(Human):
    pass


def create():
    return Man('Adam'), Woman('Eve')


a, b = create()
print('#Exercise 3')
print(f'Man= {a.name}, Woman= {b.name}')
if issubclass(Man, Human) == True:
    print("Man is a subclass of Human")
if issubclass(Woman, Human) == True:
    print("Woman is a subclass of Human\n")

