import json
import os
import sys
import urllib.error
import urllib.request

MESSAGES = {
    "1": "Absen cuyy!! segera buat thread dan kirim SS yaa 👇",
    "2": (
        "yokk mulai SPAM call attempt, segera buat thread pinjam CRM siapa"
        " yaa 👇"
    ),
    "3": (
        "FU TIME 🔥🔥\n\n"
        "segera simak thread ya untuk priority dan mekanisme FU today !!\n"
        "sekarang all team sudah include perform dan belum ada buffer, "
        "jadi datamu tanggung jawabmu ya. perbantuan tidak bisa se intens dulu\n\n"
        "mekanisme :\n"
        "priority 70% wajib di touch dulu\n"
        "pengulangan menggunakan filter CRM risk tier "
        "(1,2,90,62,50,22,65) copy paste angka tsb langsung di CRM"
    ),
    "4": (
        "SEMANGATTT PAGIII para pejuang cuann💸💸\n\n"
        "awali pagi dengan bismillah, jangan sampai amount&account "
        "PTP/LM merah semua (raih promise sebanyak mungkin) dan pastikan "
        "tiap kata HALO kalian tidak terbuang sia2 dan wajib jadi PTP/LM!!\n\n"
        "selalu ingat 🕵️\n"
        "- script 8.8\n"
        '"dari SPayLater, mau dihubungi diluar jam kerja utk penagihan '
        'SPaylater/SPinjam agar denda tak nambah, PAK PRAPTO?"\n'
        "jika menolak input CBL.\n"
        "jika jawaban user mau melakukan pembayaran berarti script 8.8 "
        "gugur langsung script tagihan.\n"
        "- JANGAN BUANG DATA 5sc APAPUN YG TERJADI TERMASUK MV\n"
        "- jangan sampai salah klik tgl PROLONG, CBD dan nominal Partial. "
        "pastikan sebelum submit klik baik. SAYANGI insentivemu!\n\n"
        "fokus fokus fokus"
    ),
    "5": (
        "🚨 saatnya script 8.8\n"
        '"dari SPayLater, mau dihubungi diluar jam kerja utk penagihan '
        'SPaylater/SPinjam agar denda tak nambah, PAK PRAPTO?"'
    ),
}


def send_seatalk_message(webhook_url, content_text):
    payload = {
        "tag": "text",
        "text": {"content": content_text, "at_all": True},
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url, data=data, headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            response_body = response.read().decode("utf-8")
            print(f"HTTP Status Code: {status}")
            print(f"SeaTalk Server Response: {response_body}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"An execution error occurred: {e}")


def main():
    webhook_url = os.environ.get("SEATALK_WEBHOOK_URL")
    if not webhook_url:
        print("Error: SEATALK_WEBHOOK_URL environment variable is missing.")
        return

    if len(sys.argv) < 2:
        print(
            "Error: Harap masukkan argumen pesan "
            "(contoh: python send_reminder.py 1)"
        )
        return

    pilihan = sys.argv[1]
    pesan = MESSAGES.get(pilihan)

    if pesan:
        print(f"Memproses Reminder {pilihan}...")
        send_seatalk_message(webhook_url, pesan)
    else:
        daftar_valid = ", ".join(f"'{k}'" for k in MESSAGES.keys())
        print(
            f"Error: Argumen '{pilihan}' tidak dikenali. "
            f"Gunakan angka {daftar_valid}."
        )


if __name__ == "__main__":
    main()
