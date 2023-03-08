# Generated by Django 3.2.18 on 2023-03-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_auto_20230308_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='course',
            field=models.ManyToManyField(blank=True, related_name='teacher_course', to='src.Course', verbose_name='Курсы преподавателя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='webinar',
            field=models.ManyToManyField(blank=True, related_name='teacher_webinar', to='src.Webinar', verbose_name='Вебинары преподавателя'),
        ),
    ]