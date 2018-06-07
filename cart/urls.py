from django.conf.urls import url, include
from cart import views


urlpatterns = [
    url(r'^$', views.CartDetailView.as_view(), name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAddView.as_view(), name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemoveView.as_view(), name='cart_remove'),
    url(r'^coupons/', include('coupons.urls', namespace='coupons')),
]
