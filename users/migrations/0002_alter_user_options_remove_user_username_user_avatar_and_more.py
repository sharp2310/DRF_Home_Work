from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите аватар",
                null=True,
                upload_to="users/avatars",
                verbose_name="Аватар",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="Укажите город",
                max_length=50,
                null=True,
                verbose_name="город",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                blank=True,
                help_text="Укажите номер телефона",
                max_length=35,
                null=True,
                verbose_name="Номер телефона",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Укажите почту",
                max_length=254,
                unique=True,
                verbose_name="Почта",
            ),
        ),
    ]