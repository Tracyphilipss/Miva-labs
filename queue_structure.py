"""Queue: a First-In-First-Out (FIFO) collection.

The file is called queue_structure.py (not queue.py) so that it does not hide
Python's built-in 'queue' module, which many tools and IDE debuggers import.
This module depends on nothing else in the project.
"""

from collections import deque


class Queue:
    """A queue: the first item added is the first item removed."""

    def __init__(self):
        self._items = deque()     # deque gives fast removal from the front

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self._items.popleft()

    def peek(self):
        """Return the front item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue.")
        return self._items[0]

    def is_empty(self):
        """Return True when the queue holds no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)

    def __len__(self):
        return self.size()
