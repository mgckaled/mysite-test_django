"""
mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# declarações de URLs para este projeto Django; um “índice” de seu 
# site movido a Django

"""
A função path() são passado quatro argumentos, dois obrigatórios: route e view, 
e dois opcionais: kwargs, e name.

**argumento de path(): route¶
route é uma string contento uma descrição de uma URL. Quando processa uma requisição, 
o Django começa pela primeira descrição, e vai descendo a lista, comparando a URL 
requisitada com cada descrição até que encontre uma que combine.

** argumento de path(): view¶
Quando o Django encontra uma descrição que combina, chama a função view especificada 
com um objeto HttpRequest como primeiro argumento e qualquer valor “capturado” da 
rota como argumentos keyword.

**argumento de path(): kwargs¶
Argumentos nomeados arbitrários podem ser passadas em um dicionário para a view de 
destino.

**argumento de path(): name
Nomear sua URL permite que você referencie ela de forma inequívoca de qualquer 
lugar no Django especialmente nos templates. Este poderoso recurso permite que você 
faça alterações globais nos padrões de URL de seu projeto enquanto modifica um 
único arquivo.

"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
