from ketnoidb.ketnoi_mysql import get_connection
from mysql.connector import Error

def delete_danhmuc(id_danhmuc):
    """
    Hàm xóa danh mục khỏi bảng 'danhmuc' theo id
    Tham số:
        id_danhmuc (int): ID của danh mục cần xóa
    """
    conn = get_connection()
    if conn is None:
        print("❌ Không thể kết nối CSDL.")
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        cursor.execute(sql, (id_danhmuc,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có ID = {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {id_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("🔌 Đã đóng kết nối MySQL.")
