"""Supermarket checkout demonstration.

Shows how the three data structures work together:
  Singly Linked List -> the items in each customer's cart
  Stack              -> undo history of cart actions
  Queue              -> customers waiting to be served

  SEN 306 - Software Construction 
Name: TRACY URIRINOGHENE GBAGBEKE
MAT NUMBER : 2024/C/SENG/0861
301788020
Date: 11-11-2026
"""

from cart import ShoppingCart
from checkout import CheckoutDesk
from item import Item


def show_cart(cart):
    """Print the current contents of a cart."""
    print(f"  {cart.owner}'s cart:")
    if cart.is_empty():
        print("    (empty)")
    for item in cart.items():
        print(f"    - {item}")
    print(f"    Total so far: NGN {cart.total():,.2f}")


def main():
    # 1. Build carts: adding items to a linked list (each action goes on the undo stack)
    print("== Step 1: customers fill their carts ==")
    ada = ShoppingCart("Ada")
    ada.add_item(Item("Rice (5kg)", 9500, 1))
    ada.add_item(Item("Bread", 1200, 2))
    ada.add_item(Item("Milk", 2300, 1))
    ada.add_item(Item("Eggs (crate)", 3800, 1))
    show_cart(ada)

    bayo = ShoppingCart("Bayo")
    bayo.add_item(Item("Bottled water", 400, 6))
    bayo.add_item(Item("Soap", 750, 3))

    chi = ShoppingCart("Chi")
    chi.add_item(Item("Noodles", 300, 10))

    # 2. Retrieve, delete, and undo
    print("\n== Step 2: retrieving, deleting and undoing ==")
    found = ada.find_item("milk")
    print(f"  Search for 'milk': {found}")
    removed = ada.remove_item("Bread")
    print(f"  Removed: {removed}")
    print(f"  Remove 'Pizza' (not in cart): {ada.remove_item('Pizza')}")
    show_cart(ada)

    action, item = ada.undo()
    print(f"\n  Undo -> reversed a '{action}' of {item.name}")
    show_cart(ada)
    action, item = ada.undo()
    print(f"\n  Undo -> reversed a '{action}' of {item.name}")
    show_cart(ada)

    # 3. Customers join the queue and are processed first-come, first-served
    print("\n== Step 3: customers queue at the checkout ==")
    desk = CheckoutDesk()
    for cart in (ada, bayo, chi):
        desk.join_queue(cart)
        print(f"  {cart.owner} joined the queue. Waiting: {desk.customers_waiting()}")
    print(f"  Next in line: {desk.next_in_line()}")

    print("\n== Step 4: serving customers (FIFO) ==")
    while desk.customers_waiting() > 0:
        print(desk.serve_next())
        print()

    print(f"Customers served: {desk.customers_served}")
    print(f"Total sales: NGN {desk.sales_total:,.2f}")
    print(f"Serve when nobody is waiting: {desk.serve_next()}")


if __name__ == "__main__":
    main()
