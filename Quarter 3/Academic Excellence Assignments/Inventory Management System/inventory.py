import json
from datetime import datetime

# Custom exceptions
class InventoryError(Exception):
    """Base exception for inventory errors"""
    pass

class OutOfStockError(InventoryError):
    """Raised when trying to sell more than available stock"""
    def __init__(self, product_name, requested, available):
        super().__init__(f"{product_name} is out of stock. Tried to sell {requested}, only {available} available.")

class DuplicateProductIDError(InventoryError):
    """Raised when a product with an existing ID is added"""
    def __init__(self, product_id):
        super().__init__(f"Product ID '{product_id}' already exists in inventory.")

# Base Product class
class Product:
    """Generic product with id, name, price, and quantity"""
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price} - {self.quantity} in stock"

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Restock amount must be positive")
        self.quantity += amount

    def sell(self, amount):
        if amount <= 0:
            raise ValueError("Sell amount must be positive")
        if amount > self.quantity:
            raise OutOfStockError(self.name, amount, self.quantity)
        self.quantity -= amount

    def get_value(self):
        return self.price * self.quantity

# Electronics subclass
class Electronics(Product):
    def __init__(self, product_id, name, price, quantity, warranty, brand):
        super().__init__(product_id, name, price, quantity)
        self.warranty = warranty  # years
        self.brand = brand

    def __str__(self):
        return f"Electronics: {self.name} by {self.brand} - ${self.price} - {self.warranty}yr warranty - {self.quantity} in stock"

# Grocery subclass
class Grocery(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        if isinstance(expiry_date, str):
            self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
        else:
            self.expiry_date = expiry_date

    def is_expired(self):
        return datetime.today().date() > self.expiry_date

    def __str__(self):
        status = " (EXPIRED)" if self.is_expired() else ""
        return f"Grocery: {self.name}{status} - ${self.price} - Expires: {self.expiry_date} - {self.quantity} in stock"

# Clothing subclass
class Clothing(Product):
    def __init__(self, product_id, name, price, quantity, size, material):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.material = material

    def __str__(self):
        return f"Clothing: {self.name} - {self.size} - {self.material} - ${self.price} - {self.quantity} in stock"

# Inventory management class
class Inventory:
    def __init__(self):
        self.products = {}  # {product_id: Product}

    def add_product(self, product):
        if product.product_id in self.products:
            raise DuplicateProductIDError(product.product_id)
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        self.products.pop(product_id, None)

    def find_product(self, product_id):
        return self.products.get(product_id)

    def search_by_name(self, name):
        return [p for p in self.products.values() if name.lower() in p.name.lower()]

    def list_all_products(self):
        return list(self.products.values())

    def sell_product(self, product_id, quantity):
        product = self.find_product(product_id)
        if not product:
            raise KeyError(f"Product ID '{product_id}' not found.")
        product.sell(quantity)

    def restock_product(self, product_id, quantity):
        product = self.find_product(product_id)
        if not product:
            raise KeyError(f"Product ID '{product_id}' not found.")
        product.restock(quantity)

    def total_value(self):
        return sum(p.get_value() for p in self.products.values())

    def remove_expired_products(self):
        expired_ids = [pid for pid, p in self.products.items() if isinstance(p, Grocery) and p.is_expired()]
        for pid in expired_ids:
            self.products.pop(pid)

    def save_to_file(self, filename="inventory.json"):
        data = []
        for p in self.products.values():
            d = p.__dict__.copy()
            d['__class__'] = p.__class__.__name__
            if isinstance(p, Grocery):
                d['expiry_date'] = p.expiry_date.isoformat()
            data.append(d)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, file):
        if hasattr(file, 'read'):  # uploaded file
            data = json.load(file)
        else:
            with open(file, 'r') as f:
                data = json.load(f)
        self.products.clear()
        for d in data:
            cls = d.pop('__class__', 'Product')
            pid = d.pop('product_id', None)
            if cls == 'Electronics':
                obj = Electronics(product_id=pid, **d)
            elif cls == 'Grocery':
                obj = Grocery(product_id=pid, **d)
            elif cls == 'Clothing':
                obj = Clothing(product_id=pid, **d)
            else:
                obj = Product(product_id=pid, **d)
            self.products[pid] = obj
# End of inventory.py
