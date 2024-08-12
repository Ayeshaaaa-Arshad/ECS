from django.shortcuts import render,redirect
from django.http import HttpResponse
from orders.models import Order,AddToCart,OrderItem
from shops.models import Shop
from products.models import Product
from users.models import Customer, User

def create_order(request):
    if request.method == 'POST':
        customer_user_id = request.POST.get('customer_user')
        customer_first_name = request.POST.get('customer_first_name')
        customer_last_name = request.POST.get('customer_last_name')
        customer_username = request.POST.get('customer_username')
        customer_email = request.POST.get('customer_email')
        customer_phone_number = request.POST.get('customer_phone_number')
        customer_address = request.POST.get('customer_address')

        shop_id = request.POST.get('shop_id')
        shop_name = request.POST.get('shop_name')
        shop_address = request.POST.get('shop_address')

        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')

        cart_customer_id = request.POST.get('cart_customer')
        cart_product_id = request.POST.get('cart_product')
        cart_quantity = request.POST.get('cart_quantity')

        order_item_order_id = request.POST.get('order_item_order')
        order_item_cart_id = request.POST.get('order_item_cart')
        order_item_quantity = request.POST.get('order_item_quantity')

        order_customer_id = request.POST.get('order_customer')
        order_shop_id = request.POST.get('order_shop')
        order_date = request.POST.get('order_date')

        try:
            # Create or Update Shop
            shop, created = Shop.objects.update_or_create(
                id=shop_id,
                defaults={'name': shop_name, 'address': shop_address}
            )

            # Create or Update Product
            product, created = Product.objects.update_or_create(
                id=product_id,
                defaults={'name': product_name, 'price': product_price}
            )

            # Create or Update Customer
            user, created = User.objects.update_or_create(
                id=customer_user_id,
                defaults={
                    'first_name': customer_first_name,
                    'last_name': customer_last_name,
                    'username': customer_username,
                    'email': customer_email,
                    'phone_number': customer_phone_number,
                    'address': customer_address
                }
            )
            customer, created = Customer.objects.update_or_create(user=user)

            # Create Order
            order = Order.objects.create(
                customer=customer,
                shop=shop,
                order_date=order_date
            )

            # Create AddToCart
            add_to_cart, created = AddToCart.objects.update_or_create(
                customer=customer,
                product=product,
                defaults={'quantity': cart_quantity}
            )

            # Create OrderItem
            OrderItem.objects.update_or_create(
                order=order,
                cart_item=add_to_cart,
                defaults={'quantity': order_item_quantity}
            )

            return redirect('core:index')

        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    return render(request, 'orders/order_form.html')


def delete_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if Order.objects.filter(id=order_id).exists():
            order = Order.objects.get(id=order_id)
            OrderItem.objects.filter(order=order).delete()
            order.delete()
            HttpResponse('Deleted Successfully')
        else:
            return HttpResponse('No order with this ID exists')
    return render(request, 'orders/delete_order.html')
