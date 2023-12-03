from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),
    #  /api/register/
    path('register/', views.UserCreateView.as_view()),
    path('artists/', views.ArtistListView.as_view()),
    # /api/works/
    # /api/works?work_type=YT/ or /api/works?work_type=IG/
    # /api/works?artist=[Artist Name]/
    path('works/', views.WorkListView.as_view()),
    # /api/work/create
    path('work/create/', views.WorkCreateView.as_view())
    
]