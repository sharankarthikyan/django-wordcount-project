from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET["fulltext"]
    wordList = fulltext.split()

    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1 

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordList), 'wordDictionary': wordDictionary.items()})
