import mysql.connector
from mysql.connector import Error
# this is a update 

def main():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="food_ordering_db"
        )
        if conn.is_connected():
            print("✅ Kết nối MySQL thành công!")
    except Error as e:
        print("❌ Lỗi kết nối MySQL:", e)
        return

    cursor = conn.cursor()

    while True:
        print("\n--- Thêm danh mục thuốc ---")
        tendm = input("Tên danh mục: ")
        mota = input("Mô tả danh mục: ")

        try:
            cursor.execute("INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)", (tendm, mota))
            conn.commit()
            print(f"✅ Đã thêm danh mục: {tendm}")
        except Error as e:
            print("❌ Lỗi khi thêm danh mục:", e)

        con = input("TIẾP TỤC nhấn 'y', THOÁT nhấn ký tự bất kỳ: ")
        if con.lower() != "y":
            break

    cursor.close()
    conn.close()
    print("🔒 Đã đóng kết nối MySQL.")

if __name__ == "__main__":
    main()
