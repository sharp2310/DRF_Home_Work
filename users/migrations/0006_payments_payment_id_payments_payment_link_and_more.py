from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_payments_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="payment_id",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="id оплаты"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="payment_link",
            field=models.CharField(
                blank=True, max_length=400, null=True, verbose_name="ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="tokens",
            field=models.CharField(
                blank=True, max_length=400, null=True, verbose_name="tokens"
            ),
        ),
    ]