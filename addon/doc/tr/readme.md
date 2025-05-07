## TCA Sistem Araçları

Bir klavye kısayolu aracılığıyla bazı Windows eylemlerini hızlı bir şekilde yürütmemizi sağlayan küçük Eklenti.  
SFC ile sistem onarımı yapabilir. Sistem bilgilerini panoya kopyalayabilir, BIOS'a girebilir ve çok daha fazlasını yapabilirsiniz.  
Eklenti indirmek için, nvda resmi eklenti sayfası da açılabilir.  

* Yazar: Peter Reina <peterrc87@gmail.com>
* Uyumluluk: NVDA 2018 - 2023.3

## Sistem işlevleri:

* Sistem Kapatma: Windows'u Kapatır.
 Ayrıca klasik Windows kapanış sesini de çalar. Sistemin kapatılacağı konusunda bir mesaj ile bizi uyarır.
Bize 3 saniyeliğine kapatmayı onaylama veya iptal etme imkanı sunar.
* Sistem Yeniden Başlatma: Windows'u yeniden başlatır.
Ayrıca klasik Windows kapanış sesini de çalar. Bir mesajla sistemin yeniden başlatılacağı konusunda bizi uyarır.
Bize 3 saniyeliğine yeniden başlatmayı onaylama veya iptal etme imkanı sunar.
* İptal (Kapat veya yeniden başlat): Önceki 2 seçenekten herhangi birini iptal etmemizi sağlar (kapat veya yeniden başlat)
Ayrıca, kapatma veya yeniden başlatmanın iptal edildiğini bize bir mesajla bildirir.
! Not! Bu eylemi gerçekleştirmek için sadece 3 saniyemiz var.
* Hazırda Beklet: Sistemi NVDA'dan rahat bir şekilde hazırda bekletme moduna geçirmemizi sağlar.
* Yeniden başlat ve Ağ ile Güvenli Mod'a gir: Bu moda girmek bazen karmaşık bir işlemdir. Ancak, TCA Sistem Araçları ile çocuk oyuncağıdır. 
Çok kolay bir şekilde, gereksiz hizmetler veya programlar yüklemeden sınırlı işlevlerle Windows'a girmemizi sağlar, oradan daha kapsamlı temizlik yapabilir, istenmeyen programları, kötü amaçlı yazılımları ve çok daha fazlasını kaldırabiliriz.
! Önemli Not!
Bu modda, Windows 10'dan önceki sistemlerde ses hizmeti etkinleştirilmeyebilir, bu nedenle ekran okuyucunun ses sentezine sahip olamayız.
Bu fonksiyon etkinleştirildikten sonra, onu devre dışı bırakmalıyız, bunu aynı TCA-SistemAraçları menüsünden, "Bilgisayarı Kapat" bölümünde yapabiliriz.
* Normal Modda Yeniden Başlat: Güvenli Modu etkinleştirdiysek devre dışı bırakmamızı sağlar, Windows başlangıcını normal değerlerine döndürür (başlangıçta sahip olduğumuz tüm hizmetler ve programlar yüklenir).
* Hazırda Beklet: Bilgisayarı menüden kolayca hazırda bekletme moduna almamızı sağlar.
* BIOS-UEFI'ye gir: Windows'tan rahatça ve NVDA ile bilgisayara bir sonraki yeniden başlatmada BIOS-UEFI'ye girmesini söyleyebiliriz.
Herhangibir tuşa doğrudan basmaya veya bir tuşu bilmeye gerek yoktur.
(Önemli not!) BIOS-UEFI'de ses hizmeti yoktur, bu nedenle arayüzünde ekran okuyucu kullanamayacağız). Sistemimize dönmek istediğimizde CTRL+ALT+Delete tuş kombinasyonuna basabiliriz.
* CMD'yi geçerli yolda aç: Basit bir klavye kısayoluyla Windows komut istemini (CMD) açabiliriz ve odak noktasının bulunduğu herhangi bir klasörün yolunu alır.
* CMD'yi yönetici olarak aç: Basit bir klavye kısayoluyla Windows komut istemini tam yönetici ayrıcalıklarıyla açacağız (Yalnızca Windows 10'dan önceki sistemlerde, odağın bulunduğu klasörün yolunu alın, diğerlerinde System32'de açılacaktır).
* Panoyu ve geçmişini temizle: Windows 10 ve 11'de panoda sahip olduğumuz her şeyi boşaltan kullanışlı işlevsellik, etkinleştirmişsek geçmişte sahip olduğumuz her şeyi de temizler.
* Explorer'ı yeniden başlat: Windows Gezgini'ni NVDA'dan rahatça yeniden başlatır.
Bunu atadığımız bir kısayol aracılığıyla veya TCA-Sistem Araçları menüsünden yapabiliriz.
* Tüm uygulamaları kapat: Windows'un parçası olmayan tüm etkin işlemleri kapatmaya zorlayın (Not! tüm işlemler kapanmaya zorlanacak, bu nedenle hiçbir belge, hiçbir proje kaydedilemez ve hatta NVDA da kapatılacaktır).
* Yanıt Vermeyen Görevleri Kapat - TCA SystemUtilities, yanıt vermeyen işlemleri kapatmaya çalışır.
* Sistem Mimarisini öğren: Bize Windows mimarisini ne olduğunu söyleyecektir (32 veya 64 Bit).
* Klasörleri gizle: Bulunduğumuz klasöre gizli özniteliği koymamızı sağlar, yani klasör gösterilmeyecektir (etkin olması için girmeliyiz).
* Gizli klasörleri göster: Bu işlev, herhangi bir harici cihazı takarken çok kullanışlı olan gizli (USB flash sürücüler, harici diskler ve daha fazlasında geçerlidir) tüm klasörleri ve dosyaları görünür hale getirmemizi sağlar. Klasöre girmeli ve klavye kısayoluna basmalıyız.

## Sistem onarım işlevleri:

* SFC ile sistem Analizi: Windows dosya sistemi SFC /SCANNOW için tarama/onarım yapmamızı sağlar.
* Ayrılmış depolamayı devre dışı bırak: Windows'un güncellemeler için sabit diskimizden sakladığı neredeyse 10 Gb'yi bulan (güncellemelerin çalışması için bunun etkinleştirilmesi gerekmez).
* Ayrılmış depolamayı etkinleştir: Yine de bu Windows işlevini etkinleştirmek ve sabit sürücünüzü neredeyse 10Gb ayırmaya zorlamak istiyorsanız, bu eylemle onu etkinleştireceksiniz.
* DNS Önbelleğini Temizle: Tüm Windows DNS önbelleğini hızlı ve doğrudan temizleyin (internet tarama sorunlarını iyileştirebilir). (
* Güvenli Ekranlarda Kaydedilmiş Ayarları Temizle: Güvenli ekranlarda çalışması için kopyaladığımız tüm eklentileri ve ayarları kaldırır ve NVDA'yı doğal olarak geldiği gibi bırakır.
* Diski Temizle: Windows Disk temizlemeyi başlatmamıza izin verir, ancak çok daha gelişmiş seçeneklerle. Sisteme bağladığımız disklerin ve depolama aygıtlarının her birini tek tek temizleyecektir.
İlk çalıştırdığımızda, bir temizleme profili oluşturmak için bir iletişim penceresi açacak, daha ayrıntılı olarak temizlemek istediğimiz tüm kutuları işaretleyebiliriz. Düğmeye basmamız uygundur: "Profil oluştur", bunu yalnızca bir kez yapmak gerekir. Bu iletişim kutusunun artık görünmesini istemiyorsak işaretleyebileceğimiz bir onay kutumuz var.
* Dism ile sistemi onar: Derin bir tarama gerçekleştirir ve Windows'taki sorunları onarmaya çalışır.

## Doğrudan pano işlevleri:

* Geçerli yolun klasör veya dosyalarının listesini panoya kopyala:
Bulunduğumuz konumun öğelerinin listesini doğrudan panoya kopyalar, böylece onu düzenlenebilir herhangi bir yere yapıştırabiliriz.
* Ses kartlarıyla ilgili bilgileri panoya kopyala: Sistemde bulunan tüm ses cihazlarıyla ilgili bilgileri doğrudan panoya kopyalamamızı sağlar.
böylece düzenlenebilir herhangi bir yere yapıştırabiliriz.
* Sistem bilgilerini kopyala: Sistemimizin bir özetini doğrudan kopyalamamızı sağlar.
böylece düzenlenebilir herhangi bir yere yapıştırabiliriz.
* Yolu kopyala: Bulunduğumuz klasörün yolunu panoya kopyalayacaktır.
 böylece düzenlenebilir herhangi bir yere yapıştırabiliriz.

## Windows Güvenlik Seçenekleri.
Kullanıcı hesabı kontrolü (uac).

* Kullanıcı Hesabı Denetimini Etkinleştir (uac): Kullanıcı hesabı denetim düzeyini 34 (etkin) olarak ayarlar.
* Kullanıcı Hesabı Denetimini Devre Dışı Bırak (uac): Kullanıcı hesabı denetim düzeyini 0 (devre dışı) olarak ayarlar.

Windows Defender.

* Sistem önyüklemesini tara: Windows önyükleme sektörüne (Önyükleme sektörü) ait dosyaların virüs ve kötü amaçlı yazılım taramasını doğrudan gerçekleştirir.
* Tam tarama: Doğrudan tüm sistemin virüs taramasını başlatır.
* hızlı tarama: Doğrudan hızlı bir virüs ve kötü amaçlı yazılım taraması başlatır (temel sistem parçaları).
* Sıkıştırılmış dosyaları tara: Windows antivirüsünün sıkıştırılmış dosyaları (rar, zip, ace, tar, vb.) taraması için doğrudan etkinleştirin.
* Sıkıştırılmış dosyaları tarama: Windows antivirüsünün sıkıştırılmış dosyaları (rar, zip, ace, tar vb.) taramasını doğrudan devre dışı bırakır.
* Karantinaya alınan dosyaların listesini panoya kopyala: Windows antivirüsün karantinaya aldığı tüm dosyaların liste ve bilgilerini panoya kopyalar.

## Multimedya Seçenekleri:

* Web Kamerasını Etkinleştir: varsa web kamerasını etkinleştirmenizi sağlar. (Kullanıma hazır hale getirir)
* Web Kamerasını Devre Dışı Bırak: Etkin olan Web kamerasını devre dışı bırakmamıza imkan verir. (Hiç bir program kullanamaz.)
* Ses karıştırıcı: Windows ses karıştırıcısını NVDA'dan rahatça açmamızı sağlar.
Bunu TCA Sistem Araçları menüsünde, "multimedya" bölümünde yapabiliriz veya bir klavye kısayolu oluşturabiliriz.
* Konuşma Seçeneklerini aç: Metin-konuşma Seçeneklerini veya Özellikler'i hızla açar. Burada varsayılan olarak sistemde yüklü olan TTS sesimizi seçebiliriz.
* Ses Seçeneklerini Aç: Kontrol Panelinin Ses seçeneklerini (Ses, Oynatma, Kayıt, İletişim) doğrudan açmamızı sağlar.

## Bazı sistem işlevlerini hızlıca açın:

* Disk Birleştiricisini Aç: Sabit sürücülerimizin performansını artırmak için Windows'un disk birleştirme penceresini doğrudan açmamıza olanak tanır.
* Karakter haritasını aç: Bu ilginç Windows işlevselliğini doğrudan açar. Bu, sistemdeki mevcut işaretler, sayılar ve harflerden herhangi birini seçmemizi ve bilmemizi sağlar.
Nadir işaretleri bilmek veya klavyeyle elde edilmesi zor olan karakterler için çok faydalıdır.
* Kullanıcı parolalarını kaydet sihirbazını aç: Bu çok kullanışlı ancak az bilinen Windows yardımcı programının sihirbazını açar.
Bu, sistemde sahip olduğumuz kullanıcı hesaplarının kimlik bilgilerini (adlar, şifreler ve daha fazlası) kaydetmemizi sağlar.
* Bluetooth Dosya Aktarım Sihirbazını Aç: BlueTooth cihazlarımız aracılığıyla dosya almak veya göndermek için bu sihirbazı doğrudan başlatmamızı sağlar.
* Klasör Seçeneklerini Aç: Windows Gezgini'ni, klasör görünümlerini, dosya uzantılarının görüntülenmesini ve daha fazlasını yönetmek için bu çok kullanılan özelliği doğrudan açar.
* Roaming Klasörünü Aç: Doğrudan Appdata>Roaming klasörünü açın (Burada NVDA yapılandırma klasörünü ve diğer birçok programı buluyoruz).
* Disk yöneticisini aç: Bilgisayarımızda kurulu diskleri, bölümleri ve diğer depolama cihazlarını yönetmek için bu ilginç işlevi doğrudan açmamıza izin verir.
* Sistem Parolasını kaydetmek için sihirbazı Aç: Harici bir cihazdan kurtarmak için Windows şifresinin yedeğini almamıza izin veren bu az bilinen kullanışlı Asistanı açacaktır.
* Kaynak İzleyicisini Aç: Bu güçlü, az bilinen Windows aracını doğrudan açabiliriz. Gelişmiş bir görev yöneticisi gibi, sistemimizde çalışan tüm hizmetleri, uygulamaları ve süreçleri yönetebiliriz. Ayrıca ne kadar bellek, disk, ağ ve daha fazlasını tükettiklerini bilebiliriz.
* Aygıt yöneticisini aç: Bilgisayarın donanımını ve sürücülerini yönetmek için bu kullanışlı Windows işlevini açmamıza olanak tanır.
* Windows sürümünü göster: Bilgileri işletim sisteminin sürümüyle birlikte açacaktır.
* Resmi Eklenti Sitesini Aç: Bu, NVDA eklentilerini almak için resmi site olan varsayılan tarayıcınızda açılır.

## Önemli Not!

Eklenti hala test aşamasındadır (Beta).  
Ayrıca, klavye kısayollarının her biri, NVDA Tercihler > Girdi Hareketleri iletişim kutusundan kişisel zevkinize göre atanabilir.  

## Sürüm 0.10'daki değişiklikler:
* NVDA 2025.1 sürümüyle uyumluluk desteği.
* Yeni özellik: Yüksek Performans Planını Etkinleştir (Windows Güç yönetimi).
* Yeni işlev: Dengeli planı etkinleştirin (Windows güç yönetimi.).
* Yeni özellik: Konsol başlatıcısını açın.
* Düzeltilmiş Fonksiyon: Geçerli konumda CMD'yi açın.
* Diski Temizle işlevi düzeltildi.
* Diskleri birleştir işlevi düzeltildi.
* Kapat, Yeniden Başlat ve yeniden başlatmayı iptal et özellikleri optimize edildi.

## Sürüm 0.9'daki değişiklikler:
* NVDA 2024.1 ile uyumluluk.
* Yeni özellik Herhangi bir aktif uygulamanın işlemlerini sonlandırın.
* Optimize edilmiş işlev: GetPath, Windows 11 23H2'de gereklidir.
* Dll dahil: Python 3.11 ile uyumlu pywintypes311.dll.
* Kaldırılan varsayılan kısayollar: kapatma, yeniden başlatma ve sistem kapatmayı geçersiz kılma.

## Sürüm 0.8'deki değişiklikler:
* Bu sürümden itibaren TCA Sistem Araçları sürüm isimlendirmesini değiştiriyor (NVDA 2023.3 ile uyumlu olmak için).
Artık sürümler, 0.8.2 şeklinde üç basamaklı olacak.
* Yeni özellik, kullanıcı hesabı kontrolünü (uac) devre dışı bırakma.
* Yeni özellik Kullanıcı Hesabı Denetimini (UAC) Etkinleştir.
* Kullanıcı hesabı kontrol işlevlerinin hem etkinleştirilmesi hem de devre dışı bırakılması, TCA SystemUtilities menüsünde şu kategoride olacaktır: Windows Güvenliği;
Aynı şekilde, dilerseniz Girdi Hareketlerinden klavye kısayollarını da ayarlayabilirsiniz.

## 06 sürümündeki değişiklikler:
* Sistem yolunu (yolu) almak için yeni dahili işlev, şimdi 2 tane var, birinin başarısız olması durumunda TCA SystemUtilities diğerini kullanmayı deneyecek. (İşlevlerden biri geliştirilmiştir: Héctor Benítez).
* Yeni özellik: Tüm etkin işlemleri kapatın.
* Windows'ta yanıt vermeyen görevleri kapatın.
* Eklentiler yeniden yüklendiğinde TCA SystemUtilities menüsünün artık tekrarlanmaması düzeltildi. (Hector Benitez'in izniyle).
* Düzeltildi: Artık önceden tanımlanmış klavye kısayolları yok.

## 05 sürümündeki değişiklikler:

* Güvenli ekranlarda eklentileri ve ayarları temizlemek için yeni özellik.
* Windows'ta geçmiş dahil olmak üzere yeni işlev açık pano.
* Yeni işlev, geçerli yolda CMD'yi açar.
* Yeni işlev, CMD'yi yönetici ayrıcalıklarıyla açar.
* Yeni Özellik: Windows'ta Ayrılmış Depolamayı Devre Dışı Bırakın.
* Yeni Özellik: Windows'ta Ayrılmış Depolamayı Etkinleştirin.
* Nesneyi elde etmek için düzeltilmiş ve optimize edilmiş işlev, bununla birlikte birkaç işlev iyileştirilir, örneğin: panoya giden yolu kopyalama, dosya listesini panoya kopyalama, dosya ve klasörleri gizleme veya gösterme.

## 04 Sürümündeki değişiklikler:

* Sistemin BIOS-UEFI'sine girmesi için yeni işlev ("Bilgisayarı Kapat" bölümünde).
* "Konuşma ve ses" menüsü, "Multimedya" olarak değiştirildi.
* Multimedya bölümüne Web kamerasını devre dışı bırakma ve etkinleştirme eklendi.
* Yeni özellik: "DNS önbelleğini temizle" (Onarım ve optimizasyon bölümünde).
* Eklenti belgeleri yeniden yapılandırıldı.
* İtalyanca Çeviri eklendi.
* NVDA 2022 ile uyumludur.
* Türkçe çevirisi eklendi.
* Güvenlik düzeltmesi (sys.path.remove())

## 03 sürümündeki değişiklikler:

* Windows 11 ile uyumluluk.
* Yeni Menü: Windows Güvenliği Windows antivirüs ile ilgili çeşitli seçeneklerle.
* Menüdeki başka bir seçenek: Bilgisayarı Kapat altında "Hazırda beklet.
* Bu sürümde eklenti şu dillere çevrilmiştir: Arapça, Portekizce (Portekiz, Brezilya Portekizcesi) ve Rumence.

## 02 Sürümündeki değişiklikler: 

* Bu sürümde eklenti, işlevlerinin çoğunu (tümü değil) çalıştırabileceğimiz rahat bir Menüye sahiptir.
NVDA'nın "Araçlar" menüsünde bulunur ve eklenti adına sahiptir: "TCA Sistem Araçları".
* Bu sürümde önceden ayarlanmış tüm kısayollar kaldırılmıştır, o nedenle şimdi NVDA'nın "Girdi hareketleri" menüsünden herhangi bir işleve kısayol atamanız gerekir.
* Menüdeki diğer seçenekler: Bilgisayarı kapat, Windows Gezgini, Ses ve ses, Sistem onarımı.
* Tüm eklenti kodunun optimizasyonu.

***

GitHub'daki proje kodu:
[https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento](https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento)
