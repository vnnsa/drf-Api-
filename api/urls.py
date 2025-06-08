from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    TaskViewSet,
    SubmissionViewSet,
    home_view,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('home/', home_view, name='home'),
    path('', include(router.urls)),
]



# This code sets up the URL routing for the API, including a home view and routes for user, task, and submission endpoints.
# It uses Django's `path` and `include` functions to define the URL patterns,
# The `include` function is used to include the routes for the viewsets in the main URL
# configuration, allowing for a clean and organized URL structure.
# The `home_view` function provides a simple welcome message for the API.
# This structure allows for easy expansion and maintenance of the API as new features or endpoints are added.
# The `urlpatterns` list defines the URL patterns for the API, mapping URLs to their corresponding views.   
# The `path` function is used to define the URL patterns, and the `include` function allows for modular URL routing.
# The `DefaultRouter` from Django REST Framework automatically generates the necessary URL patterns for the viewsets,
# and the `include` function is used to include these patterns in the main URL configuration.       
# This modular approach allows for easy expansion and maintenance of the API as new features or endpoints are added.

# The API endpoints can be accessed at the following URLs:
# api/users/
# api/tasks/
# api/submissions/
# api/home/

