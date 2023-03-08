# Generated by Django 3.2.18 on 2023-03-08 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('description', models.CharField(max_length=200, verbose_name='Описание курса')),
                ('start_date', models.DateField(db_index=True, verbose_name='Дата начала курса')),
                ('end_date', models.DateField(verbose_name='Дата окончания курса')),
                ('subject', models.CharField(max_length=20, verbose_name='Предмет')),
            ],
        ),
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название вебинара')),
                ('description', models.CharField(max_length=200, verbose_name='Описание вебинара')),
                ('start_date', models.DateTimeField(db_index=True, verbose_name='Дата проведения вебинара')),
                ('duration', models.TimeField(verbose_name='Длительность вебинара')),
                ('status', models.CharField(choices=[('CREATED', 'Создан'), ('NOW IS', 'Сейчас идет'), ('COMPLETED', 'Закончен'), ('CANCEL', 'Отменен')], max_length=10, verbose_name='Статус вебинара')),
                ('subject', models.CharField(max_length=20, verbose_name='Предмет')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, verbose_name='Имя преподавателя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия преподавателя')),
                ('position', models.CharField(max_length=100, verbose_name='Должность препоадвателя')),
                ('experience', models.PositiveSmallIntegerField(verbose_name='Стаж преподавателя')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта преподавателя')),
                ('course', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_course', to='src.course', verbose_name='Курсы преподавателя')),
                ('webinar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_webinar', to='src.webinar', verbose_name='Вебинары преподавателя')),
            ],
        ),
    ]
