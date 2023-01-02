from django.urls import path
from bankapp import views

app_name='bankapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('create/',views.create,name='create'),

]
