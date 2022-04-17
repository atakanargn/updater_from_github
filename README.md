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
