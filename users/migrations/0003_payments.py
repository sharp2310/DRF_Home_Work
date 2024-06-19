import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_lesson_course"),
        ("users", "0002_alter_user_options_remove_user_username_user_avatar_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
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
                    "data",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="Дата оплаты"
                    ),
                ),
                (
                    "payment_count",
                    models.PositiveIntegerField(verbose_name="Сумма оплаты"),
                ),
                (
                    "payment_method",
                    models.CharField(max_length=50, verbose_name="Метод оплаты"),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paid_course",
                        to="materials.course",
                        verbose_name="paid_course",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paid_lesson",
                        to="materials.lesson",
                        verbose_name="paid_lesson",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "оплата",
                "verbose_name_plural": "оплаты",
            },
        ),
    ]