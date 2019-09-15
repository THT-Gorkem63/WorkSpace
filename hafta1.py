#!/usr/bin/python 3
import time
import random

print("THT-Gorkem63 Tarafindan Kodlandi")
time.sleep(3)

print("-Sayi Tahmin Oyunu-")
time.sleep(2)

rnd_int = random.randint(1,100)

while True:
	entry = int(input("Lutfen 1 den 100 e Kadar Bir Sayi Giriniz:"))
	if (entry == rnd_int):
		print("Bravo! Sansli Sayiyi Buldun :)")
		break
	elif (entry < rnd_int):
		print ("Lutfen Daha Yuksek Sayi Giriniz")
	elif (entry > rnd_int):
		print ("Lutfen Daha Dusuk Sayi Giriniz")
	else:
		print("Lutfen Belirtilen Araliklarda Sayi Giriniz!")

