    elif pilihan == "4":
        pesan = (
            "SEMANGATTT PAGIII para pejuang cuann💸💸\n\n"
            "awali pagi dengan bismillah, jangan sampai amount&account PTP/LM merah semua (raih promise sebanyak mungkin) dan pastikan tiap kata HALO kalian tidak terbuang sia2 dan wajib jadi PTP/LM!!\n\n"
            "selalu ingat 🕵️\n"
            "- script 8.8\n"
            "\"Dari spaylater penelponannya direkam, bersedia dihubungi diluar jam kerja agar denda tidak makin membesar ya?\"\n"
            "jika menolak input CBL.\n"
            "jika jawaban user mau melakukan pembayaran berarti script 8.8 gugur langsung script tagihan.\n"
            "- JANGAN BUANG DATA 5sc APAPUN YG TERJADI TERMASUK MV\n"
            "- jangan sampai salah klik tgl PROLONG, CBD dan nominal Partial. pastikan sebelum submit klik baik. SAYANGI insentivemu! \n\n"
            "fokus fokus fokus"
        )
        print("Memproses Reminder 4...")
        send_seatalk_message(webhook_url, pesan)

    elif pilihan == "5":
        pesan = (
            "🚨 saatnya **script 8.8**\n"
            "\"Dari spaylater penelponannya direkam, bersedia dihubungi diluar jam kerja agar denda tidak makin membesar ya?\""
        )
        print("Memproses Reminder 5...")
        send_seatalk_message(webhook_url, pesan)
        
    else:
        print(f"Error: Argumen '{pilihan}' tidak dikenali. Gunakan angka '1', '2', '3', '4', atau '5'.")
