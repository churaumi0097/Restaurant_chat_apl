from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("",views.QueryView.as_view(),name = "query"),
    path("new_chat/", views.NewChatView.as_view(), name="new_chat"),
    path("memory/",views.Memory.as_view(),name = "memory")
]