import requests
from datetime import datetime, timedelta

def get_jadwal(kota, tanggal):
    # Format tanggal harus DD-MM-YYYY
    url = f"https://api.aladhan.com/v1/timingsByCity/{tanggal}?city={kota}&country=Indonesia&method=20"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["data"]
    except Exception as e:
        print(f"Gagal mengambil data: {e}")
        return None

print("=" * 40)
print(" APLIKASI JADWAL SHOLAT & HIJRIAH ")
print("=" * 40)

kota = input("Masukkan nama kota: ")

# Mendapatkan tanggal hari ini dan besok
hari_ini = datetime.now().strftime("%d-%m-%Y")
besok = (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y")

daftar_tanggal = [
    ("HARI INI", hari_ini),
    ("BESOK", besok)
]

for label, tgl in daftar_tanggal:
    data = get_jadwal(kota, tgl)
    
    if data:
        jadwal = data["timings"]
        hijri = data["date"]["hijri"]
        
        print(f"\n[{label} - {tgl}]")
        print(f"Kalender Hijriah: {hijri['day']} {hijri['month']['en']} {hijri['year']} H")
        print("-" * 20)
        print(f"-> Subuh   : {jadwal['Fajr']}")
        print(f"-> Dzuhur  : {jadwal['Dhuhr']}")
        print(f"-> Ashar   : {jadwal['Asr']}")
        print(f"-> Maghrib : {jadwal['Maghrib']}")
        print(f"-> Isya    : {jadwal['Isha']}")
        print("-" * 20)

print("\nAyo sholat!")