# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        arr = []
        curr = head
        
        while curr!=None:
            arr.append(curr)
            curr=curr.next
        
        i=0
        j=len(arr)-1
        # print(i,j)

        # 0,n,1,n-1,2,n-2,3,n-3
        while i<j:
            arr[i].next = arr[j]
            i+=1
            arr[j].next = arr[i]
            j-=1
        arr[i].next=None

        print(arr)


