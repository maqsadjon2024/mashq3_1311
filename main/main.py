# 3-misol
class Product:

    def __init__(self, name: str, price: float, stock_quantity: int):
        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity
        
    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock_quantity(self) -> int:
        return self.__stock_quantity
    
    def _set_stock_quantity_internal(self, new_quantity: int) -> bool:
        if new_quantity >= 0:
            self.__stock_quantity = new_quantity
            return True
        return False


class InventoryManager:

    def __init__(self):
        self.products: dict[str, Product] = {}

    def add_product(self, product: Product):
        self.products[product.get_name()] = product

    def get_product(self, name: str) -> Product | None:
        return self.products.get(name)

    def purchase(self, product_name: str, quantity: int) -> bool:
        product = self.get_product(product_name)

        if not product:
            print(f"**Xatolik:** '{product_name}' topilmadi.")
            return False

        current_stock = product.get_stock_quantity()

        if current_stock == 0:
            print(f"**Sotuvda yo'q:** '{product_name}' zaxirasi tugagan.")
            return False

        if quantity > current_stock:
            print(f"**Diqqat:** '{product_name}' uchun yetarli zaxira yo'q. Bor: {current_stock}.")
            return False

        new_stock = current_stock - quantity

        if product._set_stock_quantity_internal(new_stock):
            print(f"Xarid muvaffaqiyatli: {product_name} dan {quantity} dona sotildi.")
            print(f"   Qolgan zaxira: {new_stock}")
            return True

        return False


print("--- 🛒 Onlayn Inventar Yechimi ---")

kitob = Product("Dasturlash Asoslari", 75000, 5)
qalam = Product("Avtomatik Qalam", 5000, 1)
ruchka = Product("Gel Ruchka", 10000, 0)

manager = InventoryManager()
manager.add_product(kitob)
manager.add_product(qalam)
manager.add_product(ruchka)

print(
    f"\nBoshlang'ich zaxiralar: Kitob: {kitob.get_stock_quantity()}, Qalam: {qalam.get_stock_quantity()}, Ruchka: {ruchka.get_stock_quantity()}")

print("\n--- Xaridlar ---")

manager.purchase("Dasturlash Asoslari", 2)
manager.purchase("Avtomatik Qalam", 1)
manager.purchase("Avtomatik Qalam", 1)
manager.purchase("Gel Ruchka", 1)

print(
    f"\nYakuniy zaxiralar: Kitob: {kitob.get_stock_quantity()}, Qalam: {qalam.get_stock_quantity()}, Ruchka: {ruchka.get_stock_quantity()}")
