from django.db import models
class Books(models.Model):
    KHMER = 'kh'
    LANGUAGE = (('kh', 'Khmer'), ('en', 'English'))
    
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    language = models.CharField(max_length=2, choices=LANGUAGE, default=KHMER)
    class Meta:
            ordering = ('title',)