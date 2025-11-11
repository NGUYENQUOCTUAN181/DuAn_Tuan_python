from ketnoidb.ketnoi_mysql import get_connection
from mysql.connector import Error

def insert_danhmuc(tendm, mota):
    """
    Hàm thêm danh mục mới vào bảng danhmuc
    Tham số:
        tendm (str): Tên danh mục
        mota (str): Mô tả danh mục
    """
    conn = get_connection()
    if conn is None:
        print("❌ Không thể kết nối CSDL.")
        return

    try:
        cursor = conn.cursor()
        # Câu lệnh SQL đúng theo cấu trúc bảng của bạn
        sql = "INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)"
        values = (tendm, mota)
        cursor.execute(sql, values)
        conn.commit()

        print("✅ Thêm danh mục thành công!")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("🔌 Đã đóng kết nối MySQL.")
