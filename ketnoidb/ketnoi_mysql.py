import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    Hàm kết nối MySQL và trả về đối tượng connection
    """
    try:
        conn = mysql.connector.connect(
            host='localhost',        # Địa chỉ MySQL
            user='root',             # Tên đăng nhập
            password='',       # Mật khẩu
            database='food_ordering_db'  # Tên database
        )
        if conn.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return conn
    except Error as e:
        print("❌ Lỗi kết nối MySQL:", e)
        return None
