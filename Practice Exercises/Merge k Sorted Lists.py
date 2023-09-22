class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    import heapq

    heap = []
    for i, node in enumerate(lists):
        if node:
            heap.append((node.val, i, node))

    heapq.heapify(heap)
    dummy = ListNode()
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# Example usage
# Create sorted linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]
result = merge_k_sorted_lists(lists)
