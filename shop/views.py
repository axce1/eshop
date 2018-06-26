from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from cart.forms import CartAddProductForm
from .models import Category, Product
from .recommender import Recommender


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category'] = None
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(available=True)
        category_slug = self.kwargs.get("slug")
        if category_slug:
            context['category'] = get_object_or_404(Category, slug=category_slug)
            context['products'] = Product.objects.filter(category=context['category'], available=True)
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm
        r = Recommender()
        context['recommended_products'] = r.suggest_products_for([self.get_object()], 4)
        return context

    def get_object(self):
        return get_object_or_404(Product,
                                 id=self.kwargs.get("id"),
                                 slug=self.kwargs.get("slug"),
                                 available=True)
