from time import sleep
import random,string
from random import randint
from pyfiglet import Figlet
import itertools
f=Figlet(font='big')
print(f.renderText("WordListOlustur"))
print("""
##############################################################################################################                                                                           
#   	[1] Harf ve Sayı [KARIŞIK] Wordlist Oluştur ------>                                                       
#                                                           
#    	[2] Sadece Sayı için [RASTGELE] Wordlist Oluştur -------->                                                                                                                                 
#   	[3]Küçük Harfler için [RASTGELE] Wordlist oluştur -------->
#            	                                               
#	[4]Büyük Harfler için [RASTGELE] Wordlist oluştur -------->                                                               
#        
#	[5] Kücük Ve Büyük Harfler (Karısık) Wordlist Oluştur ------>                             
# 
#	[6] Sayılar için Kombinasyon yapmak için Wordlist Oluştur -----> 
#
#	[7] Kişiye Özel İsim için Wordlist Oluştur ------>
#
#	[8] Kişiye Özel İsim Kombinasyon yapmak için Wordlist Oluştur ------> 

	[9] Kişiye Özel İsimin Yanında Sayı Wordlist Oluştur -----------> ÖRNEK  	omer1  omer2 omer3 ... omer99 gibi
																				1omer 2omer 3omer... 99omer gibi
#
##############################################################################################################     
 """)
wordlistname=input("Kaydedeceğin dosya ismini yazin (kelime olarak yaziniz sonuna .txt vb koymayın) :")
print("\n")
user_Answer=input("Lütfen WORDLİST OLUSTURUCU tablosundan bir Sayı Giriniz :")
print("\n")
if user_Answer=='1':
		kacdeger=int(input("Kaç Tane İstiyorsunuz :"))
		kacbasamakli=int(input("Kelime Uzunluğu :"))
		lower=string.ascii_lowercase
		upper=string.ascii_uppercase
		num=string.digits
		all= lower +upper+num
		for i in range(0,kacdeger+1):
			sonuc=random.sample(all,kacbasamakli)
			password="".join(sonuc)
			print(password)
			dosya=open(wordlistname+".txt","a")
			dosya.write(password + "\n")
		print("Başarıyla Wordlistiniz oluşturulmuştur.....")
		sleep(3)
		dosya.close()
elif user_Answer=='2':
	kactane=int(input("Kac tane istiyorsunuz :"))
	kacbasamakli=int(input("Kac basamakli istiyorsunuz :"))
	numbers=string.digits
	for i in range(kactane):
		randomnumbers=(''.join(random.choice(numbers) for i in range(kacbasamakli)) )
		print(randomnumbers)
		dosya=open(wordlistname + ".txt", "a")
		dosya.write(randomnumbers + "\n")
	print("Başarıyla Wordlistiniz oluşturulmuştur.....")
	sleep(3)
	dosya.close()
elif user_Answer=='3':
	kactane=int(input("Kaç Tane İstiyorsunuz :"))
	kacbasamakli=int(input("Kaç Basamaklı İstiyorsunuz :"))
	alfabeler=string.ascii_lowercase
	for i in range(kactane):
		kucukalfabeler=(''.join(random.choice(alfabeler) for i in range(kacbasamakli)))
		print(kucukalfabeler)
		dosya=open(wordlistname + ".txt","a")
		dosya.write(kucukalfabeler + "\n")
	print("Başarıyla Wordlistiniz oluşturulmuştur.....")
	sleep(3)
	dosya.close()
elif user_Answer=='4':
	kactane=int(input("Kaç Tane İstiyorsunuz :"))
	kacbasamakli=int(input("Kaç Basamaklı İstiyorsunuz :"))
	alfabeler=string.ascii_uppercase
	for i in range(kactane):
		buyukalfabeler=(''.join(random.choice(alfabeler) for i in range(kacbasamakli)))
		print(buyukalfabeler)
		dosya=open(wordlistname + ".txt","a")
		dosya.write(buyukalfabeler + "\n")
	print("Başarıyla Wordlistiniz oluşturulmuştur.....")
	sleep(3)
	dosya.close()
elif user_Answer=='5':
	kactane=int(input("Kaç Tane İstiyorsunuz :"))
	kacbasamakli=int(input("Kaç Basamaklı İstiyorsunuz :"))
	alfabeler=string.ascii_letters
	for i in range(kactane):
		karisikalfabeler=(''.join(random.choice(alfabeler) for i in range(kacbasamakli)))
		print(karisikalfabeler)
		dosya=open(wordlistname + ".txt","a")
		dosya.write(karisikalfabeler + "\n")
	print("Başarıyla Wordlistiniz oluşturulmuştur.....")
	sleep(3)
	dosya.close()
#Sayı kombinasyonu yapıyoruz
elif user_Answer=='6':
	n=int(input("Kaç Basamakli Kombinasyon yapmak istiyorsunuz :"))
	numbers = "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
	print("Lütfen Bekleyiniz....")
	for wl in itertools.product(numbers, repeat = n):
		file = open(wordlistname+".txt", "a")
		file.write("".join(wl) + "\n")
	print("Başarıyla Wordlistiniz oluşturulmuştur.....")
	sleep(3)
	dosya.close()
#kisiye özel kelime kombinasyon wordlist oluştur
elif user_Answer=='7':
	ozelistek = str(input("Girmek İstediğiniz Kelime Giriniz (Büyük Kücük harflere dikkat ediniz)  :"))
	ozelistek2=int(input("Kaç Tane İstiyorsunuz :"))
	print("Lütfen Bekleyiniz....")
	sayac=1
	while sayac<=ozelistek2:
		liste=(str(randint(1,99999))+ ozelistek + str(randint(1,99999))) 
		liste2=ozelistek+str(randint(1,99999))
		liste3=str(randint(1,99999))+ozelistek
		sayac=sayac+1
		file = open(wordlistname+".txt", "a")
		file.write(liste +"\n")
		file.write(liste2 +"\n")
		file.write(liste3 +"\n")
	print("Başarıyla Wordlistiniz oluşturulmuştur.....")
	sleep(3)
elif user_Answer=='8':
	name = input("Girmek İstediğiniz İsmi Giriniz :")
	print("Lütfen Bekleyiniz....")
	for wl in itertools.product(name, repeat = len(name)):
		liste= name + str(randint(1,99999)) 
		file = open(wordlistname+".txt", "a")
		file.write("".join(wl) + "\n")
		file.write(liste + "\n")
	print("Başarıyla Wordlistiniz oluşturulmuştur.....")
	sleep(3)
	dosya.close()
elif user_Answer=='9':

	ozelistek = str(input("Girmek İstediğiniz Kelime Giriniz (Büyük Kücük harflere dikkat ediniz)  :"))
	ozelistek2=int(input("Girdiğiniz Kelimenin Yanında Kaç Tane Sayı Girsin (Max Sayı Giriniz) :"))
	print("Lütfen Bekleyiniz....")
	for i in range(0,ozelistek2+1):
		liste=ozelistek+str(i)
		print(liste)
		file = open(wordlistname+".txt", "a")
		file.write(liste+"\n")
	for j in range(0,ozelistek2+1):
		liste2=str(j)+ozelistek
		print(liste2)
		file = open(wordlistname+".txt", "a")
		file.write(liste2+"\n")
	print("Başarıyla Wordlistiniz oluşturulmuştur.....")
	sleep(3)
else:
	print("Yanlış Tuş Girdiniz.....")
	print("Programı Yeniden Başlatınız...")
	sleep(3)
