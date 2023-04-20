# coding=utf8
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path(r'', include("risk_auth.urls")),
    path(r'permissions/', include("permissions.urls")),
    path(r'strategy/', include("strategy.urls")),
    path(r'menu/', include("menu.urls")),
    path(r'rule/', include("rule.urls")),
    path(r'config/', include("bk_config.urls")),
    path(r'log_manage/', include("log_manage.urls")),
]

# 用于线上时应移除此部分，动静分离
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    from django.views.defaults import (page_not_found, server_error,
                                       permission_denied)

    urlpatterns += [
        path(r'404/', page_not_found),
        path(r'500/', server_error),
        path(r'403/', permission_denied),
    ]
