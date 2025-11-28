
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_venue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentprofile',
            options={'permissions': [('can_add_venue', 'Can add venue')]},
        ),
    ]
