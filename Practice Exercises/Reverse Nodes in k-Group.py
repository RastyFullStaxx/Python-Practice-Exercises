class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_list(head, k):
        prev = None
        curr = head

        while k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1

        return prev

    count = 0
    curr = head

    while count < k:
        if not curr:
            return head
        curr = curr.next
        count += 1

    new_head = reverse_list(head, k)
    head.next = reverse_k_group(curr, k)

    return new_head

# Example usage
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k_value = 2
result = reverse_k_group(head, k_value)
