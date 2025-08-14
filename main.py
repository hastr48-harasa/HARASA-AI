from flask import Flask, render_template, request
from groq import Groq
import os
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

app = Flask(__name__)

# Mengambil API Key dari environment variable yang sudah dimuat.
AI_KEY = os.getenv("GROQ_API_KEY")

# Validasi API Key
if not AI_KEY:
    raise ValueError("GROQ_API_KEY tidak ditemukan. Pastikan Anda sudah membuat file .env dan mengisinya.")

client = Groq(api_key=AI_KEY)

def get_ai_definition(term):
    """Fungsi untuk memanggil Groq API dan mendapatkan definisi."""
    try:
        prompt_content = (
            f"Jelaskan terminologi '{term}' dalam lingkup ilmu pangan, teknologi pangan, dan rekayasa pangan (food science, food technology, & food engineering) "
            f"Jelaskan istilah '{term}' secara singkat, padat, dan akurat dari sudut pandang keahlian Anda. "
            f"Gunakan bahasa yang mudah dimengerti oleh orang awam namun tetap menunjukkan kedalaman pengetahuan Anda sebagai seorang ahli."

        )
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt_content}
            ],
            model="llama-3.1-8b-instant"
        )
        definition = chat_completion.choices[0].message.content
        return definition
    except Exception as e:
        print("="*35)
        print("GAGAL MEMANGGIL API, ERROR ASLI:")
        print(e)
        print("="*35)
        return "Gagal mendapatkan jawaban dari AI. Cek terminal untuk detail error."

# Route utama sekarang untuk halaman pembuka
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Route untuk kamus dipindahkan ke /kamus
@app.route('/kamus', methods=['GET', 'POST'])
def food_dictionary():
    # Variabel default
    search_term = None
    definition = None
    
    if request.method == 'POST':
        # Ambil data dari form saat tombol di-klik
        search_term = request.form.get('istilah')
        
        # Panggil AI hanya jika ada istilah yang dimasukkan
        if search_term:
            definition = get_ai_definition(search_term)

    # Tampilkan halaman kamus dengan data yang sudah diisi
    return render_template('kamus.html', istilah=search_term, definisi=definition)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
