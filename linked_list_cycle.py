def linked_list_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next #moves 1 step at a time
        fast = fast.next.next #moves 2 steps at a time

        if slow == fast:
            return True

    return False

print(linked_list_cycle([3, 2, 0, -4]))  # Output: True