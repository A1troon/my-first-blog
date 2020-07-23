
from django.urls import path
from . import views
urlpatterns = [
    path('', views.first),
    path('123', views.get_student),
    path('456', views.second),
    path('789',views.Upload_file),
    path('clear1', views.clear_interest),
    path('clear2', views.clear_student),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('create/', views.create),
    path('addmoreinteres/<int:id>/',views.add_more_interes),
    path('search',views.search),
    path('vkparsing',views.vk)

]