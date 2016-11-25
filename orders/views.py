from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Product


class OrderCreateForm(FormView):
    form_class = OrderCreateForm
    template_name = 'orders/order/create.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        print(cart)
        order = form.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product = item['product'],
                price = item['price'],
                quantity = item['quantity']
            )
        cart.clear()

        return render(self.request,
                      'orders/order/created.html',
                      {'order': order})
