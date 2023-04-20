# coding=utf8
from django.urls import reverse_lazy, re_path
from django.views.generic import RedirectView

from www.menu.views import (
    UseridListView, MenuCreateView, MenuDestroyView, IpListView, UidListView, PayListView, PhoneListView,
    EventListView, EventCreateView, EventDestroyView
)

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy("menus:event_list"), permanent=True), name="menu_index"),

    re_path(r'^common_create/$', MenuCreateView.as_view(), name="create"),
    re_path(r'^common_delete/$', MenuDestroyView.as_view(), name="delete"),

    re_path(r'^event/list/$', EventListView.as_view(), name="event_list"),
    re_path(r'^event/create/$', EventCreateView.as_view(), name="event_create"),
    re_path(r'^event/destroy/$', EventDestroyView.as_view(), name="event_destroy"),

    re_path(r'^userid/list/$', UseridListView.as_view(), name="userid_list"),
    re_path(r'^ip/list/$', IpListView.as_view(), name="ip_list"),
    re_path(r'^uid/list/$', UidListView.as_view(), name="uid_list"),
    re_path(r'^pay/list/$', PayListView.as_view(), name="pay_list"),
    re_path(r'^phone/list/$', PhoneListView.as_view(), name="phone_list"),
]
