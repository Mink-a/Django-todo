from django.urls import path
from . import views

urlpatterns = [
    path("", views.allTodos, name="all-todos"),
    path("delete/<int:id>", views.deleteTodo, name="delete-todo"),
    path("update/<int:id>", views.updateTodo, name="update-todo")
]
