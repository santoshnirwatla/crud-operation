
from django.urls import path,include
from omesapp import views

urlpatterns = [
  
    path('index/',views.Index),
    path('all/',views.All_view),
    path('add/',views.Add_view),
    path('del/',views.Delete_view),
    path('delete/<int:id>/',views.Delete),
    path('updt/',views.Update_view),
    path('update/<int:id>/',views.Update),
    path('fil/',views.Filter),
]
