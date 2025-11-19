# storage.py
import json
import os

DATA_FILE = "buku_tamu.json"

def load_data():
    """Memuat isi JSON (jika file tidak ada, buat data kosong)."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    """Menyimpan data ke file JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
