---
layout: default
title: Gizlilik Politikası
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <strong>Türkçe</strong> · <a href="privacy-ja">日本語</a>
</div>

# Gizlilik Politikası

**Son güncelleme: 17 Ağustos 2026**

EV Dashboard ("uygulama"), Greg Burlingame tarafından geliştirilmektedir. Bu gizlilik politikası, uygulamanın verilerinizi nasıl işlediğini açıklar.

## Veri toplama

EV Dashboard, herhangi bir kişisel veriyi üçüncü taraflara **toplamaz, iletmez veya satmaz**. Uygulamanın sunucusu, hesabı ve oturum açma özelliği yoktur. Hiçbir şekilde analitik, reklam veya izleme içermez ve verilerinizi hiçbir yere yüklemez.

## Cihazınızda saklanan veriler

Uygulama aşağıdaki verileri cihazınızda yerel olarak saklar:

* **Araç tanılama verileri** — Batarya durumu, hücre gerilimleri, sıcaklıklar, şarj verileri, lastik basınçları ve aracınızdan gelen diğer sensör okumaları, uygulama çalışırken bellekte tutulur. Bir kayıt özelliğini kullanmadığınız sürece bu veriler uygulama açılışları arasında saklanmaz.
* **Sürüş ve şarj geçmişi** — Geçmiş özelliğini kullandığınızda, sürüşlerinizin ve şarj oturumlarınızın özetleri ile kaydedilen sinyal örnekleri (şarj durumu, enerji, sıcaklıklar ve diğer okumalar) daha sonra inceleyebilmeniz için cihazınıza kaydedilir. Bir oturum, haritada gösterilebilmesi için gerçekleştiği konumu da saklayabilir.
* **Uygulama ayarları** — Tercihleriniz (birimler, dil, görünüm, temalar, grafik ayarları, adaptör seçimi, CarPlay kutucuk düzenleri) UserDefaults ile yerel olarak saklanır.
* **Kayıtlı hedefler** — Navigasyon için kaydettiğiniz adresler ve son hedefleriniz cihazınızda yerel olarak saklanır.
* **Bluetooth cihaz bilgileri** — Eşleştirdiğiniz OBD-II adaptörünün tanımlayıcısı ve adı, uygulamanın otomatik olarak yeniden bağlanabilmesi için yerel olarak saklanır.
* **Uygulama etkinlik günlüğü** — Uygulama yaşam döngüsü, Bluetooth bağlantısı, adaptör çakışması ve geçmiş depolama olaylarını kaydeden bir günlük dosyası. Yalnızca Paylaş düğmesini açıkça kullandığınızda paylaşılır.
* **Sürüş tanımlama kaydedici** — Her sürüş için GPS konumlarını, araç hız örneklerini ve mesafe hesaplamalarını içeren, mesafe ve navigasyon doğruluğunu incelemek için kullanılan bir günlük dosyası. Yalnızca Paylaş düğmesini açıkça kullandığınızda paylaşılır.
* **Tanılama kayıtları ve anlık görüntü günlükleri** — Tanılama kaydını veya anlık görüntü karşılaştırma özelliğini kullanırsanız, Bluetooth olaylarını, adaptör komutlarını ve ham araç verilerini içeren bir günlük dosyası yerel olarak kaydedilir. Yalnızca Paylaş düğmesini açıkça kullandığınızda paylaşılır.

## Konum

EV Dashboard, konumunuzu CarPlay haritasında göstermek, adım adım yol tarifi sunmak, sürüş sırasında yolculuk mesafesini ve verimliliği ölçmek ve yakındaki şarj istasyonlarını bulmak için konumunuzu kullanır.

Uygulama yalnızca "Uygulamayı kullanırken" erişimi ister. Hiçbir zaman "Her zaman" erişimi istemez. Yolculuk mesafesi sürüş boyunca sürekli ölçüldüğü için, uygulama arka plandayken veya siz başka bir uygulama kullanırken konum güncellemeleri sürebilir; bu, sürüş bittiğinde sona erer.

Konumunuz cihazınızda kullanılır ve geliştiriciye gönderilmez. Toplanmaz, profillenmez ve satılmaz. Konum verileri yukarıda açıklanan cihaz içi dosyalara yazılabilir (Sürüş tanımlama kaydedici ve bir geçmiş oturumuyla saklanan konum); bunlar yalnızca siz paylaşmayı seçerseniz cihazınızdan çıkar.

## Haritalar ve navigasyon

Haritalar, adres arama ve rota hesaplama Apple'ın MapKit'i tarafından sağlanır. Bir adres aradığınızda veya navigasyonu başlattığınızda, sonuç döndürmek için gereken sorgu ve konum bilgileri Apple'a gönderilir ve [Apple'ın gizlilik politikası](https://www.apple.com/legal/privacy/) kapsamında işlenir. Bu bilgiler geliştiriciye gönderilmez.

## Şarj veritabanı güncellemeleri

DC hızlı şarj noktalarının listesi uygulamanın içinde gelir ve çevrimdışı çalışır. Bir şarj istasyonuna göz atmak veya oraya gitmek için ağ bağlantısı gerekmez.

**Ayarlar → Navigasyon → Güncellemeyi denetle** seçeneğine dokunursanız, yalnızca o zaman uygulama daha yeni bir şarj veritabanı indirir. Bu, iki istek oluşturur: biri theburl.com üzerinde barındırılan bir manifest dosyası için, diğeri de onun belirttiği, GitHub Releases üzerinde barındırılan veri dosyası için. Her ikisi de bir sağlama toplamıyla doğrulanan, sıradan statik dosya indirmeleridir. Bu isteklerle sizinle, cihazınızla veya aracınızla ilgili hiçbir bilgi gönderilmez ve otomatik ya da periyodik bir güncelleme denetimi yoktur.

## iCloud eşitlemesi (isteğe bağlı)

iCloud eşitlemesini açarsanız, sürüş ve şarj geçmişiniz — bir oturumla saklanan konum dahil — Apple'ın CloudKit'i aracılığıyla kendi özel iCloud hesabınıza eşitlenir; böylece iPhone, iPad ve Mac'inizde tutarlı kalır. Bu veriler kişisel iCloud'unuzda saklanır, Apple'ın gizlilik politikasına tabidir ve asla geliştiriciye veya üçüncü taraf bir sunucuya gönderilmez; geliştiricinin bunlara erişimi yoktur. iCloud eşitlemesini kapalı bırakırsanız tüm veriler yalnızca cihazınızda kalır.

## Bluetooth

Uygulama, OBD-II adaptörünüzle Bluetooth Low Energy (BLE) üzerinden iletişim kurar. Tüm Bluetooth iletişimi doğrudan cihazınız ile adaptör arasında gerçekleşir. Hiçbir Bluetooth verisi herhangi bir sunucuya veya üçüncü tarafa iletilmez.

## Araç verileri

Uygulama, OBD-II bağlantı noktası üzerinden aracınızın seyir bilgisayarından tanılama verilerini okur. Bu veriler batarya durumunu, sıcaklıkları, gerilimleri, lastik basınçlarını ve diğer sensör okumalarını içerir. Bu veriler cihazınızda gösterilir ve hiçbir yere iletilmez.

## Bildirimler

Çıkarma hatırlatıcısını etkinleştirirseniz, uygulama araç kapandığında OBD-II adaptörünü çıkarmanızı hatırlatmak için yerel bildirimler kullanır. Hiçbir bildirim verisi sunucuya gönderilmez.

## Veri saklama

Tüm veriler cihazınızda saklanır. Günlük dosyaları ve kayıtlar iOS Dosyalar uygulaması üzerinden silinebilir. Uygulamayı kaldırmak, ayarlar, kayıtlı hedefler ve kayıtlı adaptör bilgileri dahil yerel olarak saklanan tüm verileri kaldırır. iCloud eşitlemesini etkinleştirdiyseniz, geçmişiniz siz uygulama içinden silene veya eşitlemeyi kapatana kadar iCloud hesabınızda da kalır.

## Çocukların gizliliği

Uygulama, 13 yaşın altındaki çocuklardan bilerek veri toplamaz.

## Bu politikadaki değişiklikler

Bu gizlilik politikası güncellenirse, gözden geçirilmiş sürüm güncellenmiş bir tarihle bu sayfada yayımlanacaktır.

## İletişim

Bu gizlilik politikası hakkında sorularınız varsa lütfen GitHub'da bir [konu açın](https://github.com/gburlingame/ioniq-app/issues) veya [greg@theburl.com](mailto:greg@theburl.com) adresine e-posta gönderin.
