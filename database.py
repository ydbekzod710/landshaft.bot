import sqlite3
import os

def init_db():
    # Eski bazani o'chirib yuborib, yangidan toza holatda ochamiz
    if os.path.exists("gardening.db"):
        os.remove("gardening.db")
        
    conn = sqlite3.connect("gardening.db")
    cursor = conn.cursor()
    
    # Manzarali daraxtlar jadvali
    cursor.execute("""CREATE TABLE IF NOT EXISTS trees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        price TEXT,
        photo_id TEXT
    )""")

    # Dekorativ toshlar jadvali
    cursor.execute("""CREATE TABLE IF NOT EXISTS stones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        price TEXT,
        photo_id TEXT
    )""")

    # Toshlar dekoratsiyasi rasmlari
    cursor.execute("""CREATE TABLE IF NOT EXISTS stone_decorations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        photo_id TEXT,
        caption TEXT
    )""")

    # Portfolio (Bajarilgan loyihalar)
    cursor.execute("""CREATE TABLE IF NOT EXISTS portfolio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        photo_id TEXT,
        caption TEXT
    )""")
    
    # Ionomus ma'lumotlarini qo'shish (4 ta qiymat to'g'ri taqsimlandi)
    cursor.execute(
        "INSERT INTO trees (name, description, price, photo_id) VALUES (?, ?, ?, ?)",
        (
            "Eonymus japonicus 'Bravo' (Ionomus)",
            "Barglarining cheti oqish va sarg'ish hoshiyali, doim yashil bo'ladigan juda ko'rkam manzarali buta. Landshaft dizaynida gulzorlarga o'zgacha ko'rk beradi. \n 2.800.000so'm ",
            "2.800.000 so'm",
            "https://hermie.com/media/ab/ff/cd/1731818435/a988b7c9c8f6b82f6083c97cdb981443.jpg?ts=1734425513"
        )
    )
    
    conn.commit()
    conn.close()

# Funksiyani chaqiramiz
if __name__ == "__main__":
    init_db()