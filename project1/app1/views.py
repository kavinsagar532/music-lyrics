from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
import requests
from requests_oauthlib import OAuth2Session
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def homepage(request):
    template=loader.get_template('homepage.html')
    return HttpResponse(template.render())
def first(request):
    template=loader.get_template('first.html')
    return HttpResponse(template.render())
def english_songs(request):
    template=loader.get_template('english_songs.html')
    return HttpResponse(template.render())
def shape_of_you(request):
    template=loader.get_template('shape_of_you.html')
    return HttpResponse(template.render())
def dandelions(request):
    template=loader.get_template('dandelions.html')
    return HttpResponse(template.render())
def believer(request):
    template=loader.get_template('believer.html')
    return HttpResponse(template.render())
def perfect(request):
    template=loader.get_template('perfect.html')
    return HttpResponse(template.render())
def love_me_like_you_do(request):
    template=loader.get_template('love_me_like_you_do.html')
    return HttpResponse(template.render())
def tamil_songs(request):
    template=loader.get_template('tamil_songs.html')
    return HttpResponse(template.render())
def hukum(request):
    template=loader.get_template('hukum.html')
    return HttpResponse(template.render())
def nira(request):
    template=loader.get_template('nira.html')
    return HttpResponse(template.render())
def naa_ready(request):
    template=loader.get_template('naa_ready.html')
    return HttpResponse(template.render())
def naan_gaali(request):
    template=loader.get_template('naan_gaali.html')
    return HttpResponse(template.render())
def aval(request):
    template=loader.get_template('aval.html')
    return HttpResponse(template.render())
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def signup(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render())
def lyrics(request):
    template=loader.get_template('lyrics.html')
    return HttpResponse(template.render())
# views.py

def fetch_lyrics(song_title):
    # Create an OAuth2Session with Genius API credentials
    client_id = settings.GENIUS_CLIENT_ID
    client_secret = settings.GENIUS_CLIENT_SECRET
    redirect_uri = 'http://127.0.0.1:8000/lyrics/homepage/first.html/lyrics.html'  # Ensure the redirect URI matches your Genius application settings
    authorization_base_url = 'https://api.genius.com/oauth/authorize'
    token_url = 'https://api.genius.com/oauth/token'

    genius = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, _ = genius.authorization_url(authorization_base_url)

    # Redirect user to Genius for authorization
    return authorization_url

def get_lyrics(request):
    if request.method == 'POST':
        # Handle form submission
        song_title = request.POST.get('song_title', '')
        if song_title:
            # Redirect to the Genius authorization URL
            authorization_url = fetch_lyrics(song_title)
            return redirect(authorization_url)
        else:
            lyrics_url = 'Please enter a song title.'
    else:
        lyrics_url = None

    return render(request, 'lyrics.html', {'lyrics_url': lyrics_url})

def callback(request):
    # Handle the callback from Genius and obtain the access token
    client_id = settings.GENIUS_CLIENT_ID
    client_secret = settings.GENIUS_CLIENT_SECRET
    redirect_uri = 'http://127.0.0.1:8000/lyrics/homepage/first.html/lyrics.html'  # Ensure the redirect URI matches your Genius application settings
    token_url = 'https://api.genius.com/oauth/token'

    genius = OAuth2Session(client_id, redirect_uri=redirect_uri)
    token = genius.fetch_token(
        token_url,
        client_secret=client_secret,
        authorization_response=request.build_absolute_uri(),
    )

    # Use the access token to make authenticated requests to Genius API
    song_title = request.GET.get('song_title', '')  # Get the song title from the query parameters
    api_url = f'https://api.genius.com/search?q={song_title}'
    headers = {
        'Authorization': f'Bearer {token["access_token"]}',
    }

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        lyrics_url = data['response']['hits'][0]['result']['url']
    except Exception as e:
        lyrics_url = 'Lyrics not found'

    return render(request, 'lyrics.html', {'lyrics_url': lyrics_url})

