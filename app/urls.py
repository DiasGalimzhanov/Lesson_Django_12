from django.urls import path
from .views import PersonList, PersonCreate, PersonUpdate, PersonDelete, PersonDetail

urlpatterns = [
    path("", PersonList.as_view(), name="home"),
    path("create/", PersonCreate.as_view(), name="create"),
    path("update/<int:pk>/", PersonUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", PersonDelete.as_view(), name="delete"),
    path("detail/<int:pk>/", PersonDetail.as_view(), name="detail"),
]

