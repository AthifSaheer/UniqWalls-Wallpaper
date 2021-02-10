from django.shortcuts import render
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

class AdminPageView(CreateView):
    template_name = 'admin.html'
    form_class = PictureAddingForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CategoryAddingView(CreateView):
    template_name = 'category_adding.html'
    form_class = CategoryAddingForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)