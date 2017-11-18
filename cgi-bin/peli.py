import urllib.request

url = "http://www.omdbapi.com/?apikey=29767981&t=it"

respuesta = urllib.request.urlopen(url)

print(respuesta.read())
