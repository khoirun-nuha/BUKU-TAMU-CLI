# service.py
from datetime import datetime
from storage import load_data, save_data


def tambah_tamu(nama, alamat, keperluan):
    data = load_data()

    tamu = {
        "id": int(datetime.now().timestamp()),
        "nama": nama,
        "alamat": alamat,
        "keperluan": keperluan,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(tamu)
    save_data(data)
    return tamu


def list_tamu():
    return load_data()


def cari_tamu(keyword):
    keyword = keyword.lower()
    data = load_data()
    return [t for t in data if keyword in t["nama"].lower() or keyword in t["keperluan"].lower()]


def edit_tamu(id_tamu, nama=None, alamat=None, keperluan=None):
    data = load_data()

    for tamu in data:
        if str(tamu["id"]) == str(id_tamu):
            if nama: tamu["nama"] = nama
            if alamat: tamu["alamat"] = alamat
            if keperluan: tamu["keperluan"] = keperluan

            save_data(data)
            return tamu

    return None


def hapus_tamu(id_tamu):
    data = load_data()
    baru = [t for t in data if str(t["id"]) != str(id_tamu)]

    if len(baru) == len(data):
        return False  # tidak ada yang dihapus

    save_data(baru)
    return True
