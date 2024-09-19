class Bubblesort:
    def sort(self, lst):
        for i in range(len(lst)-1, 0, -1):
            for j in range(i):
                if lst[j] > lst[j+1]:
                    lst[j] , lst[j+1] = lst[j+1], lst[j]
        return lst

lst = []

length = int(input())
for i in range(length):
    add = int(input())
    lst.append(add)

bubble = Bubblesort()
print(bubble.sort(lst))