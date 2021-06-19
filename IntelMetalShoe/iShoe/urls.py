from django.urls import include,path
from django.urls.resolvers import URLPattern
from iShoe import views

urlpatterns = [
    path('',views.shoelist,name='list'),
    path('manage/',views.shoemanage,name='manage')
]