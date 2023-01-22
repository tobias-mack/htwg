from requests import Session
from bs4 import BeautifulSoup as bs
#username & password in file credentials.py
import credentials

username = credentials.username
password = credentials.password

moodle_login_page = "https://moodle.htwg-konstanz.de/moodle/login/index.php"
barrier_free_chat = "https://moodle.htwg-konstanz.de/moodle/mod/chat/gui_basic/index.php?id=354"
normal_chat = "https://moodle.htwg-konstanz.de/moodle/mod/chat/view.php?id=219346"
moodle_upload_page = "https://moodle.htwg-konstanz.de/moodle/mod/assign/view.php?id=219345"
pdf_file = "https://moodle.htwg-konstanz.de/moodle/pluginfile.php/346660/mod_assign/introattachment/0/AIN%20RN%20-%20Laboraufgabe%20-%20HTTP.pdf"

textfile = "/home/twobeers/Desktop/Rechnernetze/HTTP/data.txt"
pdffile = "/home/twobeers/Desktop/Rechnernetze/HTTP/data.pdf"

def downloadPdf():
    pdf = s.get(pdf_file)
    text_file = open(pdffile,"wb")
    text_file.write(pdf.content)
    text_file.close()

def sendMessage():
    lab5_chat = s.get(barrier_free_chat)
    bs_content = bs(lab5_chat.content, "html.parser")
    last = bs_content.find("input", {"name":"last"})["value"]
    sesskey = bs_content.find("input", {"name":"sesskey"})["value"]
    message_data = {"message": "message","id": "354", "groupid":"0", "last": last, "sesskey": sesskey}
    print(message_data)
    s.post(barrier_free_chat,message_data)

with Session() as s:
    site = s.get(moodle_login_page)
    bs_content = bs(site.content, "html.parser")

    login_token = bs_content.find("input", {"name":"logintoken"})["value"]
    login_data = {"username": username,"password": password, "logintoken":login_token}

    s.post(moodle_login_page,login_data)
    #downloadPdf()
    sendMessage()

