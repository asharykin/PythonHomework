class Product:
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount: int):
        self.quantity += amount

    def decrease_quantity(self, amount: int):
        if amount > self.quantity:
            raise ValueError("Недостаточно единиц товара на складе для удаления")
        self.quantity -= amount

    def get_total_value(self):
        return self.quantity * self.price


class Warehouse:
    def __init__(self):
        self.products = []

    def add_new_product(self, product: Product):
        for existing_product in self.products:
            if existing_product.name == product.name:
                raise ValueError(f"Товар '{product.name}' уже есть на складе")
        self.products.append(product)
        print(f"Новый товар '{product.name}' добавлен на склад в количестве {product.quantity} единиц")

    def add_existing_product(self, product_name: str, amount: int):
        for existing_product in self.products:
            if existing_product.name == product_name:
                existing_product.increase_quantity(amount)
                print(f"На склад добавлено {amount} единиц товара '{product_name}'")
                return
        raise ValueError(f"Товар '{product_name}' не найден на складе")

    def remove_existing_product(self, product_name: str, amount: int):
        for existing_product in self.products:
            if existing_product.name == product_name:
                existing_product.decrease_quantity(amount)
                print(f"Со склада удалено {amount} единиц товара '{product_name}'")
                return
        raise ValueError(f"Товар '{product_name}' не найден на складе")

    def get_total_value(self):
        return sum(product.get_total_value() for product in self.products)


class Seller:
    def __init__(self, name: str):
        self.name = name
        self.sales_report = []

    def sell_product(self, warehouse: Warehouse, product_name: str, amount: int):
        for product in warehouse.products:
            if product.name == product_name:
                product.decrease_quantity(amount)
                revenue = amount * product.price
                report_str = f"Продавец {self.name} продал {amount} единиц товара '{product.name}' на сумму {revenue}"
                self.sales_report.append(report_str)
                print(report_str)
                return
        raise ValueError(f"Товар '{product_name}' не найден на складе")

    def get_sales_report(self):
        return self.sales_report
