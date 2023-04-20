# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.urls import re_path

from www.permissions.views import (
    UserPermListView, UserPermUpdateView,
    GroupPermListView, GroupPermUpdateView, GroupPermCreateView,
    UriGroupPermListView, UriGroupPermUpdateView, UriGroupPermCreateView,
)


urlpatterns = [
    # user permission
    re_path(r'^$', login_required(UserPermListView.as_view()), name="index"),
    re_path(r'^users/$', login_required(UserPermListView.as_view()), name="users"),
    re_path(r'^user/update/$', login_required(UserPermUpdateView.as_view()), name="user_update"),

    # group permission
    re_path(r'^groups/$', login_required(GroupPermListView.as_view()), name="groups"),
    re_path(r'^group/update/$', login_required(GroupPermUpdateView.as_view()), name="group_update"),
    re_path(r'^group/create/$', login_required(GroupPermCreateView.as_view()), name="group_create"),

    # uri group permission
    re_path(r'^uri_groups/$', login_required(UriGroupPermListView.as_view()), name="uri_groups"),
    re_path(r'^uri_group/update/$', login_required(UriGroupPermUpdateView.as_view()), name="uri_group_update"),
    re_path(r'^uri_group/create/$', login_required(UriGroupPermCreateView.as_view()), name="uri_group_create"),
]
