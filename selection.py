class Selection_sort:
    def sort(self, lst):
        for i in range(len(lst)-1):
            min = i
            for j in range(i, len(lst)):
                if lst[j] < lst[min]:
                    min = j
            if min != i:
                lst[i] = lst[i] + lst[min]
                lst[min] = lst[i] - lst[min]
                lst[i] = lst[i] - lst[min]
            else:
                continue
        return lst

lst = []
length = int(input())

for i in range(length):
    add = int(input())
    lst.append(add)

select = Selection_sort()
print(select.sort(lst))