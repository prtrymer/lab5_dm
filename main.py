table = [[0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 0, 1],
         [0, 1, 1, 1],
         [1, 0, 0, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 1, 1, 0]]
func = [1, 1, 1, 1, 1, 0, 1, 0]


def task1(matrix):
    for row in matrix:
        print(row)


def task2(f):
    print(dual(f))


def task3(f, tab):
    print("Here is ddnf: ")
    print(ddnf(f, tab))
    print("Here is dknf: ")
    print(dknf(f, tab))


def task4(f, tab):
    print("Zhegalkin's polionom:")
    print(Zhegalkin(f, tab))


def task5(f, tab):
    print("Check on saving constant: ")
    const(f)
    print("Check on monoduality: ")
    monoduality(f)
    print("Check on monotone: ")
    monoton(f)
    print("Check on linearity: ")
    linearity(f, tab)


def dual(f):
    k = list(reversed(f))
    for i in range(8):
        if k[i] == 0:
            k[i] = 1
        else:
            k[i] = 0
    return k


def ddnf(arr, tabl):
    res = ""
    for i in range(0, len(arr)):
        if arr[i]:
            res += "("
            if tabl[i][0]:
                res += "x"
            else:
                res += "¬x"
            res += " ∧ "
            if tabl[i][1]:
                res += "y"
            else:
                res += "¬y"
            res += " ∧ "
            if tabl[i][2]:
                res += "z"
            else:
                res += "¬z"
            res += ")\/"
    return res[:len(res) - 2]


def dknf(arr, tabl):
    res = ""
    for i in range(0, len(arr)):
        if arr[i] == 0:
            res += "("
            if tabl[i][0]:
                res += "x"
            else:
                res += "¬x"
            res += " ∧ "
            if tabl[i][1]:
                res += "y"
            else:
                res += "¬y"
            res += " ∧ "
            if tabl[i][2]:
                res += "z"
            else:
                res += "¬z"
            res += ")\/"
    return res[:len(res) - 2]


def Zhegalkin(f, tab):
    ZhegalkinPolynomial = 'f(x1, x2, x3) = '
    for i in range(len(tab)):
        if f[i] == 1:
            ZhegalkinPolynomial += '('
            for j in range(len(tab[i]) - 1):
                if tab[i][j] == 1:
                    ZhegalkinPolynomial += ('x' + str(j + 1))
                else:
                    ZhegalkinPolynomial += ('x' + str(j + 1) + ' ⊕ 1')

                if j + 1 != 3:
                    ZhegalkinPolynomial += str(' ∧ ')

            ZhegalkinPolynomial += ') ⊕ '

    newZhegalkinPolynomial = ZhegalkinPolynomial[:len(ZhegalkinPolynomial) - 3]
    return newZhegalkinPolynomial


def const(arr):
    o = 0
    n = 0
    for i in arr:
        if i == 1:
            o += 1
        if i == 0:
            n += 1
    if o < 1:
        print("Function isn't saving constant 1")
    else:
        print("Function isn't saving constant 1")
    if n < 1:
        print("Function isn't saving constant 0")
    else:
        print("Function isn't saving constant 0")


def monoton(arr):
    m = 0
    for i in range(0, (len(arr) - 1)):
        if arr[i] > arr[i + 1]:
            m += 1
    if m == len(arr):
        print("Your function is monotone")
    else:
        print("Your function is not monotone")


def monoduality(arr):
    if arr == dual(arr):
        print("Function is monodual")
    else:
        print("Function is not monodual")


def linearity(f, tab):
    k = 0
    for i in Zhegalkin(f, tab):
        if i == "∧":
            k += 1
    if k >= 1:
        print("Function is not linear")
    else:
        print("Function is linear")


task5(func, table)
