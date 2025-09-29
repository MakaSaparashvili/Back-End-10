from django.db import models


class Author(models.Model):
    name=models.CharField(verbose_name="Full Name", max_length=100)
    birth_date = models.DateField(verbose_name="Birth Date", null=True, blank=True)
    country=models.CharField(verbose_name="Country", max_length=100, null=True, blank=True)


    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date=models.DateField(verbose_name="Publication Date", null=True, blank=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    def __str__(self):
        return self.title
