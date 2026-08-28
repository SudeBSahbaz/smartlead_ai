# ENCORE – AI Destekli Kültür-Sanat Asistanı

ENCORE, kullanıcıların kültür ve sanat hakkında yapay zekâ destekli yanıtlar almasını ve iletişim bilgilerini bırakmasını sağlayan bir web uygulamasıdır.

Proje; Python, Flask, SQLite, Groq AI API ve Wix Velo kullanılarak geliştirilmiştir. Backend Render üzerinde yayınlanmış, kullanıcı ve yönetim arayüzleri Wix Studio ile hazırlanmıştır.

---

## Projenin Amacı

ENCORE'un amacı, kültür-sanat alanında kullanıcılarla etkileşim kurabilen basit bir yapay zekâ asistanı oluşturmak ve ilgilenen kullanıcıların iletişim bilgilerini lead olarak kaydetmektir.

Sistem iki temel arayüzden oluşur:

- **B2C Kullanıcı Arayüzü:** Kullanıcı yapay zekâ asistanına soru sorabilir ve iletişim bilgilerini bırakabilir.
- **B2B Yönetim Paneli:** Kaydedilen lead verileri yönetim ekranında listelenebilir.

---

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Wix Studio
- Wix Velo
- JavaScript
- HTML / CSS
- Git & GitHub
- Render

---

## Proje Mimarisi

```text
smartlead_ai/
│
├── app/
│   ├── services/
│   │   ├── __init__.py
│   │   └── ai_service.py
│   │
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   │
│   ├── __init__.py
│   ├── database.py
│   └── routes.py
│
├── config.py
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
```

---

## Modüller

### config.py

Uygulamanın ortam değişkenlerini ve yapılandırma ayarlarını yönetir.

API anahtarları kaynak kod içerisine yazılmak yerine `.env` ve Render Environment Variables üzerinden yönetilir.

### database.py

SQLite veritabanı işlemlerinden sorumludur.

Lead kayıtlarının oluşturulması ve listelenmesi bu modül üzerinden gerçekleştirilir.

### ai_service.py

Yapay zekâ servisi ile iletişim kuran katmandır.

Kullanıcı mesajları Groq API'ye gönderilir ve yapay zekâ tarafından oluşturulan yanıt uygulamaya döndürülür.

### routes.py

Sayfa ve API rotalarını içerir.

Uygulamada `pages` ve `api` olmak üzere iki Flask Blueprint kullanılmaktadır.

### app/__init__.py

Flask uygulamasının oluşturulduğu application factory yapısını içerir.

Veritabanı başlatılır, Blueprint'ler kaydedilir ve API rotaları için CORS yapılandırması uygulanır.

---

## API Endpointleri

### Health Check

```http
GET /api/health
```

Örnek yanıt:

```json
{
  "basari": true,
  "durum": "ok"
}
```

### AI Sohbet

```http
POST /api/sohbet
```

Örnek istek:

```json
{
  "mesaj": "İstanbul'da bir sanat etkinliği önerir misin?",
  "gecmis": []
}
```

Başarılı yanıtta `basari` ve yapay zekâ tarafından oluşturulan `yanit` alanları döndürülür.

### Lead Oluşturma

```http
POST /api/leads
```

Örnek istek:

```json
{
  "isim": "Test Kullanıcı",
  "telefon": "5551234567",
  "mesaj": "Kültür-sanat etkinlikleriyle ilgileniyorum."
}
```

### Lead Listeleme

```http
GET /api/leads
```

SQLite veritabanında bulunan lead kayıtlarını JSON formatında döndürür.

---

## Wix Entegrasyonu

Wix Studio üzerinde iki temel arayüz hazırlanmıştır.

### B2C Arayüzü

Kullanıcı:

- ENCORE yapay zekâ asistanına mesaj gönderebilir.
- Yapay zekâ yanıtını görüntüleyebilir.
- Ad Soyad ve Telefon bilgilerini bırakabilir.
- Bilgilerini backend API üzerinden kaydedebilir.
- Yönetim Paneli sayfasına geçebilir.

Wix Velo tarafında `wix-fetch` kullanılarak Flask API ile iletişim kurulmaktadır.

### B2B Yönetim Paneli

Yönetim Paneli, Flask API'deki:

```http
GET /api/leads
```

endpoint'inden kayıtları alır.

Veriler Wix Repeater içerisinde aşağıdaki alanlarla gösterilir:

- ID
- İsim
- Telefon
- Mesaj
- Tarih

Her kayıt için benzersiz `_id` değeri kullanılır.

---

## Veritabanı

Projede SQLite kullanılmaktadır.

Temel `leads` tablosu aşağıdaki verileri saklar:

- id
- isim
- telefon
- mesaj
- tarih

---

## Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/SudeBSahbaz/smartlead_ai.git
cd smartlead_ai
```

Sanal ortam oluşturun:

```bash
python -m venv venv
```

Windows üzerinde sanal ortamı etkinleştirin:

```bash
venv\Scripts\activate
```

Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

---

## Ortam Değişkenleri

Proje kök dizininde `.env` dosyası oluşturulmalıdır.

Örnek:

```env
GROQ_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///smartlead.db
AI_PROVIDER=groq
FLASK_CONFIG=development
CORS_ORIGINS=*
SECRET_KEY=your_secret_key
```

> `.env` dosyası güvenlik nedeniyle GitHub reposuna eklenmemelidir.

---

## Uygulamayı Çalıştırma

```bash
python run.py
```

Uygulama varsayılan olarak yerel Flask sunucusunda çalışır.

---

## Deployment

Backend uygulaması Render üzerinde deploy edilmiştir.

Render üzerinde kullanılan temel ayarlar:

```text
Build Command:
pip install -r requirements.txt

Start Command:
gunicorn run:app
```

Environment variables Render paneli üzerinden tanımlanmıştır.

---

## Canlı Bağlantılar

**Wix Demo:**  
https://sudebsahbaz.wixstudio.com/encoredemo

**Render Backend:**  
https://smartlead-ai-y2s0.onrender.com

**Render Yönetim Paneli:**  
https://smartlead-ai-y2s0.onrender.com/dashboard

**API Health Check:**  
https://smartlead-ai-y2s0.onrender.com/api/health

**GitHub Repository:**  
https://github.com/SudeBSahbaz/smartlead_ai

---

## Güvenlik

- API anahtarları kaynak kod içerisinde tutulmaz.
- Hassas bilgiler environment variable olarak saklanır.
- `.env` dosyası `.gitignore` içerisinde tutulur.
- Harici servis çağrılarında hata yönetimi uygulanır.

---

## Proje Akışı

```text
Kullanıcı
   ↓
Wix Studio B2C Arayüzü
   ↓
Wix Velo / wix-fetch
   ↓
Flask REST API (Render)
   ├── Groq AI API
   └── SQLite
          ↓
      Lead Verileri
          ↓
GET /api/leads
          ↓
Wix B2B Yönetim Paneli
```

---

## Geliştirici

**Sude Betül Şahbaz**

Computer Engineering  
Yeditepe University