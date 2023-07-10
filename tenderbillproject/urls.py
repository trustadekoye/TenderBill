from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

app_name = 'tenderbillproject'

urlpatterns = [
    path('create_quote/', views.create_quotation, name='create_quotation'),
    path('', RedirectView.as_view(url='/tenderbill/tenderbillproject/templates/create_quote/'), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)