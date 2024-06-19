from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_payments_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="data",
            field=models.DateField(
                auto_now_add=True, null=True, verbose_name="Дата оплаты"
            ),
        ),
    ]