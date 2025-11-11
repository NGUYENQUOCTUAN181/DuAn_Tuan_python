from ketnoidb.ketnoi_mysql import get_connection
from mysql.connector import Error

def update_danhmuc(id_danhmuc, tendm_moi, mota_moi):
    """
    Hàm cập nhật thông tin danh mục trong bảng 'danhmuc'
    Tham số:
        id_danhmuc (int): ID danh mục cần cập nhật
        tendm_moi (str): Tên danh mục mới
        mota_moi (str): Mô tả mới
    """
    conn = get_connection()
    if conn is None:
        print("❌ Không thể kết nối CSDL.")
        return

    try:
        cursor = conn.cursor()
        sql = "UPDATE danhmuc SET tendm = %s, mota = %s WHERE id = %s"
        cursor.execute(sql, (tendm_moi, mota_moi, id_danhmuc))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Cập nhật danh mục ID = {id_danhmuc} thành công!")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {id_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("🔌 Đã đóng kết nối MySQL.")
