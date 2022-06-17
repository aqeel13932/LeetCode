# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def num2carry(num):
        result = []
        while l1 is not None and l2 is not None:
            result.append(l1.val+l2.val)
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            result.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            result.append(l2.val)
            l2 = l2.next

        for i in range(len(result)):
            if result[i]>=10:
                rem = result[i]%10
                if i+1==len(result):
                    result.append(result[i]//10)
                else:
                    result[i+1]+=result[i]//10
                result[i]=result[i]%10

        start=ListNode()
        current = start
        i = 0
        while(i<len(result)):
            current.val = int(result[i])
            i+=1
            if i<len(result):
                current.next= ListNode()
                current = current.next

        return start
