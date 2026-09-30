# 📓 Note technicals của hieungocdinh

> Kho kiến thức cá nhân — nơi tôi ghi lại những gì học được mỗi ngày với tư cách là một developer.

---

## 🎯 Mục đích

Repository này là **"bộ não thứ hai"** của tôi về lập trình.
Thay vì quên những gì đã đọc, tôi viết lại — bằng lời của mình, với ví dụ của mình.

- **Kiên trì hơn hoàn hảo** — Một ghi chú ngắn mỗi ngày tốt hơn một ghi chú dài mỗi tháng.
- **Git commit như nhật ký học tập** — Mỗi commit ghi lại câu chuyện của ngày hôm đó.
- **Tổ chức theo chủ đề** — Dễ tìm, dễ ôn lại.

---

## 📁 Cấu trúc

```
my-dev-notes/
├── README.md              # Bạn đang ở đây — trang chủ & điều hướng
├── CONTRIBUTING.md        # Quy tắc: cách viết, đặt tên file, format commit
├── .gitmessage            # Template cho commit message
│
├── scripts/               # Script hỗ trợ (new-note.py...)
│
├── topics/                # Kiến thức về công nghệ cụ thể (React, Docker, SQL...)
│   └── README.md          # Danh sách tất cả topics
│
└── fundamentals/          # Kiến thức CS không phụ thuộc vào công nghệ nào
    └── README.md          # Danh sách tất cả fundamentals
```

---

## 🗺️ Điều hướng

### 🔧 Topics
Ghi chú về công nghệ cụ thể. Mỗi folder = một công nghệ hoặc công cụ.

| Chủ đề | Mô tả |
|--------|-------|
<!-- new-note: insert topics row above -->

→ [Xem tất cả topics](./topics/README.md)

---

### 📐 Fundamentals
Kiến thức Khoa học Máy tính cốt lõi, không phụ thuộc vào bất kỳ công nghệ nào.

| Chủ đề | Mô tả |
|--------|-------|
| [Cấu trúc dữ liệu](./fundamentals/data-structures/README.md) | Mảng, danh sách liên kết, cây, bảng băm, đồ thị... |
<!-- new-note: insert fundamentals row above -->

→ [Xem tất cả fundamentals](./fundamentals/README.md)

---

## 📋 Quy tắc & Quy ước

Trước khi thêm ghi chú (hoặc để nhắc lại cách mọi thứ hoạt động):

→ [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 🛠️ Scripts

Để tạo ghi chú mới và tự động cập nhật tất cả README:

```bash
python scripts/new-note.py <đường-dẫn> <tên-file> [tiêu-đề]

# Ví dụ:
python scripts/new-note.py fundamentals/data-structures linked-list "Danh sách liên kết"
python scripts/new-note.py topics/react use-effect "useEffect"
```

→ [scripts/README.md](./scripts/README.md) — tài liệu đầy đủ

---

## 📅 Nhật ký học tập

Hoạt động học tập hằng ngày của tôi được theo dõi qua **lịch sử Git commit**.
Mỗi commit message theo một định dạng chuẩn để dễ dàng đọc lại.

→ [Xem lịch sử commit trên GitHub](../../commits/main)

---
