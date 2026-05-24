class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a=[]
        top=0
        bottom = len(matrix)-1
        left=0
        right=len(matrix[0])-1

        while top<=bottom and left<=right:
            
            #left to right
            for i in range(left,right+1):
                a.append(matrix[top][i])
            top +=1
            
            #top to bottom
            for i in range(top,bottom+1):
                a.append(matrix[i][right])
            right-=1

            if top<=bottom:
            #right to left
                for i in range(right,left-1,-1):
                    a.append(matrix[bottom][i])
                bottom-=1
            
            if right>=left:
            #bottomto top
                for i in range(bottom,top-1,-1):
                    a.append(matrix[i][left])
                left+=1
        return a

output = Solution()
print(output.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(output.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

# [1, 2, 3, 6, 9, 8, 7, 4, 5]
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]



    
      