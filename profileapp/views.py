from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin



class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    # def get_context_data(self, **kwargs):
    #     object_list = Article.objects.filter(writer=self.get_object())
    #     return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)