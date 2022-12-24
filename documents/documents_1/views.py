from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Document, Image
from .filters import DocFilter
from .models import *
from .forms import DocumentsForm


class DocumentList(ListView):
    model = Document, Image
    # ordering = 'title'
    template_name = 'documents.html'
    context_object_name = 'documents'
    queryset = Document.objects.all()
    # paginate_by = 3
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        # context['docs'] = documents.
        context['filter'] = DocFilter(self.request.GET, queryset=self.get_queryset()) # фильтр поиска
        # context['form'] = DocForm
        return context

class DocumentDetail(DetailView):
    model = Document, Image
    template_name = 'document.html'
    context_object_name = 'document'
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Document.objects.get(pk=id)


class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'doc_delete.html'
    context_object_name = 'document'
    # queryset = Document.objects.all()
    success_url = '/documents/'    


def doc_filter(request):
    f = DocFilter(request.GET, queryset=Document.objects.all())
    return render(request, '_filtr.html', {'filter': f})


class DocumentCreateView(CreateView):
    template_name = '_add.html'
    form_class = DocumentsForm
    
    def get_success_url(self) -> str:
        return '/documents/'
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('images')
        if form.is_valid():
            form.cleaned_data.pop('images')
            document = Document.objects.create(**form.cleaned_data)
            Image.objects.bulk_create(
                [Image(file=file, document=document) for file in files]
            )
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class DocumentUpdateView(UpdateView):
    template_name = '_edit.html'
    form_class = DocumentsForm
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Document.objects.get(pk=id)    