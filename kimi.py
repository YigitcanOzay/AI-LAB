import os
from openai import OpenAI
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()

# .env yüklemesini ve anahtarı kontrol et
load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    print("Hata: NVIDIA_API_KEY bulunamadı! .env dosyasını kontrol et.")
    exit()

print(f"Bağlantı kuruluyor... (Anahtar: {api_key[:5]}***)")

# OpenAI istemcisini NVIDIA ayarlarıyla başlat
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_API_KEY")
)
# ... (importlar aynı)
completion = client.chat.completions.create(
  model="moonshotai/kimi-k2-instruct",
  messages=[{"role":"user", "content": "Selam, bağlantı testi yapıyoruz."}],
  stream=False, # Akışı kapatalım
  timeout=60.0   # Süreyi 60 saniyeye çıkaralım
)
print(completion.choices[0].message.content)