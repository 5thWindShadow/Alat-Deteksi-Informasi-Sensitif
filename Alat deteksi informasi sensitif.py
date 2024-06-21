import urllib.parse

def datapribadi1(x):
    x_encoded = urllib.parse.quote('"' + x + '"')
    
    personal_data_search = "Data Pribadi Dork by Files :\n"
    personal_data_search += "\033]8;;https://www.google.com/search?q=" + x_encoded + "%20filetype:pdf%20OR%20filetype:xlsx%20OR%20filetype:docx\033\\"
    personal_data_search += "www.google.com/search?q=" + x_encoded + "%20filetype:pdf%20OR%20filetype:xlsx%20OR%20filetype:docx\n"
    personal_data_search += "\033]8;;\033\\"
    return personal_data_search

def datapribadi2(x):
    x_encoded = urllib.parse.quote('"' + x + '"')
    
    personal_info_search = "Data Pribadi Dork (Text) :\n"
    personal_info_search += "\033]8;;https://www.google.com/search?q=" + x_encoded + "%20intext:NIK%20OR%20intext:Alamat%20OR%20intext:KK\033\\"
    personal_info_search += "www.google.com/search?q=" + x_encoded + "%20intext:NIK%20OR%20intext:Alamat%20OR%20intext:KK\n"
    personal_info_search += "\033]8;;\033\\"
    return personal_info_search

def kredlogin1(x):
    x_encoded = urllib.parse.quote('"' + x + '"')
    
    login_credentials_search = "Kredensial Login (SQL) :\n"
    login_credentials_search += "\033]8;;https://www.google.com/search?q=" + x_encoded + "%20filetype:sql%20intext:password\033\\"
    login_credentials_search += "www.google.com/search?q=" + x_encoded + "%20filetype:sql%20intext:password\n"
    login_credentials_search += "\033]8;;\033\\"
    return login_credentials_search

def kredlogin2(x):
    x_encoded = urllib.parse.quote('"' + x + '"')
    
    login_credentials_search = "Kredensial Login (XLS) :\n"
    login_credentials_search += "\033]8;;https://www.google.com/search?q=" + x_encoded + "%20filetype:xls%20intext:password\033\\"
    login_credentials_search += "www.google.com/search?q=" + x_encoded + "%20filetype:xls%20intext:password\n"
    login_credentials_search += "\033]8;;\033\\"
    return login_credentials_search

def organdatapribadi(web):
    web_encoded = urllib.parse.quote('site:' + web + '')
    
    personal_data_search = "Organisasi Data Pribadi :\n"
    personal_data_search += "\033]8;;https://www.google.com/search?q=" + web_encoded + "%20intext:%22tanggal%20lahir%22%20%22NIK%22%20filetype:pdf%20OR%20filetype:xlsx%20OR%20filetype:docx\033\\"
    personal_data_search += "www.google.com/search?q=" + web_encoded + "%20intext:%22tanggal%20lahir%22%20%22NIK%22%20filetype:pdf%20OR%20filetype:xlsx%20OR%20filetype:docx\n"
    personal_data_search += "\033]8;;\033\\"
    return personal_data_search

def organkredlog1(web):
    web_encoded = urllib.parse.quote('site:' + web + '')
    
    login_credentials_search = "Organisasi Kredensial Login (SQL) :\n"
    login_credentials_search += "\033]8;;https://www.google.com/search?q=" + web_encoded + "%20filetype:sql%20intext:password\033\\"
    login_credentials_search += "www.google.com/search?q=" + web_encoded + "%20filetype:sql%20intext:password\n"
    login_credentials_search += "\033]8;;\033\\"
    return login_credentials_search

def organkredlog2(web):
    web_encoded = urllib.parse.quote('site:' + web + '')
    
    login_credentials_search = "Organisasi Kredensial Login (XLS) :\n"
    login_credentials_search += "\033]8;;https://www.google.com/search?q=" + web_encoded + "%20filetype:xls%20intext:password\033\\"
    login_credentials_search += "www.google.com/search?q=" + web_encoded + "%20filetype:xls%20intext:password\n"
    login_credentials_search += "\033]8;;\033\\"
    return login_credentials_search

def source1(web):
    web_encoded = urllib.parse.quote('site:' + web + '')
    
    source1_search = "Source code (Apache) :\n"
    source1_search += "\033]8;;https://www.google.com/search?q=" + web_encoded + "%20intext:%22index%20of%20/home%22\033\\"
    source1_search += "www.google.com/search?q=" + web_encoded + "%20intext:%22index%20of%20/home%22\n"
    source1_search += "\033]8;;\033\\"
    return source1_search

def source2(web):
    web_encoded = urllib.parse.quote('site:' + web + '')
    
    source2_search = "Source code (PHP) :\n"
    source2_search += "\033]8;;https://www.google.com/search?q=" + web_encoded + "%20%22index%20of%22%20inurl:.php\033\\"
    source2_search += "www.google.com/search?q=" + web_encoded + "%20%22index%20of%22%20inurl:.php\n"
    source2_search += "\033]8;;\033\\"
    return source2_search

def source3(web):
    web_encoded = urllib.parse.quote('site:' + web + '')
    
    source3_search = "Source (GIT) :\n"
    source3_search += "\033]8;;https://www.google.com/search?q=" + web_encoded + "%20%22index%20of%22%20inurl:.git\033\\"
    source3_search += "www.google.com/search?q=" + web_encoded + "%20%22index%20of%22%20inurl:.git\n"
    source3_search += "\033]8;;\033\\"
    return source3_search

if __name__ == "__main__":
    print("\n ALAT DETEKSI INFORMASI SENSITIF")
    print("by Iman Kurnia \n")
    print("Pilih jenis target : \n 1)Individu (Data Pribadi & Kredensial Login) \n 2)Organisasi (Data Pribadi, Kredensial Login, & Source Code)\n")
    opsi = input("[ 1/2 >] ")

    if int(opsi) == 1:
        print("Jenis Target : Individual")
        nama = input("Masukkan Nama Lengkap Target : ")
        print("\n Hasil Dork (Jika link tidak dapat diklik, coba ctrl+klik) : \n")
        nama1 = datapribadi1(nama)
        nama2 = datapribadi2(nama)
        nama3 = kredlogin1(nama)
        nama4 = kredlogin2(nama)
        print(nama1)
        print(nama2)
        print(nama3)
        print(nama4)

    elif int(opsi) == 2:
        print("Jenis Target : Organisasi")
        organ = input("Masukkan Web Organisasi Target (ex: google.com) : ")
        print("\n Hasil Dork (Jika link tidak dapat diklik, coba ctrl+klik) : \n")
        organ1 = organdatapribadi(organ)
        organ2 = organkredlog1(organ)
        organ3 = organkredlog2(organ)
        organ4 = source1(organ)
        organ5 = source2(organ)
        organ6 = source3(organ)
        print(organ1)
        print(organ2)
        print(organ3)
        print(organ4)
        print(organ5)
        print(organ6)

    else:
        print("Choose the number in the options \n")