class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = collections.defaultdict(list)
    
        for i in strs:
            sort="".join(sorted(i))
            grouped[sort].append(i)
        
        return list(grouped.values())
