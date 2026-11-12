"""Item: one product line in a shopping cart."""


class Item:
    """A product with a name, a unit price and a quantity."""

    def __init__(self, name, price, quantity=1):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def line_total(self):
        """Price multiplied by quantity."""
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} x{self.quantity} @ NGN {self.price:,.2f}"
