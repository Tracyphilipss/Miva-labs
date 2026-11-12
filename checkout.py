"""CheckoutDesk: serves waiting customers in the order they arrived (queue)."""

from queue_structure import Queue


def build_receipt(cart):
    """Return a printable receipt (text) for a cart."""
    lines = [f"Receipt for {cart.owner}"]
    for item in cart.items():
        lines.append(f"  {item}  =  NGN {item.line_total():,.2f}")
    lines.append(f"  TOTAL: NGN {cart.total():,.2f}")
    return "\n".join(lines)


class CheckoutDesk:
    """A till where customers wait in a queue and are served one at a time."""

    def __init__(self):
        self._waiting = Queue()
        self.customers_served = 0
        self.sales_total = 0.0

    def join_queue(self, cart):
        """A customer (with their cart) joins the back of the queue."""
        self._waiting.enqueue(cart)

    def next_in_line(self):
        """Name of the customer at the front, or None if nobody is waiting."""
        if self._waiting.is_empty():
            return None
        return self._waiting.peek().owner

    def customers_waiting(self):
        return self._waiting.size()

    def serve_next(self):
        """Serve the customer at the front. Returns the receipt, or None if idle."""
        if self._waiting.is_empty():
            return None
        cart = self._waiting.dequeue()
        self.customers_served += 1
        self.sales_total += cart.total()
        return build_receipt(cart)
