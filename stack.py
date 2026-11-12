"""Stack: a Last-In-First-Out (LIFO) collection.

"""

class Stack:
    """A stack: the last item pushed is the first item popped."""

    def __init__(self):
        self._items = []          # the end of the list is the top of the stack

    def push(self, item):
        """Place an item on top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self._items[-1]

    def is_empty(self):
        """Return True when the stack holds no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items on the stack."""
        return len(self._items)

    def __len__(self):
        return self.size()
