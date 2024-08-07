from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

# from django.views.generic import TemplateView

urlpatterns = [
    path("", include("bakery_app.pages.urls", namespace="inicio")),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("bakery_app.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # APP PATHS
    path("product/", include("bakery_app.product.urls", namespace="product")),
    path("inventario/", include("bakery_app.inventario.urls", namespace="inventario")),
    path("dashboard/", include("bakery_app.dashboard.urls", namespace="dashboard")),
    path("venta/", include("bakery_app.venta.urls", namespace="venta")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # Importar Media Files
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
