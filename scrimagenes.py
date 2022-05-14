from bs4 import BeautifulSoup
from lxml import html
import requests
import os
import re
import sys

class Scraps:
	
	def foldr(images):
	try:
		ruta = input ("Introduzca la direccion de la nueva carpeta:")
		f = open (ruta, 'r+')
		os.mkdir(imageness)
		f.close

	descargar(images, imageness)

	def descargar(images, imageness):

	count = 0

	print(f"Se encontraron {len(images)} imagenes")

	if len(images) != 0:
		for i, image in enumerate(images):

			try:
				image_link = image["data-srcset"]

			except:
				try:
					image_link = image["data-src"]
				except:
					try:
						image_link = image["data-fallback-src"]
					except:
						try:
							image_link = image["src"]

						except:
							pass

			try:
				r = requests.get(image_link).content
				try:
					r = str(r, 'utf-8')

				except UnicodeDecodeError:

					with open(f"{imageness}/images{i+1}.jpg", "wb+") as f:
						f.write(r)

					count += 1
			except:
				pass

		if count == len(images):
			print("Se descargaron todas las imagenes exitosamente.")

		else:
			print(f"Se descargaron {count} de las {len(images)} imagenes totales.")


	def main(url):

	r = requests.get(url)

	soup = BeautifulSoup(r.text, 'html.parser')

	images = soup.findAll('img')

	foldr(images)
