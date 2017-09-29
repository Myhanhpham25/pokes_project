# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

class Poke(models.Model):
	poker = models.ForeignKey(User, related_name = "pokers")
	pokee = models.ForeignKey(User, related_name = "poked")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)