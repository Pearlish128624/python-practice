import os
from collections import defaultdict
from typing import Dict, List
import re

class Product:
    #產品類
    def __init__(self, product_id: str, name: str, price: float):
        self.id = product_id
        self.name = name
        self.price = price

class ProductCatalog:
    """產品目錄類"""
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self._load_products()

    def _load_products(self):
        with open('source/produce.txt', 'r') as f:
            for line in f:
                product_id, name, price = line.strip().split(',')
                self.products[product_id] = Product(product_id, name, float(price))

    def get_product(self, product_id: str) -> Product:
        return self.products[product_id]

class OrderItem:
    """訂單項目類"""
    def __init__(self, product_id: str, quantity: int):
        self.product_id = product_id
        self.quantity = quantity

class Order:
    """訂單類"""
    def __init__(self, customer: str, items: Dict[str, int]):
        self.customer = customer
        self.items = {
            product_id: OrderItem(product_id, quantity)
            for product_id, quantity in items.items()
        }
        self.total = 0.0

    def format_order(self) -> str:
        items_str = ' '.join(
            f"{item.quantity}{product_id}"
            for product_id, item in sorted(self.items.items())
        )
        return f"{self.customer}: {items_str} ${self.total:.0f}"

class DiscountRule:
    """折扣規則"""
    def apply(self, order: Order, catalog: ProductCatalog) -> float:
        raise NotImplementedError

class Over500DiscountRule(DiscountRule):
    """訂單超過$500打85折"""
    def apply(self, order: Order, catalog: ProductCatalog) -> float:
        total = sum(catalog.get_product(item.product_id).price * item.quantity 
                    for item in order.items.values())
        return total * 0.15 if total > 500 else 0

class PursePenRule(DiscountRule):
    """每購買一個包包(B)，就贈送一支鋼筆(A)"""
    def apply(self, order: Order, catalog: ProductCatalog) -> float:
        b_item = order.items.get('B', OrderItem('B', 0))
        b_quantity = b_item.quantity
        if b_quantity <= 0:
            return 0
        
        # 每個包包送一支鋼筆
        free_pen_count = b_quantity
        discount = catalog.get_product('A').price * free_pen_count
        
        # 如果訂單中已經有購買的A，這裡直接累加免費贈送的數量
        if 'A' in order.items:
            order.items['A'].quantity += free_pen_count
        else:
            order.items['A'] = OrderItem('A', free_pen_count)
            
        return discount
class ComboDiscountRule(DiscountRule):
    """當同時購買 D、E、F 時，F 的價格變成70"""
    def apply(self, order: Order, catalog: ProductCatalog) -> float:
        # 取得各商品的數量，若未購買則數量為0
        d_quantity = order.items.get('D', OrderItem('D', 0)).quantity
        e_quantity = order.items.get('E', OrderItem('E', 0)).quantity
        f_quantity = order.items.get('F', OrderItem('F', 0)).quantity
        
        # 計算可組成的完整套裝數量
        combo_count = min(d_quantity, e_quantity, f_quantity)
        
        if combo_count > 0:
            original_f_price = catalog.get_product('F').price
            # 只有在原始 F 的價格大於 70 時，才有折扣
            discount_per_combo = original_f_price - 70 if original_f_price > 70 else 0
            return discount_per_combo * combo_count
        return 0

class KeychainDiscountRule(DiscountRule):
    """兩個鑰匙圈95折"""
    def apply(self, order: Order, catalog: ProductCatalog) -> float:
        if 'C' in order.items:
            pairs = order.items['C'].quantity // 2
            return 2 * catalog.get_product('C').price * 0.05 * pairs
        return 0

class BillingSystem:
    """帳單系統"""
    def __init__(self):
        self.catalog = ProductCatalog()
        self.orders: List[Order] = []
        self.rules = [
            Over500DiscountRule(),
            PursePenRule(),
            ComboDiscountRule(),
            KeychainDiscountRule()
        ]
        self._load_orders()

    def _load_orders(self):
        """從record_1.txt加載訂單信息"""
        with open('source/record_1.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                    
                customer, items = line.split(': ')
                # 解析商品數量
                item_counts = {}
                for item_info in items.split():
                    matches = re.findall(r'(\d+)([A-Z])', item_info)  # 使用正則表達式提取數量和產品ID
                    for count, product_id in matches:
                        item_counts[product_id] = int(count)  # 將數量轉換為整數
                
                order = Order(customer, item_counts)
                self._calculate_total(order)
                self.orders.append(order)

    def _calculate_total(self, order: Order):
        """計算訂單金額並應用優惠規則"""
        # 計算原始總價
        original_total = sum(
            self.catalog.get_product(item.product_id).price * item.quantity
            for item in order.items.values()
        )
        
        # 應用所有折扣規則
        total_discount = sum(
            rule.apply(order, self.catalog)
            for rule in self.rules
        )
        
        # 計算最終總價，確保不低於0
        order.total = max(0, original_total - total_discount)

    def get_grouped_orders(self) -> Dict[str, Order]:
        """
        聚合同一客戶的訂單:
          - 將相同客戶的訂單商品數量累加
          - 將總價也累加
        回傳一個 dict，key 為 customer name，value 為聚合後的 Order
        """
        grouped_orders: Dict[str, Order] = {}
        for order in self.orders:
            if order.customer not in grouped_orders:
                # 深拷貝一份訂單資料
                new_order = Order(order.customer, {})
                for product_id, order_item in order.items.items():
                    new_order.items[product_id] = OrderItem(product_id, order_item.quantity)
                new_order.total = order.total
                grouped_orders[order.customer] = new_order
            else:
                grouped_order = grouped_orders[order.customer]
                # 累加每個產品的數量
                for product_id, order_item in order.items.items():
                    if product_id in grouped_order.items:
                        grouped_order.items[product_id].quantity += order_item.quantity
                    else:
                        grouped_order.items[product_id] = OrderItem(product_id, order_item.quantity)
                # 累加總價
                grouped_order.total += order.total
        return grouped_orders

    def save_summary(self):
        """保存訂單匯總到bills.txt"""
        grouped_orders = self.get_grouped_orders()
        with open('source/bills.txt', 'w', encoding='utf-8') as f:
            f.write("訂單匯總:\n")
            f.write("-" * 50 + "\n")
            for customer in sorted(grouped_orders):
                f.write(grouped_orders[customer].format_order() + "\n")

    def print_summary(self):
        """打印所有訂單匯總"""
        grouped_orders = self.get_grouped_orders()
        print("\n訂單匯總:")
        print("-" * 50)
        for customer in sorted(grouped_orders):
            print(grouped_orders[customer].format_order())
        # 同時保存到文件
        self.save_summary()

        
def main():
    try:
        billing_system = BillingSystem()
        billing_system.print_summary()
    except FileNotFoundError as e:
        print(f"錯誤: {e}")
    except Exception as e:
        print(f"發生未預期的錯誤: {e}")

if __name__ == "__main__":
    main()
