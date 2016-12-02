from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from shop.recommender import Recommender


class CartAddView(FormView):
    form_class = CartAddProductForm

    def form_valid(self, form):
        cart = Cart(self.request)
        product_id = self.kwargs.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        cd = form.cleaned_data
        cart.add(product=product,
                      quantity=cd['quantity'],
                      update_quantity=cd['update'])
        return redirect('cart:cart_detail')


class CartRemoveView(View):

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = self.kwargs.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetailView(TemplateView):
    template_name = 'cart/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CartDetailView, self).get_context_data(**kwargs)
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'],
                         'update': True})
        context['cart'] = cart
        context['coupon_apply_form'] = CouponApplyForm()
        r = Recommender()
        cart_products = [item['product'] for item in cart]
        context['recommended_products'] = r.suggest_products_for(cart_products, 4)

        return context
