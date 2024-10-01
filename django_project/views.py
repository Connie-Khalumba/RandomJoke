import requests
from django.shortcuts import render

def index(request):
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  data = response.json()
  result = data["message"]
  return render(request, 'templates/index.html', {'result': result})

def randomJoke(request):
  response = requests.get("https://official-joke-api.appspot.com/random_joke")
  data = response.json()
  result2 = data["setup"]  # Setup of the joke

  # Pass the joke setup to the template
  return render(request, 'index.html', {'result2': result2})

def joke_view(request):
  response = requests.get('https://official-joke-api.appspot.com/random_joke')
  joke_data = response.json()

  context = {
      'setup': joke_data.get('setup'),
      'punchline': joke_data.get('punchline')
  }

  return render(request, 'templates/index.html', context)