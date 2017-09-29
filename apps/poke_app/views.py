# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Poke
from django.db.models import Count


def dashboard(request):

	
	context = {

	'curUser' : User.objects.get(id = request.session['id']),
	'otherUsers' : User.objects.exclude(id = request.session['id']).order_by(),
	'pokedMe' : User.objects.get(id = request.session['id']).poked.all().values('poker__name').distinct(),
	'people' : User.objects.all().values('name').annotate(Count('poked')),

	}	
	
	everyone = User.objects.all()

	me = User.objects.get(id = request.session['id'])
	
	pokeePokedMe = context['curUser'].poked.all().values('pokee__id').distinct()
	# for pokes in pokeePokedMe:
	# 		context['pokers'].append(User.objects.get(id = pokes('pokee__id')))
	# I COULDN'T GET IT TO LOOP THROUGH AND PULL NAMES. BUT I THINK MY 'POKEDME' did the job. 
	# I DIDN'T REALIZED THAT TO ADD COUNT I NEEDED TO DO A FOR LOOP WITH COUNT++


	if 'email' not in request.session:
		return redirect("/")
	else:
		return render(request, 'poke_app/dashboard.html', context)


def givepoke(request, user_id):

	Poke.objects.create(poker = User.objects.get(id = request.session['id']), pokee = User.objects.get(id = user_id))


	return redirect('/poke/dashboard')