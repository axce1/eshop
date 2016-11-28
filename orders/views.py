from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderCreateForm(FormView):
    form_class = OrderCreateForm
    template_name = 'orders/order/create.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product = item['product'],
                price = item['price'],
                quantity = item['quantity']
            )
        cart.clear()

        self.request.session['order_id'] = order.id

        return redirect(reverse('payment:process'))

