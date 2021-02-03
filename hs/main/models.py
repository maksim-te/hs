from django.db import models


class Task(models.Model):
    task_title = models.CharField('Заголовок задачи', max_length=70)
    description = models.TextField('Описание')
    due_date_to = models.DateTimeField('Срок исполнения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'