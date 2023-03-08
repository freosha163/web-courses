from django.db import models
import uuid


class Webinar(models.Model):
    CREATED = 'CREATED'
    NOW_IS = 'NOW IS'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCEL'
    status_selection = [
        (CREATED, 'Создан'),
        (NOW_IS, 'Сейчас идет'),
        (COMPLETED, 'Закончен'),
        (CANCELLED, 'Отменен'),
    ]
    title = models.CharField(max_length=100, verbose_name='Название вебинара')
    description = models.CharField(max_length=200, verbose_name='Описание вебинара')
    start_date = models.DateTimeField(db_index=True, verbose_name='Дата проведения вебинара')
    duration = models.TimeField(verbose_name='Длительность вебинара')
    status = models.CharField(max_length=10, choices=status_selection, verbose_name='Статус вебинара')
    subject = models.CharField(max_length=20, verbose_name='Предмет')

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.CharField(max_length=200, verbose_name='Описание курса')
    start_date = models.DateField(db_index=True, verbose_name='Дата начала курса')
    end_date = models.DateField(verbose_name='Дата окончания курса')
    subject = models.CharField(max_length=20, verbose_name='Предмет')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    first_name = models.CharField(max_length=15, verbose_name='Имя преподавателя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия преподавателя')
    position = models.CharField(max_length=100, verbose_name='Должность препоадвателя')
    experience = models.PositiveSmallIntegerField(verbose_name='Стаж преподавателя')
    email = models.EmailField(blank=True, verbose_name='Почта преподавателя')
    webinar = models.ManyToManyField('Webinar', blank=True, related_name='teacher_webinar', verbose_name='Вебинары преподавателя')
    course = models.ManyToManyField('Course', blank=True, related_name='teacher_course', verbose_name='Курсы преподавателя')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
