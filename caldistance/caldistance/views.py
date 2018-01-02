from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient

import sys
import os
import os.path
from os import listdir
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
import json
from nltk.translate.bleu_score import sentence_bleu


def bleu(request):
    return render(request, "bleu.html", {})

def leven(request):
	return render(request, "leven.html", {})

@csrf_exempt
def givetoPy(request):
    candidate = request.POST['candidate']
    reference = request.POST['reference']
    score = sentence_bleu([reference], candidate)
    score = float("{0:.2f}".format(score));
    return HttpResponse(json.dumps({'result': score}), content_type="application/json")