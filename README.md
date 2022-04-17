# updater_from_github
Github repolarındaki "Release" bölümünden yeni güncellemeleri indirebileceğiniz bir script.

Reponun latest release'ini "Tag"ine göre kontrol eder. "tag" olarak tam sayı değeri verebilirsiniz.
Eğer ver.json dosyasında girilen version "1" ise ve siz parametlere verilen repo'ya "2" tag'i ile release atarsanız, program ilk çalıştığı anda bu durumu kontrol eder, yeni version geldiğini anlar ve versionu günceller.

Version yüklensin mi diye sormayacaktır. Bu durumu siz ekleyebilirsiniz.

## "ver.json" dosyasındaki parametreler sırasıyla şunlardır;
github : release kısmına erişmek istediğiniz github hesabı
repo : aynı github hesabı içerisindeki repository
run : Güncelleme yapıldıktan sonra çalışacak olan dosya
version : indirilecek olan dosyanın versiyonu

## Repoyu indirdikten hemen sonra şu şekil de test edebilirsiniz.
Ilk indirdiğinizde ya da klonladığınızda
dosyalar içerisinde "start.py" dosyasını göreceksiniz.

Dosya içeriğine bir bakın.

ver.json içerisinde de benim hesabımda bir repoya işaret ettiğini ve version'un 1 olduğunu görebilirsiniz.

Aşağıdaki reponun release kısmına bakacak olursanız, latest release'in tag'i "2"'dir, bizdeki ise "1" olarak gözüküyor yani yazılım güncelleme alacaktır.
https://github.com/atakanargn/NODEMCU_OTA

# Geliştirme
Proje bilerek yarım bırakılmış haldedir.
Eklenebilecekler;
"Yeni sürüm var. Program güncellensin mi?" Yes|No dialog'u.

Pyinstaller ile derleyip kullanabilirsiniz. Sadece kaynak kod değil, binary dosyalar için de güncelleme sistemi olarak kullanabilirsiniz.
