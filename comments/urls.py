from django.urls import path
from .views import CommentsView

urlpatterns = [
    path('post/<str:slug>/add_comment/', CommentsView.as_view()),
    path('comment/<int:pk>/edit_comment/', CommentsView.as_view()),
    path('comment/<int:pk>/delete_comment/', CommentsView.as_view()),
]