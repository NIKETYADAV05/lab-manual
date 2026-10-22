
# Practical 5: Shopping Cart using Classes and Objects


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            return None

        if name in self.items:
            self.items[name][1] += quantity
        else:
            self.items[name] = [price, quantity]

        print(name, "added to cart.")
        return self.items[name]

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(name, "removed from cart.")
            return True

        print("Item not found in cart.")
        return False

    def calculate_total(self):
        total = 0

        for price, quantity in self.items.values():
            total += price * quantity

        return total

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return None

        print("\n--- Shopping Cart ---")

        for name, details in self.items.items():
            price, quantity = details
            print(name, "- Price:", price,
                  "Quantity:", quantity,
                  "Subtotal:", price * quantity)

        print("Total Price:", self.calculate_total())
        return self.calculate_total()


def main():
    cart = ShoppingCart()

    while True:
        print("\n===== Shopping Cart Menu =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Cart")
        print("4. Calculate Total")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")

            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter quantity: "))

                cart.add_item(name, price, quantity)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "2":
            name = input("Enter product name to remove: ")
            cart.remove_item(name)

        elif choice == "3":
            cart.display_cart()

        elif choice == "4":
            print("Total Price:", cart.calculate_total())

        elif choice == "5":
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
