# Generated by Django 4.1 on 2023-04-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0004_rename_plaintiff_agent_judgment_agent_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="doc_name",
            field=models.CharField(blank=True, max_length=30, verbose_name="文书名称"),
        ),
        migrations.AlterField(
            model_name="document",
            name="agency",
            field=models.CharField(
                choices=[("1", "法院"), ("2", "检察院"), ("3", "司法行政")],
                max_length=20,
                verbose_name="文书制作单位",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="doc_type",
            field=models.CharField(blank=True, max_length=30, verbose_name="文书种类"),
        ),
        migrations.AlterField(
            model_name="prosecution",
            name="court",
            field=models.CharField(max_length=100, verbose_name="诉至法院"),
        ),
    ]
