from django.db import models
from django.urls.base import reverse
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


class Interaction(models.Model):
    project = models.ForeignKey('projects.Project',
                                on_delete=models.CASCADE,
                                related_name='interaction_project',
                                )
    client = models.ForeignKey('clients.Client',
                               on_delete=models.CASCADE,
                               related_name='interaction_client',
                               )
    CHOICE = 'CH'
    REQUEST = 'RQ'
    LETTER = 'LT'
    SITE = 'ST'
    INITIATIVE = 'INT'

    MESSAGE_CHANNEL_CHOICE = [
        (CHOICE, 'Interaction not selected'),
        (REQUEST, 'Request'),
        (LETTER, 'Letter'),
        (SITE, 'Site'),
        (INITIATIVE, 'Initiative of company'),
    ]
    message_channel = models.CharField(max_length=3, choices=MESSAGE_CHANNEL_CHOICE, default=CHOICE,)
    manager = models.ManyToManyField(User, related_name='interaction_manager',)
    description = tinymce_models.HTMLField('Description')

    NOTHING = 'NTH'
    MINUS_ONE = 'M1'
    MINUS_TWO = 'M2'
    MINUS_THREE = 'M3'
    MINUS_FOUR = 'M4'
    MINUS_FIVE = 'M5'
    PLUS_ONE = 'P1'
    PLUS_TWO = 'P2'
    PLUS_THREE = 'P3'
    PLUS_FOUR = 'P4'
    PLUS_FIVE = 'P5'

    GRADE_CHOICE = [
        (MINUS_FIVE, '-5'),
        (MINUS_FOUR, '-4'),
        (MINUS_THREE, '-3'),
        (MINUS_TWO, '-2'),
        (MINUS_ONE, '-1'),
        (NOTHING, 'No grade'),
        (PLUS_ONE, '+1'),
        (PLUS_TWO, '+2'),
        (PLUS_THREE, '+3'),
        (PLUS_FOUR, '+4'),
        (PLUS_FIVE, '+5'),
    ]
    grade = models.CharField(max_length=3, choices=GRADE_CHOICE, default=NOTHING,)

    def __str__(self):
        return 'Interactions'

    def get_absolute_url(self):
        return reverse('interaction_detail', kwargs={'interaction_id': self.pk})
