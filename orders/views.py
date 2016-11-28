from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


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

        # start task
        order_created.delay(order.id)

        return render(self.request,
                      'orders/order/created.html',
                      {'order': order})
