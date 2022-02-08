import requests
from bs4 import BeautifulSoup

website = ('https://subslikescript.com/movie/Sunshine-145503')
resultado = requests.get(website)
contenido = resultado.text

soup = BeautifulSoup(contenido, 'lxml')
#print(soup.prettify)  --Obtiene todo el codigo html

caja = soup.find('article', class_='main-article') #Para seleccionar el contenedor del texto que vamos a extraer

titulo = caja.find('h1').get_text() #Para obtener el titulo
texto = caja.find('div', class_='full-script').get_text(strip=True, separator=' ') #Para obtener todo el texto de la pelicula (Transcript)

# Exportar la data en un archivo txt con el nombre de la variable titulo (title), agregamos el tipo de codificacion para evitar mensaje de error
with open(f'{titulo}.txt', 'w', encoding='utf-8') as file:
    file.write(texto)

# print("** Titulo: ", titulo,"\n", texto) Para probar el resultado
