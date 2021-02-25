def binary_search(lst, left, right, ele):

    if right >= left:

        mid_element = (right+left) // 2
        
        if lst[mid_element] == ele:
            return mid_element
        
        elif lst[mid_element] > ele:
            return binary_search(lst, left, mid_element-1, ele)

        else:
            return binary_search(lst, mid_element+1, right, ele)
    else:
        return -1


lst = [2, 3, 4, 5, 6, 7, 8]

ele = 3

left = 0
right = len(lst)

if __name__ == "__main__":
    res = binary_search(lst, left, right-1, ele)

    if res != -1:
        print(f"Present {str(res)}")
    else:
        print(f"Not in list")
