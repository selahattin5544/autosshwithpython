# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 02:28:07 2023

@author: Selahattin Karayel
"""

from time import sleep 
import paramiko #paramiko kutuphanesini kullandim alternatif olarak netmikoda kullanilabilir.


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 3725 Router Versiyonu Eski oldugundan dolayi HostKeyi alabilmek icin bu politikayi kullanmak gerekli.


ssh.connect(hostname='ip address', username='admin', password='admin')  # Baglanti icin gerekli olan kullanici adi ve sifreyi tanimliyoruz
connection = ssh.invoke_shell()  #Bu kod ile Connection degiskenine gerekli olan ssh baglanti bilgilerini atiyoruz.

hostname = input('Hostname Giriniz:')

connection.send("enable\n")#komutlari routera gonderiyorum.
connection.send("admin\n")
connection.send("conf t\n")
connection.send(' hostname ' + hostname + '\n')
connection.send("exit\n")
sleep(.8) # 7.komuta kadar calisiyor ve cikti aliyoruz
output = connection.recv(65535) # Router'dan geri donus alabilmek icin connection.recv 65535 Portunu kullandim
print(output.decode("UTF-8")) #Router'dan gelen ciktiya utf-8 kullanarak decode ettim
print("Hostname Başarıyla Değiştirildi")
ssh.close() #SSH Baglantisini kapattik
