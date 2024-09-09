# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*n for _ in range(m)]
        i,j = 0, 0
        di, dj = 1, 0
        copy_head = head
        while copy_head:
            mat[j][i]=copy_head.val
            if i+di<0 or i+di>=n or j+dj<0 or j+dj>=m or mat[j+dj][i+di]>=0:
                di, dj = -dj, di
            j+=dj
            i+=di
            copy_head=copy_head.next
        return mat