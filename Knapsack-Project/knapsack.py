
#defines an object item that has a name, weight and value to be called later
class Item:
    def __init__(self, name, val, wt):
        self.name = name
        self.wt = wt
        self.val = val


def knapsack(items, cap):
    n = len(items) # initiallize n as the length of the list of items
    tbl = [[0] * (cap + 1) for _ in range(n + 1)] #initialize the table that will place values from the bottom up
    selected = [] #initialize array of selected values

    for i in range(1, n + 1):
        wt = items[i - 1].wt
        val = items[i - 1].val
        for j in range(1, cap + 1):
            if wt > j:
                tbl[i][j] = tbl[i - 1][j]
            else:
                tbl[i][j] = max(tbl[i - 1][j], val + tbl[i - 1][j - wt])

    w = cap 
    for i in range(n, 0, -1):
        if tbl[i][w] != tbl[i - 1][w]:
            selected.append(items[i - 1])
            w -= items[i - 1].wt

    return tbl[n][cap], selected

def test1():
    i1 = Item("gold", 10, 2)
    i2 = Item("ruby", 15, 3)
    i3 = Item("dimond", 20, 5)
    i4 = Item("jade", 25, 7)
    items = [i1, i2, i3, i4]
    cap = 10
    max, selected = knapsack(items, cap)

    print("Maximum val:", max)
    print("Selected items:")
    for item in selected:
        print(item.name)

def test2():
    i1 = Item("1", 13, 9)
    i2 = Item("2", 7, 33)
    i3 = Item("3", 18, 63)
    i4 = Item("4", 17, 47)
    i5 = Item("5", 12, 18)
    i6 = Item("6", 4, 63)
    i7 = Item("7", 19, 76)
    i8 = Item("8", 11, 81)
    i9 = Item("9",16, 55)
    i10 = Item("10", 7,44)
    
    items = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
    cap = 100
    max, selected = knapsack(items, cap)

    print("Maximum val:", max)
    print("Selected items:")
    for item in selected:
        print(item.name)

test1()
test2()
