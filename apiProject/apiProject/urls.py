from api import views
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'notes', views.NoteViewSet)

urlpatterns = [

    # Admin url
    path(r'^admin/', admin.site.urls),

    # Page url
    path(r'^$', views.HomePageView.as_view()),
    path(r'^users/', views.UsersPageView.as_view()),
    path(r'^notes/', views.NotesPageView.as_view()),

    # Api urls
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'^api/', include(router.urls))

]
