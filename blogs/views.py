
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import UpdateView, DeleteView

from .forms import CreateForm
from .models import Blog


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blogs/detail.html'


def create(request):
    error =''
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:success_saved'))
        else:
            error = 'Ошибка при создании'

    form = CreateForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'blogs/create.html', data)


def success_saved(request):
    return render(request, 'blogs/success_saved.html')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blogs/'
    template_name = 'blogs/delete.html'


