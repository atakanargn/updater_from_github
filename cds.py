from requests import get
from os import listdir, rmdir, mkdir, getcwd, chdir
from os.path import isfile, join
from shutil import move
from sys import stdout, argv, executable
from json import loads, dumps
from subprocess import Popen
from ctypes import windll
from logger import log_exception

class CDS:
    @log_exception
    def __init__(self,file,control_and_run=True,cwd=getcwd(),admin_control=False):
        print("Sürüm kontrolü...")
        self.cwd = cwd
        self.file = file
        self.options = loads(open(file,"r").read())
        self.owner   = self.options['github']
        self.repo    = self.options['repo']
        self.version = self.options['version']
        self.run     = self.options['run']
        self.control_and_run = control_and_run

        if admin_control:
            if self.is_admin()==False:
                chdir(self.cwd)
                pass
            else:
                windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)

        self.control()

    @log_exception
    def is_admin(self):
        try:
            return windll.shell32.IsUserAnAdmin()
        except:
            return False

    @log_exception
    def control(self):
        chdir(self.cwd)
        self.url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
        
        req = get(url=self.url)

        print("Kurulu sürüm:",self.version)
        print("Güncel sürüm:",req.json()['tag_name'])

        if int(req.json()['tag_name'])>self.version:
            mkdir("update",777)
            print("Yeni sürüm kuruluyor...")
            NEW_VERSION_URL = get(url=req.json()['assets'][0]['url']).json()['browser_download_url']
            filename = NEW_VERSION_URL.split("/")[-1]
            self.download(filename,NEW_VERSION_URL)

            files = [f for f in listdir("update") if isfile(join(".", f))==True]
            for file in files:
                move("./update/{}".format(filename), "./{}".format(filename))
                print('Güncelleme tamamlandı')
            self.options['version']=int(req.json()['tag_name'])
            open(self.file,"w+").write(dumps(self.options))
            rmdir("./update")
        if self.control_and_run:
            Popen(self.run)
    
    @log_exception
    def download(self,filename,link):
        chdir(self.cwd)
        with open("{}{}".format("./update/",filename), "wb") as f:
            print("Indiriliyor %s" % filename)
            response = get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    stdout.write("\r[%s%s]\n" % ('=' * done, ' ' * (32-done)) )    
                    stdout.flush()