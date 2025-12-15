"""
Health Record Symmetry Checker

Determines if a patient's health metrics form a palindrome pattern.

Time Complexity: O(n) - single pass to find middle, reverse, and compare
Space Complexity: O(1) - in-place reversal, no extra data structures
"""

from typing import Optional


class ListNode:
    """Node representing a single health metric reading."""
    
    def __init__(self, value: int, next_node: 'ListNode' = None):
        self.value = value
        self.next = next_node


def isHealthRecordSymmetric(head: Optional[ListNode]) -> bool:
    """
    Check if health record sequence is symmetric (palindrome).
    
    Uses Floyd's algorithm to find middle, reverses second half,
    then compares both halves.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        True if palindrome, False otherwise
    """
    if not head or not head.next:
        return True
    
    # Find middle using slow/fast pointers
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second_half = reverse_list(slow.next)
    
    # Compare both halves
    first_half = head
    result = True
    while second_half:
        if first_half.value != second_half.value:
            result = False
            break
        first_half = first_half.next
        second_half = second_half.next
    
    return result


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a linked list in-place."""
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def create_linked_list(values: list) -> Optional[ListNode]:
    """Helper to create linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def list_to_array(head: Optional[ListNode]) -> list:
    """Helper to convert linked list to array for display."""
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


if __name__ == "__main__":
    test_cases = [
        [120, 80, 75, 80, 120],  # Symmetric
        [98, 102, 98],           # Symmetric
        [120, 80, 75, 90, 120],  # Not symmetric
        [],                      # Empty - symmetric
        [100],                   # Single - symmetric
    ]
    
    for values in test_cases:
        head = create_linked_list(values)
        result = isHealthRecordSymmetric(head)
        print(f"Input: {values} -> Symmetric: {result}")
    
if __name__ == '__main__':
    main()