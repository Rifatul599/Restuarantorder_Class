class RestaurantOrder:
    def __init__(self):
        self.order={}
        self.total_amount=0
        self.completed=False

    def add_item(self,item,quantity,price):
        if item in self.order:
            self.order[item]["quantity"]+= quantity
        else:
            self.order[item]={"quantity":quantity,"price":price}
            print(f"Added {quantity} of {item} to the order.")

    def remove_item(self,item):
        if item in self.order:
            del self.order[item]
            print(f"Removed [item] from the order.")
        else:
            print(f"[item] not found in order.")

    def get_total_amount(self):
        self.total_amount=sum(details['quantity']*details['price'] for details in self.order.values())
        return self.total_amount

    def apply_discount(self,percentage):
        discount_amount=self.get_total_amount()*(percentage/100)
        self.total_amount-=discount_amount
        print(f"Discount of {percentage}% applied: {discount_amount:.2f} off.")

    def generate_receipt(self):
        if not self.order:
            print("Your order is empty.")
            return
        print("Receipt:")
        for item,details in self.order.items():
            item_total=details["quantity"]*details["price"]
            print(f"{item}:{details['quantity']*details['price']:.2f}={item_total:.2f}")
        print(f"Total_amount:{self.get_total_amount():.2f}")

    def complete_order(self):
        if not self.order:
            print("No items in the order to complete.")
            return
        self.generate_receipt()
        print("Order completed:Thank you for dining with us.")
        self.order.clear()
        self.total_amount=0
        self.completed=True

order=RestaurantOrder()

order.add_item("Burger",2,200)
order.add_item("Pizza",2,2400)
order.generate_receipt()
order.complete_order()
order.apply_discount(20)
order.remove_item("Burger")