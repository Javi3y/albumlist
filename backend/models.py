#!/usr/bin/env python3
from django.db import models

class Album(models.Model):
    cover = models.ImageField(upload_to=covers,null=True, blank=True)
    title = charField(max_length=60)
    artist = charField(max_length=60)
    release_year = IntegerField()
