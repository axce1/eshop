from django.shortcuts import redirect
from django.utils import timezone

from .forms import CouponApplyForm
from .models import Coupon
from django.views.generic.base import View


# formview use
class CouponApplyView(View):

    def post(self, request, *args, **kwargs):
        form = CouponApplyForm(request.POST)
        now = timezone.now()

        if form.is_valid():
            cd = form.cleaned_data
            try:
                coupon = Coupon.objects.get(code__iexact=cd['code'],
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
                request.session['coupon_id'] = coupon.id
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
            return redirect('cart:cart_detail')
