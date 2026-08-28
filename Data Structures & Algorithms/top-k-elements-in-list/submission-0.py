class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_element = {}
        result = []

        for i in nums:
            frequent_element[i] =frequent_element.get(i,0)+1
        
        sorted_elements= sorted(
            frequent_element.items(), 
        key=lambda x: x[1],
        reverse= True)
            

        for item in sorted_elements[:k]:
            result.append(item[0])

        return result


             

