
class Binary_Search:

    position = []
    def __init__(self, lst):
        for i in range(len(lst)-1):
            min = i
            for j in range(i, len(lst)):
                if lst[j] < lst[min]:
                    min = j
            lst[i], lst[min] = lst[min], lst[i]
        print(lst)


    def search_fun(self, lst, search_element, new_lst):
        lower_bound = 0
        upper_bound = len(lst) - 1
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if lst[mid] == search_element:
                for i in range(len(new_lst)):
                    if search_element == new_lst[i]:
                        Binary_Search.position.append(i+1)
                return True
            else:
                if lst[mid] < search_element:
                    lower_bound = mid + 1
                else:
                    upper_bound = mid - 1
        return False

lst = []
new_lst = []
length = int(input())
for i in range(length):
    add = int(input())
    lst.append(add)

new_lst = list(lst)

search_element = int(input())
binary = Binary_Search(lst)


if (binary.search_fun(lst, search_element, new_lst)):
    print("Element Found at", binary.position)
else:
    print("Element not found")