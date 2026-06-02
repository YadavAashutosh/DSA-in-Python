class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        count =0 
        end = intervals[0][1]
        for i in range (1,len(intervals)):
            if end >intervals[i][0]:
                count+=1
            else:
                end = intervals[i][1]

        return count
    
o = Solution()
print(o.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(o.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(o.eraseOverlapIntervals([[1,2],[2,3]]))

# 1 [1,3] can be removed and the rest of the intervals are non-overlapping.
# 2 You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# 0 You don't need to remove any of the intervals since they're already non-overlapping.