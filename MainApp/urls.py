from django.urls import path
from . import views 
app_name = 'main'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('done/<int:pk>',views.done,name = 'done'),
    path('notdone/<int:pk>',views.notdone,name = 'notdone'),
    path('add/',views.add,name = 'add'),
    path('/delete/<int:pk>',views.delete,name = 'delete')
]
