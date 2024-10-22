from django.views.generic import ListView

from ..models import PersonalMember


class PersonalMemberListView(ListView):
    model = PersonalMember
    template_name = "member/personal_member_list.html"
    context_object_name = "personal_members"
    paginate_by = 10
