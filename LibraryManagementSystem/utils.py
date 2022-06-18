def first_negative_index(nums):
    for idx, num in enumerate(nums):
        if num == -1:
            return idx

    return None

def count_total_negative_index(nums:list):
    count=0
    for num in nums:
        if num==-1:
            count+=1
    return count


def add_list_elements_to_set(s, l):
    for num in l:
        s.add(num)

def search_element_in_list(l, e):
    for idx, num in enumerate(l):
        if num==e:
            return idx
    return None

