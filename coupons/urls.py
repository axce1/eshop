from django.conf.urls import url
from coupons import views


urlpatterns = [
    url(r'^apply/$', views.CouponApplyView.as_view(), name='apply'),
]
