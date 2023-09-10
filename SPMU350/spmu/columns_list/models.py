from django.db import models

class Columns(models.Model):
    title = models.CharField('ФИО', max_length=100, db_index=True, unique=True)
    link = models.CharField('Ссылка', max_length=250)
    info = models.TextField('Краткая информация', db_index=True)
    photo = models.TextField('Фотография', db_index=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/columns_list/{self.id}'

    class Meta:
        verbose_name = 'Выпускник'
        verbose_name_plural = 'Выпускники'
        ordering = ['title']
