from collections import Counter
class Solution():
    def findMatrix(self, nums):
        twodarr=[]
        counter_object = Counter(nums)
        max_freq = max(counter_object.values())
        matrix = [[] for i in range(max_freq)]
        j = 0
        print(counter_object.items())
        for num, freq in counter_object.items():
            for k in range(freq):
                matrix[j].append(num)
                j = (j+1)%len(matrix)
        return matrix        
