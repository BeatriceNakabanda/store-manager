class Product:
    """Product class defines the product sold by the store"""
    def __init__(self, product_id, product_name, date_added, price = int, quantity = int):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.date_added = date_added

    def serialize(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "price": self.price,
            "product_quantity": self.quantity,
            "date_added": self.date_added,
            }