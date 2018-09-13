from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me'})


def about(request):
    return render(request, 'about.html', {'aboutme': 'Lets Count!'})


def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)#prints to the shell
    wordlist = fulltext.split()

    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            # Increase
            wordDictionary[word] += 1
        else:
            # add to wordDictionary
            wordDictionary[word] = 1

    sortWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortWords': sortWords})
