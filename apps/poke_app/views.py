# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Poke
from django.db.models import Count


def dashboard(request):

	#The number of times they poked me.	
	receivedpokes = Poke.objects.filter(pokee = request.session['id'])

	obj = {}
	for poke in receivedpokes:
		name = poke.poker.name
		if name not in obj:
			obj[name] = 1
		else: 
			obj[name] += 1
	print obj	

	context = {

	'curUser' : User.objects.get(id = request.session['id']),
	'otherUsers' : User.objects.exclude(id = request.session['id']).order_by(),
	'totalCount' : obj,

	}	

	if 'email' not in request.session:
		return redirect("/")
	else:
		return render(request, 'poke_app/dashboard.html', context)

def givepoke(request, user_id):

	Poke.objects.create(poker = User.objects.get(id = request.session['id']), pokee = User.objects.get(id = user_id))

	return redirect('/poke/dashboard')


	#'pokedMe' : User.objects.get(id = request.session['id']).poked.all().values('poker__name').distinct(),
	# {%for user in pokedMe%}
	# 	<p>{{user.poker__name}}<p>
	# 	{%endfor%}	

	# <p> ID of people who poked me</p>
	# 	{%for user in pokers%}
	# 	<p>{{user.poker__id}}</p>
	# 	{%endfor%}

# <p><strong>The number of times they poked me.</strong></p>
#'pokers2' : receivedpokes,
# 		{%for poke in pokers2%}
# 		<p>{{poke.poker.name}}<p>
# 		{%endfor%}

	#'people' : User.objects.values('name').annotate(Count('poked')), #total count of how many times the user have poked someone




	