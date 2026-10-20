# 🌍 Wikipedia Nüfus Verisi ETL Boru Hattı

Bu proje, Wikipedia üzerindeki güncel ülke nüfus verilerini otomatik olarak çeken, veriyi `pandas` ile temizleyip biçimlendiren ve güvenli bir şekilde **MySQL** veritabanına kaydeden profesyonel ve modüler bir **ETL (Extract, Transform, Load)** boru hattıdır.

---

## 🚀 Projenin Amacı ve Özellikleri
* **Modüler Mimari:** Sorumluluklarına göre ayrılmış dosyalar (`database.py` ve `etl_pipeline.py`) sayesinde sürdürülebilir ve temiz kod yapısı.
* **Canlı Veri Çekme (Extract):** Wikipedia'dan en güncel nüfus tablosunu `requests` ve `pandas` ile doğrudan çekme.
* **Veri Temizleme & Dönüştürme (Transform):** Gereksiz sütunların ayıklanması, yüzdelik oranların sayısal formata dönüştürülmesi ve tarih verilerinin parse edilmesi.
* **Güvenli Yükleme (Load):** Veritabanı şifreleri kod içine yazılmadan `.env` ve `python-dotenv` ile korunur; veriler hem MySQL veritabanına hem de lokal `.csv` yedeğine aktarılır.

---

## 📁 Proje Dosya Mimarisi

```text
Pipeline/
├── .env                  # Veritabanı şifreleri (Gizlidir, Git'e yüklenmez)
├── .gitignore            # Git tarafından takip edilmeyecek hassas ve geçici dosyalar
├── database.py           # Güvenli veritabanı bağlantı motoru
├── etl_pipeline.py       # Ana ETL boru hattı (Extract, Transform, Load)
└── Guncel_nufus_verisi.csv # Lokal CSV yedeği (Export çıktısı)

🛠️ Kullanılan Teknolojiler
Python 3.x
Pandas (Veri manipülasyonu ve analizi)
Requests (HTTP istek yönetimi)
SQLAlchemy & PyMySQL (MySQL veritabanı bağlantısı)
Python-dotenv (Çevre değişkeni güvenliği)

⚙️ Depoyu klonlayın
git clone [https://github.com/AbdullahKaynak/Dunya_nufusu.git](https://github.com/AbdullahKaynak/Dunya_nufusu.git)
cd Dunya_nufusu

Gerekli kütüphaneleri yükle
pip install pandas requests sqlalchemy pymysql python-dotenv

.env dosyası oluşturun ve MySQL bilgilerinizi tanımlayın:
DB_USER=root
DB_PASSWORD=şifreniz
DB_HOST=localhost
DB_PORT=3306
DB_NAME=dunya_nufus_db

Boru hattını çalıştırın:
python3 etl_pipeline.py

🔒 Güvenlik Politikası
Hassas veriler (veritabanı parolaları vb.) .env dosyası içinde tutulur ve .gitignore sayesinde GitHub'a
yüklenmesi engellenir. Bu sayede projeniz açık kaynak paylaşımına tamamen uygun ve güvenlidir.
