from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserUpdateForm
from .models import CustomUser


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "註冊成功")
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password2"],
        )
        if user:
            login(self.request, user)

        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        messages.success(self.request, "登入成功")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "登入失敗")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    next_page = "users:login"

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "登出成功")
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = "users/update.html"
    success_url = "/"

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def form_valid(self, form):
        messages.success(self.request, "更新成功")
        return super().form_valid(form)
