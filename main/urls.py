from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contato, name='contato'),
    # O "$" no fim da string do endereço da pagina indica
    # o fim do endereço. Se alguem escrever algo mais alí
    # não funcionara. É uma boa pratica para segurança. Me parece...
]
