def twoSum(nums, target):
        dictionary = {}
        answer = []
        
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
                
            dictionary.update({nums[i]: i})


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

target = 9

print(twoSum(lst, target))

