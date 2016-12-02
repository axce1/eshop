from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


class OrderCreateForm(FormView):
    form_class = OrderCreateForm
    template_name = 'orders/order/create.html'

    def dispatch(self, request, *args, **kwargs):
        cart = Cart(self.request)
        if not cart.cart:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save(commit=False)
        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.coupon.discount
        order.save()
        for item in cart:
            print(item['product'])
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()

        # start task
        order_created.delay(order.id)
        self.request.session['order_id'] = order.id

        return redirect(reverse('payment:process'))

