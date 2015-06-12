from django.db import models


class Hero(models.Model):
    hero_id = models.IntegerField()
    name = models.CharField(max_length=50)
    local_name = models.CharField(max_length=50)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return ''.join(['id:', str(self.hero_id), ' name:', self.name, ' local_name:', self.local_name])
