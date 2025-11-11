import tkinter as tk
from tkinter import ttk, messagebox
from common.danhmuc_dal import insert_danhmuc, update_danhmuc, delete_danhmuc, get_all_danhmuc

def load_data():
    for i in tree.get_children():
        tree.delete(i)
    for row in get_all_danhmuc():
        tree.insert("", "end", values=row)

def them():
    tendm = tendm_entry.get().strip()
    mota = mota_entry.get("1.0", tk.END).strip()
    if not tendm:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục")
        return
    insert_danhmuc(tendm, mota)
    load_data()
    messagebox.showinfo("Thành công", "Đã thêm danh mục mới")

def xoa():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để xóa")
        return
    data = tree.item(selected, "values")
    delete_danhmuc(data[0])
    load_data()
    messagebox.showinfo("Thành công", "Đã xóa danh mục")

def sua():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục để sửa")
        return
    data = tree.item(selected, "values")
    id = data[0]
    tendm = tendm_entry.get().strip()
    mota = mota_entry.get("1.0", tk.END).strip()
    if not tendm:
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục")
        return
    update_danhmuc(id, tendm, mota)
    load_data()
    messagebox.showinfo("Thành công", "Đã cập nhật danh mục")

def on_select(event):
    selected = tree.focus()
    if not selected:
        return
    data = tree.item(selected, "values")
    tendm_entry.delete(0, tk.END)
    tendm_entry.insert(0, data[1])
    mota_entry.delete("1.0", tk.END)
    mota_entry.insert("1.0", data[2])

root = tk.Tk()
root.title("Quản lý Danh Mục")
root.geometry("700x500")

# Input fields
tk.Label(root, text="Tên danh mục:").place(x=30, y=20)
tendm_entry = tk.Entry(root, width=40)
tendm_entry.place(x=150, y=20)

tk.Label(root, text="Mô tả:").place(x=30, y=60)
mota_entry = tk.Text(root, width=50, height=5)
mota_entry.place(x=150, y=60)

# Buttons
tk.Button(root, text="➕ Thêm", width=10, command=them).place(x=550, y=20)
tk.Button(root, text="📝 Sửa", width=10, command=sua).place(x=550, y=60)
tk.Button(root, text="❌ Xóa", width=10, command=xoa).place(x=550, y=100)

# Table
columns = ("id", "tendm", "mota")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.column("id", width=50)
tree.column("tendm", width=200)
tree.column("mota", width=300)
tree.place(x=30, y=200, width=630, height=250)
tree.bind("<<TreeviewSelect>>", on_select)

load_data()
root.mainloop()
