import os
import requests

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def buscar_y_enviar():
    # --- CONFIGURACIÓN PERFIL PAOLA CAROLINA FERRAGUT ---
    puestos = "('Analista Senior Microbiologia' OR 'Control de Calidad Farmaceutico' OR 'Biotecnologo')"
    zonas = "(Pilar OR Garin OR Escobar OR CABA)"
    
    query = f"site:bumeran.com.ar OR site:linkedin.com/jobs {puestos} {zonas} GMP"
    url_google = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    mensaje = (
        "🔬 *¡Hola Carolina! Reporte diario de vacantes:*\n\n"
        "📌 *Perfil:* Senior Microbiología / QC Farmacéutico\n"
        "📍 *Zonas:* Pilar, Garín, Escobar y CABA\n"
        "⚙️ *Filtro:* Normas GMP / Control de Calidad\n\n"
        f"🔗 [VER VACANTES DE HOY]({url_google})\n\n"
        "⚠️ _Revisá las publicaciones de las últimas 24hs._"
    )
    
    url_tg = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url_tg, json=payload)
        if response.status_code == 200:
            print("Mensaje enviado con éxito")
        else:
            print(f"Error de Telegram: {response.text}")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    buscar_y_enviar()
