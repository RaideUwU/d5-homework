from django.db import models

# Create your models here.

class Author(models.Model):
    full_name = models.TextField(verbose_name="ФИО")
    birth_year = models.SmallIntegerField(verbose_name="День рождения")
    country = models.CharField(max_length=2, verbose_name="Страна")
    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    name = models.TextField(verbose_name="Издательство")
    def __str__(self):
        return self.name

class Friend(models.Model):
    friend_name = models.TextField(verbose_name="Имя друга")
    def __str__(self):
        return self.friend_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13, verbose_name="Уникальный номер")  
    title = models.TextField(verbose_name="Название")  
    description = models.TextField(verbose_name="Описание")  
    year_release = models.SmallIntegerField(verbose_name="Дата выпуска")  
    copy_count = models.SmallIntegerField(default=1, verbose_name="Количество копий")
    price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Цена")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, verbose_name="Автор")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, verbose_name="Издательство")
    friend = models.ForeignKey(Friend, on_delete=models.PROTECT, null=True, verbose_name="Одолжил")
    def __str__(self):
        return self.title
