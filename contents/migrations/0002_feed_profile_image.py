# Generated by Django 3.1.7 on 2022-10-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='profile_image',
            field=models.TextField(default='https://www.google.com/search?q=%EC%B9%98%ED%82%A8&sxsrf=ALiCzsbCvK2Fwx9Ngc1x77hFvCt5haQebw:1665843067863&tbm=isch&source=iu&ictx=1&vet=1&fir=MV1H1wE7MmRE1M%252CaVVadPkAiVhCeM%252C%252Fm%252F01px4b%253BFmUrkBePxXLuCM%252CdRZ3cUqNyrqDUM%252C_%253Bndtvtx-litlmEM%252CDRDiADhsd1GhLM%252C_%253Bjb8cmcN-P9dsjM%252CNiZazaV-CkPC1M%252C_%253ByZwIsEDTaAHo_M%252Cq-ihT7DSXmnlHM%252C_&usg=AI4_-kSePU-prF--RV5D29Ao4JAiuCSxtA&sa=X&ved=2ahUKEwio076CteL6AhXjrlYBHRy-CO8Q_B16BAgmEAE#imgrc=MV1H1wE7MmRE1M'),
            preserve_default=False,
        ),
    ]
