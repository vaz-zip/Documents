from django.shortcuts import render
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
    # queryset = Image.objects.all()  

    # Document.objects.get().images_set.all()

    # def image(self, request, pk):
    #     return super().post(request, pk)


class DocumentUpdateView(UpdateView):
    template_name = '_edit.html'
    form_class = DocumentsForm
 
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Document.objects.get(pk=id)    