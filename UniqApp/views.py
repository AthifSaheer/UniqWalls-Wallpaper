from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import *
from .models import *
from .forms import *

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = Image.objects.all()
        return context
    
    # def get(self, request, *args, **kwargs):
    #     image = Image.objects.get(pk=self.kwargs['image_id'])
    #     image_buffer = open(image.file.path, "rb").read()
    #     content_type = magic.from_buffer(image_buffer, mime=True)
    #     response = HttpResponse(image_buffer, content_type=content_type);
    #     response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(image.file.path)
    #     return response

class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

@method_decorator(staff_member_required, name='dispatch')
class AdminPageView(CreateView):
    template_name = 'admin.html'
    form_class = PictureAddingForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ImageUploadView(CreateView):
    template_name = 'image_upload.html'
    form_class = PictureAddingForm
    success_url = '/adminpage'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CategoryAddingView(CreateView):
    template_name = 'category_adding.html'
    form_class = CategoryAddingForm
    success_url = '/adminpage'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ImageDeleteView(TemplateView):
    template_name = 'image_delete_view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = Image.objects.all()
        return context

class ImageDeleteButton(DeleteView):
    template_name = "image_confirm_delete.html"
    model = Image
    success_url = '/adminpage'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = Image.objects.all()
        return context

class CategoryDeleteView(TemplateView):
    template_name = 'category_delete_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class CategoryDeleteButton(DeleteView):
    template_name = "category_condirm_delete.html"
    model = Category
    success_url = "/adminpage"

class SigninView(FormView):
    template_name = 'auth/signin.html'
    form_class = OwnUserLoginForm
    success_url = '/'

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form":self.form_class, "error":"Invalid Credentials"})
        return super().form_valid(form)

class SignupView(FormView):
    template_name = 'auth/signup.html'
    form_class = OwnUserRegisterForm
    success_url = '/signin'

    def form_valid(slef, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        return super().form_valid(form)

class LogoutView(View):
    def get(self,request):
        x = logout(request)
        return redirect('home')