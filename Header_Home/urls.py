from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    # O "$" no fim da string do endereço da pagina indica
    # o fim do endereço. Se alguem escrever algo mais alí
    # não funcionara. É uma boa pratica para segurança. Me parece...

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
