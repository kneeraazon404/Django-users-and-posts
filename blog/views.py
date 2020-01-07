from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import post


def Emails(request):
    sender = os.environ.get("EMAIL_USER")
    send_mail(
        "Alert message:",
        "There  is a  chance of heavy rain which may cause flood to happen in your area please stay alert",
        sender,
        ["nabarajkarki217@gmail.com", "ghimirepinky3@gmail.com"],
        fail_silently=False,
    )
    return render(request, "blog / emails.html")


# def home(request):
#     context = {"posts": post.objects.all()}
#     return render(request, "blog/home.html", context)


class postListView(ListView):
    model = post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5


class UserpostListView(ListView):
    model = post
    template_name = "blog/user_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return post.objects.filter(author=user).order_by("-date_posted")


class postDetailView(DetailView):
    model = post


class postCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class postUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class postDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
