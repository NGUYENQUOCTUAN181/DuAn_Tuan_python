from common.delete_danhmuc import delete_danhmuc

while True:
    try:
        id_dm = int(input("Nhập ID danh mục cần xóa: "))
        delete_danhmuc(id_dm)
    except ValueError:
        print("⚠️ ID phải là số nguyên!")

    con = input("TIẾP TỤC XÓA (y), THOÁT THÌ NHẤN KÝ TỰ BẤT KỲ: ")
    if con.lower() != "y":
        break
