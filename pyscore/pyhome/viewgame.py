# Generated by Django 4.2.5 on 2023-09-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
    # dependencies = [
    #     ('home', '0005_remove_score_vpoint_score_coupon'),
    # ]

    operations = [
        migrations.CreateModel(
            name="ViewGame",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("gamedate", models.DateField(verbose_name="날짜")),
                ("gamememo", models.CharField(max_length=20, verbose_name="메모")),
                ("coupon", models.IntegerField()),
                ("names", models.CharField(max_length=1000000000)),
                ("count", models.IntegerField()),
            ],
            options={
                "db_table": "v_game",
                "managed": False,
            },
        ),
    ]
