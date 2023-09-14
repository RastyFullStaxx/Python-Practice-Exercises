class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_linked_list(head):
    if not head or not head.next:
        return head

    prev, slow, fast = None, head, head

    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next

    prev.next = None
    left_sorted = sort_linked_list(head)
    right_sorted = sort_linked_list(slow)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next, left = left, left.next
        else:
            current.next, right = right, right.next

        current = current.next

    current.next = left or right

    return dummy.next

# Example usage
# Create linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sorted_head = sort_linked_list(head)
