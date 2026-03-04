import os
import requests

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def buscar_y_enviar():
    # --- CONFIGURÁ AQUÍ LOS DATOS DE CAROLINA ---
    puesto = "PONER_AQUÍ_EL_PUESTO" 
    zona = "CABA"
    # --------------------------------------------
    
    query = f"site:bumeran.com.ar OR site:linkedin.com/jobs '{puesto}' {zona}"
    url_google = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    mensaje = (
        f"🚀 *Reporte Diario - Perfil: {puesto}*\n\n"
        f"📍 *Zona:* {zona}\n\n"
        f"🔗 [VER VACANTES DE HOY]({url_google})\n"
    )
    
    url_tg = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    requests.post(url_tg, json=payload)

if __name__ == "__main__":
    buscar_y_enviar()
