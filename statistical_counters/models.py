from django.db import models
from django.utils import timezone


class Statistics(models.Model):
    timestamp = models.DateField(default=timezone.now)
    views = models.IntegerField(default=1)
    clicks = models.IntegerField(default=1)
    cost_of_click = models.DecimalField(max_digits=6, decimal_places=2, default=1)

    @property
    def cpc(self):
        return self.cost_of_click/self.clicks

    @property
    def cpm(self):
        return self.cost_of_click/self.views*1000

    def __str__(self):
        return f"stistic for {self.timestamp}"
