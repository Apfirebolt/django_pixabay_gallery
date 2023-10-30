from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_gallery import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('api-schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api-docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

