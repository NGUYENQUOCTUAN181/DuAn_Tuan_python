from common.insertdanhmuc import insert_danhmuc

while True:
    tendm = input("Nhập vào tên danh mục: ")
    mota = input("Nhập vào mô tả: ")

    # Gọi hàm chèn dữ liệu
    insert_danhmuc(tendm, mota)

    con = input("TIẾP TỤC (y), THOÁT THÌ NHẤN KÝ TỰ BẤT KỲ: ")
    if con.lower() != "y":
        break
