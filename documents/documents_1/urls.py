from django.urls import path
from .views import DocumentList, DocumentDetail, DocumentDeleteView, doc_filter, DocumentCreateView, DocumentUpdateView


urlpatterns = [
    path('', DocumentList.as_view()),
    path('<int:pk>', DocumentDetail.as_view(), name='document'),
    path('delete/<int:pk>', DocumentDeleteView.as_view(), name='doc_delete'),
    path('edit/<int:pk>', DocumentUpdateView.as_view(), name='_edit'),
    path('search', doc_filter, name='doc_filter'),
    path('create', DocumentCreateView.as_view(), name='_add')
]