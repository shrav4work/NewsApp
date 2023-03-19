from django.shortcuts import render
import requests
API_KEY='8560743136454e83b23d96ee7cc888dc'



def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines/?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        print(data)
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines/?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        print(data)
        articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request,'news_api/home.html', context)


