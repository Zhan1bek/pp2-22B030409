def spy_game(nums):
    my_list = []
    x = len(nums) - 1
    for i in range(0, x):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            my_list.append(1)
        else:
            my_list.append(0)
    if 1 in my_list:
        return True
    else:
        return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))