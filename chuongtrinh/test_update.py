from common.update_danhmuc import update_danhmuc

while True:
    try:
        id_dm = int(input("Nhập ID danh mục cần cập nhật: "))
        tendm = input("Nhập tên danh mục mới: ")
        mota = input("Nhập mô tả mới: ")

        update_danhmuc(id_dm, tendm, mota)
    except ValueError:
        print("⚠️ ID phải là số nguyên!")

    con = input("TIẾP TỤC CẬP NHẬT (y), THOÁT THÌ NHẤN KÝ TỰ BẤT KỲ: ")
    if con.lower() != "y":
        break

