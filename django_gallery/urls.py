from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_gallery import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)