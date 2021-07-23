from django.urls import path

from rest_framework.authtoken import views

from .views import PollList, PollDetail, ChoiceList, CreateVote, UserCreate, LoginView

app_name = "polls"

urlpatterns = [

    path("polls", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices", ChoiceList.as_view(), name="choice_list"),
    path("choices/", ChoiceList.as_view(), name="choices_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("login2/", views.obtain_auth_token, name="login2"),


]
