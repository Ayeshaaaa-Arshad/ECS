from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Sum
from django.db.models import Count
from users.models import User, Customer, ShopAdmin, AppAdmin
from shops.models import Shop, Stock
from products.models import Product, ProductCategory
from orders.models import Order, AddToCart, OrderItem
from core.models import Shipment

class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'
    login_url = reverse_lazy('users:login')

"""Basic Queries:
Retrieve all products from a specific category.
Get all orders placed by a specific customer.
List all shops that stock a specific product.
Retrieve all products associated with a specific shop.
Get the shipment details for a specific order.

Complex Queries:

Get the total quantity of a specific product across all shops.
List all orders for a specific customer, including related order items and product details.
Retrieve all customers who have ordered a product from a specific category.
Get the top 5 products by total quantity sold across all orders.
List all shops with stock levels below a certain threshold for a specific product."""
def testingQueries(request):
    # Q1:Retrieve all products from a specific category.

    q1 = Product.objects.filter(category__name='Pizza')
    print("Query 1", q1)

    # Q2:Get all orders placed by a specific customer.

    q2 = Order.objects.filter(customer__user__first_name__icontains='a')
    print("Query 2", q2)

    # Q3: List all shops that stock a specific product.
    q3 = Shop.objects.filter(stock__product__category__name='Pizza')
    print("Query 3", q3)

    # Q4:Retrieve all products associated with a specific shop.
    q4 = Product.objects.filter(shop__name='Mr pizza')
    print("Query 4", q4)

    # Q5: Get the shipment details for a specific order.
    try:
        order = Order.objects.get(customer__user__first_name='Abdullah')
        q5 = Shipment(order=order)
        print("Query 5", q5)
    except Exception as e:
        print(e)

    # Part 2
    # Q6: Get the total quantity of a specific product across all shops.
    q6 = Shop.objects.annotate(num_product=Count("stock__product"))
    print("Query 6", q6[0].num_product)

    # Q7:List all orders for a specific customer, including related order items and product details.
    customer = Customer.objects.get(user__first_name__istartswith='Ali')

    orders = Order.objects.filter(customer=customer).prefetch_related(
        'orderitem_set__cart_item__product'
    )

    # Looping through the orders and access related order items and product details
    for order in orders:
        print(f"Order ID: {order.id}, Order Date: {order.order_date}")
        for order_item in order.orderitem_set.all():
            product = order_item.cart_item.product
            print(f"    Product: {product}, Quantity: {order_item.quantity}")

    # Q8:Retrieve all customers who have ordered a product from a specific category.
    category = ProductCategory.objects.get(name='Pizza')
    customer = Customer.objects.filter(order__orderitem__cart_item__product__category=category).distinct()
    print("Query 8", customer)

    # Q9:Get the top 3 products by total quantity sold across all orders.

    top_products = Product.objects.annotate(total_sold=Sum('addtocart__quantity')).order_by('-total_sold')[:3]
    print("Query 9",top_products)

    # Q10:List all shops with stock levels below a certain threshold for a all product.
    shops = Shop.objects.all()
    for shop in shops:
        stocks = Stock.objects.filter(shop=shop)
        for stock in stocks:
            if stock.quantity < 13:
                print(f'{shop.name} has shortage of Product {stock.product.category.name}')

    return HttpResponse(None)
