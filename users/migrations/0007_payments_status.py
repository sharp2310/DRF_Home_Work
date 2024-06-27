from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_payments_payment_id_payments_payment_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="status",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="статус"
            ),
        ),
    ]