from django.urls import path
from .views import CommentsView

urlpatterns = [
    path('post/<str:slug>/add_comment/', CommentsView.as_view())
]