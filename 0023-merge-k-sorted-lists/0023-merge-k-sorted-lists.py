from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        dummy = ListNode()
        cur = dummy

        while heap:
            _, i, node = heappop(heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next