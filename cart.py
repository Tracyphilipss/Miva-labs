"""ShoppingCart: a customer's items (linked list) with undo support (stack)."""

from linkedlist import SinglyLinkedList
from stack import Stack


class ShoppingCart:
    """Holds one customer's items and remembers actions so they can be undone."""

    def __init__(self, owner):
        self.owner = owner
        self._items = SinglyLinkedList()    # the items in the cart
        self._history = Stack()             # actions, newest on top, for undo

    def add_item(self, item):
        """Add an item to the cart and record the action."""
        self._items.append(item)
        self._history.push(("add", item))

    def remove_item(self, name):
        """Remove the first item with this name. Returns it, or None if absent."""
        removed = self._items.remove(lambda item: item.name.lower() == name.lower())
        if removed is not None:
            self._history.push(("remove", removed))
        return removed

    def find_item(self, name):
        """Return the item with this name, or None."""
        return self._items.find(lambda item: item.name.lower() == name.lower())

    def undo(self):
        """Reverse the most recent add/remove. Returns (action, item) or None."""
        if self._history.is_empty():
            return None
        action, item = self._history.pop()
        if action == "add":
            self._items.remove(lambda candidate: candidate is item)
        else:
            self._items.append(item)        # a removed item returns at the end
        return action, item

    def items(self):
        """Return the cart contents as a list."""
        return self._items.to_list()

    def total(self):
        """Total cost of everything in the cart."""
        return sum(item.line_total() for item in self._items)

    def is_empty(self):
        return self._items.is_empty()
