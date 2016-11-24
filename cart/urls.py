from django.conf.urls import url
from . import views


urlpatterns = [
    # TODO empty index cart url dont work
    url(r'^cart/$', views.CartDetailView.as_view(), name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAddView.as_view(), name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemoveView.as_view(), name='cart_remove'),
]