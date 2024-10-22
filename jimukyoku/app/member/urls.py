from django.urls import path

from . import views

urlpatterns = [
    path(
        "personal-members/",
        views.PersonalMemberListView.as_view(),
        name="personal_member_list",
    ),
]
