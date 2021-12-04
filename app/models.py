from django.db import models


class Dummy(models.Model):
    CHOICE_FIRST = 'first'
    CHOICE_SECOND = 'second'
    CHOICE_THIRD = 'third'
    CHOICES = [
        (CHOICE_FIRST, 'First'),
        (CHOICE_SECOND, 'Second'),
        (CHOICE_THIRD, 'Third'),
    ]
    foo = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=CHOICE_FIRST,
    )
