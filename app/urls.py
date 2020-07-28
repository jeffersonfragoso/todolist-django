from app.views import TodoDetailChangeAndDelete, TodoListAndCreate

from django.urls import path

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view())
]
