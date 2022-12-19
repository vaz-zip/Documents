from django.db import models
#from django.contrib.auth.models import User
from documents_1.resources import POSITIONS, reference


# class Author(models.Model):
#     author_user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Автор')
#     # doc = models.OneToOneField("Document", on_delete=models.CASCADE)
    

class Document(models.Model):
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)
    #relevance = models.BooleanField(default=True, verbose_name='Актуален')
    title = models.CharField(max_length=32, default="----", verbose_name='Название')
    category = models.CharField(max_length=16, choices=POSITIONS, default=reference, verbose_name='Тип документа')
    textDocument = models.TextField(blank=True, verbose_name='Содержание')
    # series = models.CharField(max_length=10, default='----', verbose_name='Серия')
    number = models.IntegerField(default=0, verbose_name='Номер')
    # image = models.ImageField(upload_to='media/images/', null=True, verbose_name= 'Изображение')
    dateCreate = models.DateTimeField(null=True, verbose_name='Внесён в базу')
    # dateDocument = models.DateField(verbose_name='Дата на документе')

    

    def __str__(self):

        return f'{self.dateCreate.strftime("%d. %m. %Y")} {self.title} {self.category} {self.number}'

    def get_absolute_url(self):
        
        return f'/documents/{self.id}'
        
            

class Image(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="images", verbose_name='Файл')
    file = models.ImageField(upload_to='media/images/', null=True, verbose_name= 'Изображение')
    

    # def __str__(self):

    #     return f'Изображение {self.document_id}'