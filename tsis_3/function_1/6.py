def has_33(nums):
    my_list = []
    x =len(nums)-1
    for i in range(0,x) :
        if nums[i] == 3 and nums[i+1] == 3:
            my_list.append(1)
        else :
            my_list.append(0)
    if 1 in my_list:
        return True
    else :
        return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))