# coding=utf8

from django.urls import reverse_lazy, re_path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

from www.risk_auth.views import Home
from www.risk_auth.views import risk_login, risk_logout

urlpatterns = [
    re_path(r'^$', login_required(Home.as_view()), name='home'),
    re_path(r'^home/$', RedirectView.as_view(url=reverse_lazy('risk_auth:home'), permanent=True)),
    re_path(r'^accounts/login/$', risk_login, name="risk_login"),
    re_path(r'^accounts/logout/$', risk_logout, name="risk_logout"),
]
