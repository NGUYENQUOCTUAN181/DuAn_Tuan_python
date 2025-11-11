from ketnoidb.ketnoi_mysql import get_connection
from mysql.connector import Error

def get_all_danhmuc():
    """
    Hàm lấy toàn bộ danh mục từ bảng 'danhmuc'
    Trả về danh sách các dòng (list of tuples)
    """
    conn = get_connection()
    if conn is None:
        print("❌ Không thể kết nối CSDL.")
        return []

    danh_sach = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, tendm, mota FROM danhmuc")
        danh_sach = cursor.fetchall()

        if len(danh_sach) == 0:
            print("⚠️ Chưa có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("📋 Danh sách danh mục:")
            for row in danh_sach:
                print(f"ID: {row[0]} | Tên: {row[1]} | Mô tả: {row[2]}")
    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("🔌 Đã đóng kết nối MySQL.")

    return danh_sach
