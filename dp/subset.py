def is_subset(lst, sum_num, nums):

    memo = [[False for i in range(sum_num+1)] for i in range(nums+1)]

    # if sum == 0
    for i in range(0, nums+1):
        memo[i][0] = True

    # if sum != 0 and lst == Null
    for i in range(0, sum_num+1):
        memo[0][i] = False
    
    
    for i in range(0, nums+1):
        for j in range(0, sum_num+1):
            if j < lst[i-1]:
                memo[i][j] = memo[i-1][j]
            if j > lst[i-1]:
                memo[i][j] = (memo[i-1][j]
                or
                memo[i-1][j-lst[i-1]]
                )
    
    return memo[nums][sum_num]

if __name__ =="__main__":
    lst = [3, 34, 4, 12, 5, 2]
    sum = 9
    num = len(lst)
    
    if is_subset(lst, sum, num):
        print("there")
    else:
        print("no")

