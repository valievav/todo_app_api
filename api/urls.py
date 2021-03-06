from django.urls import path
from . import views

urlpatterns = [
    # Todos
    path('todos/', views.TodoList.as_view()),
    path('todos/current/', views.TodoCurrentListCreate.as_view()),
    path('todos/completed/', views.TodoCompletedList.as_view()),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete/', views.TodoCompleteUpdate.as_view()),

    # Auth
    path('signup/', views.signup),  # creates new user and generates its token
    path('login/', views.login),  # returns token if exists or generates new one
]
