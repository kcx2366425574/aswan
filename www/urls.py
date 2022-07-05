# coding=utf8
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include("risk_auth.urls")),
    url(r'permissions/', include("permissions.urls")),
    url(r'strategy/', include("strategy.urls")),
    url(r'menu/', include("menu.urls")),
    url(r'rule/', include("rule.urls")),
    url(r'config/', include("bk_config.urls")),
    url(r'log_manage/', include("log_manage.urls")),
]

# 用于线上时应移除此部分，动静分离
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    from django.views.defaults import (page_not_found, server_error,
                                       permission_denied)

    urlpatterns += [
        url(r'404/', page_not_found),
        url(r'500/', server_error),
        url(r'403/', permission_denied),
    ]
