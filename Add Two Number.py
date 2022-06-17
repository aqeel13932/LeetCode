# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Way 1
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
    
        #Way 2
            def num2carry(num):
                return num%10,num//10

            start=ListNode()
            current = start
            carry = 0
            
            while l1 is not None and l2 is not None:

                current.val = l1.val +l2.val+carry
                carry=0
                if current.val>9:
                    current.val,carry=num2carry(current.val)

                l1 = l1.next
                l2 = l2.next
                if l1 is not None and l2 is not None:
                    current.next = ListNode()
                    current = current.next
                    
            if l1 is not None or l2 is not None:
                current.next = ListNode()
                current = current.next
            while l1 is not None:
                current.val = l1.val + carry
                carry = 0
                if current.val>9:
                    current.val,carry=num2carry(current.val)
                l1 = l1.next
                if l1 is not None:
                    current.next = ListNode()
                    current = current.next
   
            while l2 is not None:
                current.val = l2.val + carry
                carry =0
                if current.val>9:
                    current.val,carry=num2carry(current.val)
                l2 = l2.next
                if l2 is not None:
                    current.next = ListNode()
                    current = current.next
            
            if carry>0:
                current.next =ListNode()
                current = current.next
                current.val = carry
            return start
