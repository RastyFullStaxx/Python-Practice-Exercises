class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    carry = 0
    dummy = ListNode()
    current = dummy

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry

        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        current.next = ListNode(carry)

    return dummy.next

# Example usage
# Create two linked lists: 2 -> 4 -> 3 and 5 -> 6 -> 4
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = add_two_numbers(l1, l2)
