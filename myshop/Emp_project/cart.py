from decimal import Decimal
from django.conf import settings
from shop.models import Product
from cupons.models import Cupon


class Emp_project (object):
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # Сохраняем корзину пользователя в сессию


    # Добавление товара в корзину пользователя или обновление количеста товара
    def add_EmployeeToProject(self, Order, update_employee=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[Order] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_employee:
            self.cart[Order]['quantity'] = quantity
        else:
            self.cart[Order]['quantity'] += quantity
        self.save()

    def get_priority(self, priority, update_priority=False):
        priority = str(priority)
        if priority not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_priority:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Сохранение данных в сессию
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True

    def remove_EmployeeFromProject(self, Order):
        Order_id = str(Order)
        if product_id in self.cart:
            del self.cart[Order]
            self.save()

    # Итерация по товарам
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
