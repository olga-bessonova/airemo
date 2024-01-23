from typing import MutableSequence, Sequence

def append_to(element: int,
              target_list: MutableSequence[int] = []) -> Sequence[int]:
  # """Adds an element to a list and returns the list."""
  target_list.append(element)
  return target_list

print(append_to(2,[3,55,6]))
print(append_to(2))
print(append_to(1000))