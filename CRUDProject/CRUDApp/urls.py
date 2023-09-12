
from django.urls import path
from .views import CreateUserView,UserRetrieveUpdateDestroyView
urlpatterns = [

    path('', CreateUserView.as_view(),name="create"),
    path('/<str:identifier>', UserRetrieveUpdateDestroyView.as_view(),name="RUD")
]
