from django.urls import path

from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('new/<int:item_pk>', views.new_conversation, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
]