# 🛠️ Scripts

Script hỗ trợ để duy trì repository này.

---

## `new-note.py` — Tạo ghi chú mới từ template

Tạo file ghi chú mới và tự động cập nhật tất cả file README index theo chuỗi thư mục.

### Yêu cầu

| Hệ điều hành | Trạng thái |
|--------------|-----------|
| macOS | ✅ Python 3 có sẵn mặc định |
| Ubuntu/Linux | ✅ Python 3 có sẵn mặc định |
| Windows | ⚠️ Cần cài [Python 3](https://www.python.org/downloads/) trước |

Kiểm tra bạn đang có Python 3:
```bash
python3 --version   # macOS / Linux
python --version    # Windows
```

### Cách dùng

Chạy từ **thư mục gốc** của repo:

```bash
python scripts/new-note.py <đường-dẫn> <tên-file> [tiêu-đề]
```

| Tham số | Bắt buộc | Mô tả |
|---------|----------|-------|
| `đường-dẫn` | ✅ | Đường dẫn folder tương đối trong repo (dùng forward slash) |
| `tên-file` | ✅ | Tên file **không có** `.md`. Phải là `chữ-thường-gạch-ngang` |
| `tiêu-đề` | tùy chọn | Tiêu đề hiển thị. Mặc định là Title Case của tên file |

### Ví dụ

```bash
# Tạo: fundamentals/data-structures/linked-list.md
python scripts/new-note.py fundamentals/data-structures linked-list "Danh sách liên kết"

# Tạo: topics/react/use-effect.md
python scripts/new-note.py topics/react use-effect "useEffect"

# Tạo: fundamentals/algorithms/binary-search.md (tiêu đề tự động)
python scripts/new-note.py fundamentals/algorithms binary-search
```

### Script làm gì

```
--> Đang tạo ghi chú: fundamentals/data-structures/linked-list.md
    Tiêu đề: Danh sách liên kết

  [OK] Đã tạo     fundamentals/data-structures/linked-list.md
  [OK] Cập nhật   fundamentals/data-structures/README.md
  [OK] Cập nhật   fundamentals/README.md
  [OK] Cập nhật   README.md

*** Xong! Mở file và bắt đầu viết:
    /đường/dẫn/đến/my-dev-notes/fundamentals/data-structures/linked-list.md
```

1. Tạo file ghi chú với template tiếng Việt đã điền sẵn
2. Thêm hàng vào `README.md` của **folder hiện tại** (tạo mới nếu chưa có)
3. Thêm hàng vào `README.md` của **section** (ví dụ: `fundamentals/README.md`)
4. Thêm hàng vào `README.md` **gốc**

> Các hàng được chèn qua anchor comment (`<!-- new-note: insert ... row above -->`).
> Các hàng đã tồn tại sẽ được bỏ qua tự động.
