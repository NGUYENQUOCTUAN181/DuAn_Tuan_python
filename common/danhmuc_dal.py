from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from common.delete_danhmuc import delete_danhmuc
from ketnoidb.ketnoi_mysql import get_connection   # ✅ nếu bạn dùng ketnoidb

def get_all_danhmuc():
    """
    Lấy toàn bộ danh sách danh mục trong bảng 'danhmuc'
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM danhmuc")
    rows = cur.fetchall()
    conn.close()
    return rows
