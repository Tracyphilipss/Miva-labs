"""Singly linked list: nodes joined by a single 'next' reference.

"""


class Node:
    """One link in the chain: some data and a reference to the next node."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    """A list that can only be walked from the head towards the tail."""

    def __init__(self):
        self._head = None
        self._size = 0

    def append(self, data):
        """Add data at the end of the list."""
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, data):
        """Add data at the start of the list."""
        self._head = Node(data, self._head)
        self._size += 1

    def find(self, matches):
        """Return the first data item for which matches(data) is True, else None."""
        for data in self:
            if matches(data):
                return data
        return None

    def remove(self, matches):
        """Remove the first item for which matches(data) is True.

        Returns the removed data, or None if nothing matched.
        """
        previous, current = None, self._head
        while current is not None:
            if matches(current.data):
                if previous is None:
                    self._head = current.next      # removing the head
                else:
                    previous.next = current.next   # bypass the removed node
                self._size -= 1
                return current.data
            previous, current = current, current.next
        return None

    def to_list(self):
        """Return the data as an ordinary Python list (head to tail)."""
        return list(self)

    def is_empty(self):
        """Return True when the list holds no items."""
        return self._head is None

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        return self._size
