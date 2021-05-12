# 36ms
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        t=dummy=ListNode(0)
        array=[]
        temp=head
        while temp:
            array.append(temp.val)
            temp=temp.next
        array.sort()
        for i in array:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return t.next
# 타임오버
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next
            cur = parent  # 다시 cur을 맨 앞으로 이동

        return parent.next

# 172ms (책)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 만약 새로운 head보다 cur 값이 작다면, cur을 굳이 갱신하지 않고 이전 상태에서 부터 검사할 수 있음
            # 왜냐하면 어차피 위의 경우, cur 이전 값은 cur보다 작기 때문에 조사할 필요가 없음
            if head and cur.val > head.val:
                cur = parent
        return parent.next


from heapq import *



# 52ms
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        h = []
        dummy = ListNode(0)
        cur = dummy

        while head:
            heappush(h, head.val)
            head = head.next

        while h:
            cur.next = ListNode(heappop(h))
            cur = cur.next

        return dummy.next


# 60ms
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        p = head

        lst = []

        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        myListNode = ListNode()

        def inputValue(node):
            if lst:
                node.val = lst.pop(0)
                if lst:
                    node.next = ListNode()
                    inputValue(node.next)

        inputValue(myListNode)
        return myListNode