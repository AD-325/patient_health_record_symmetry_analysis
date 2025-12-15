# Health Record Symmetry Checker

Checks if a patient's health metrics (linked list) form a palindrome pattern.

## Algorithm

1. Find middle node using slow/fast pointers
2. Reverse second half in-place
3. Compare both halves

## Complexity

| Metric | Value | Reason |
|--------|-------|--------|
| Time | O(n) | Single traversal |
| Space | O(1) | In-place reversal |

## Files

- `health_record.py` - Main implementation
- `test_health_record.py` - Unit tests (5 normal + 6 edge cases)
- `diagram.mermaid` - Algorithm flowchart
- `clarifying_questions.md` - Interview questions

## Usage

```python
from health_record import create_linked_list, isHealthRecordSymmetric

head = create_linked_list([120, 80, 75, 80, 120])
result = isHealthRecordSymmetric(head)  # True
```

## Run Tests

```bash
python test_health_record.py
```