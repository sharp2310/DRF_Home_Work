import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название курса"),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью курса",
                        null=True,
                        upload_to="materials_media/courses/previews",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Опишите основные материалы курса",
                        null=True,
                        verbose_name="Описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название урока"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Опишите основные материалы урока",
                        null=True,
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью урока",
                        null=True,
                        upload_to="materials_media/lessons/previews",
                        verbose_name="Превью урока",
                    ),
                ),
                (
                    "video_link",
                    models.URLField(
                        blank=True,
                        help_text="Укажите ссылку на видео урока",
                        null=True,
                        verbose_name="Ссылка на видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]