# 📜 Quy tắc & Quy ước

File này định nghĩa **tất cả quy tắc** cho repository này.
Dù tôi tự viết hay nhờ trợ giúp — mọi thứ phải tuân theo hướng dẫn này.

> **Kiên trì hơn tần suất.** Không có áp lực phải viết mỗi ngày.
> Viết khi nào bạn học được điều gì đáng ghi lại — kể cả một lần mỗi tuần cũng có giá trị.

---

## 1. Ngôn ngữ

- **Toàn bộ nội dung viết bằng tiếng Việt.**
- Giữ ngôn ngữ **đơn giản và rõ ràng** — viết như đang giải thích cho junior developer.
- Tên file, tên folder, và lệnh git giữ nguyên tiếng Anh.

---

## 2. Cấu trúc folder

```
my-dev-notes/
├── topics/                  # Tech-specific knowledge
│   ├── <topic-name>/
│   │   ├── README.md        # REQUIRED: index/overview of this topic
│   │   └── <subtopic>.md    # One file per focused subtopic
│   └── README.md            # Index of all topics
│
└── fundamentals/            # Language-agnostic CS concepts
    ├── algorithms/
    │   ├── README.md
    │   └── <algorithm>.md   # e.g., binary-search.md, bubble-sort.md
    ├── data-structures/
    │   ├── README.md
    │   └── <structure>.md   # e.g., linked-list.md, hash-table.md
    ├── networking/
    │   ├── README.md
    │   └── <concept>.md
    ├── system-design/
    │   ├── README.md
    │   └── <concept>.md
    └── README.md            # Index of all fundamentals categories
```

### Folder `topics/`
- Dành cho ghi chú về **công nghệ, công cụ, hoặc framework cụ thể** (ví dụ: React, Docker, PostgreSQL).
- Mỗi công nghệ có **subfolder riêng**.
- Mỗi subfolder **bắt buộc** có `README.md` làm tổng quan/index.
- Tách thành nhiều file `.md` khi topic phình to (ví dụ: `hooks.md`, `state-management.md`).

### Folder `fundamentals/`
- Dành cho kiến thức **Khoa học Máy tính không phụ thuộc ngôn ngữ**, áp dụng được với mọi tech stack.
- Tổ chức theo **subfolder danh mục** (algorithms, data-structures, networking, system-design, security...).
- Mỗi subfolder có `README.md` riêng.
- Mỗi khái niệm trong subfolder là **một file `.md` duy nhất**.
- Tạo subfolder mới khi một danh mục có (hoặc sẽ có) nhiều hơn một ghi chú.

---

## 3. Đặt tên file

| Quy tắc | Ví dụ |
|---------|-------|
| Tất cả **chữ thường** | ✅ `event-loop.md` ❌ `EventLoop.md` |
| Dùng **dấu gạch ngang** (không dùng underscore hay khoảng trắng) | ✅ `data-types.md` ❌ `data_types.md` |
| Tên phản ánh **nội dung**, không phải ngày tháng | ✅ `closures.md` ❌ `2026-09-26.md` |
| Giữ tên **ngắn nhưng mô tả đủ ý** | ✅ `async-await.md` ❌ `ghi-chu-ve-async-await-trong-js.md` |

---

## 4. Cấu trúc nội dung file

Mỗi file ghi chú `.md` nên theo template này, dùng cách tiếp cận **"Tại sao trước"**:

```markdown
# <Tiêu đề>

## Tại sao nó ra đời?
<!--
  Bắt đầu từ đây. Trả lời những câu hỏi này:
  - Vấn đề gì tồn tại TRƯỚC khi nó được tạo ra?
  - "Nỗi đau" nào nó giải quyết cho developer?
  - Tại sao nó được phát minh / nó lấp đầy khoảng trống nào?
  Nghĩ theo hướng: "Nếu không có nó, developer phải chịu đựng X..."
-->

## Nó là gì?
<!-- Bây giờ định nghĩa rõ ràng bằng lời của bạn, trong bối cảnh trên. -->

## Nó hoạt động thế nào?
<!-- Giải thích cơ chế, nội tại, mô hình tư duy. -->

## Ví dụ
<!-- Code block hoặc ví dụ thực tế giúp mọi thứ trở nên cụ thể. -->

## Tóm tắt
<!-- 3-5 bullet points: những điều quan trọng nhất cần nhớ. -->

## Tài liệu tham khảo
<!-- Links đến bài viết, docs, hoặc video đã giúp bạn hiểu. -->
```

> **Lưu ý:** Không phải mọi phần đều bắt buộc. Bỏ qua phần không áp dụng,
> nhưng **luôn có ít nhất `Tại sao nó ra đời?` và `Ví dụ`** — hai phần này là nền tảng của ghi chú.

---

## 5. README.md trong mỗi folder topic

Mỗi folder topic phải có `README.md` đóng vai trò **mục lục**:

```markdown
# <Tên công nghệ>

> Mô tả một dòng về công nghệ này là gì.

## Danh sách ghi chú

| File | Mô tả |
|------|-------|
| [closures.md](./closures.md) | Closure hoạt động thế nào và tại sao quan trọng |
| [event-loop.md](./event-loop.md) | Hiểu mô hình async single-threaded của JS |
```

Cập nhật file này mỗi khi bạn thêm ghi chú mới vào folder.

---

## 6. Định dạng commit message

Lịch sử Git commit là **nhật ký học tập hằng ngày** của repository này.
Một commit được viết tốt = một bản ghi về những gì đã học ngày hôm đó.

### Định dạng

```
<loại>(<topic>): <mô tả ngắn — viết như tiêu đề>

- Điểm chính 1
- Điểm chính 2
- Điểm chính 3
- Ref: https://link-to-source.com
```

### Các loại commit

| Loại | Khi nào dùng |
|------|--------------|
| `note` | Thêm ghi chú hoặc khái niệm mới |
| `update` | Mở rộng hoặc sửa ghi chú hiện có |
| `struct` | Tổ chức lại folder, đổi tên file |
| `fix` | Sửa lỗi thực tế hoặc lỗi chính tả trong ghi chú |
| `chore` | Cập nhật README, CONTRIBUTING, hoặc file meta khác |

### Quy tắc cho dòng subject
- Dùng **thể mệnh lệnh**: `note(react): hiểu cách cleanup của useEffect` ✅ (không phải "đã hiểu" hay "đang hiểu")
- Giữ **dưới 72 ký tự**
- `<topic>` nên khớp với **tên folder** (ví dụ: `react`, `docker`, `networking`)
- **KHÔNG ghi ngày** vào subject — Git tự đánh dấu thời gian

### Ví dụ

```
note(javascript): hiểu closure và lexical scope

- Closure vẫn truy cập được scope bên ngoài dù hàm ngoài đã return
- Biến được capture by reference, không phải by value
- Pattern phổ biến: factory function, đóng gói dữ liệu, memoization
- Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
```

```
note(networking): DNS phân giải tên miền như thế nào

- DNS dịch tên miền thành địa chỉ IP
- Thứ tự phân giải: browser cache → OS cache → Resolver → Root → TLD → Authoritative
- TTL kiểm soát thời gian cache bản ghi
- Ref: https://howdns.works
```

```
update(react): thêm ví dụ cho ghi chú useCallback

- Thêm so sánh giữa useMemo và useCallback
- Làm rõ khi nào KHÔNG nên dùng useCallback (tối ưu hóa sớm)
```

```
struct: tổ chức lại folder docker thành các file con

- Tách docker.md thành: basics.md, networking.md, compose.md
- Cập nhật index topics/docker/README.md
```

---

## 7. Checklist trước khi commit

- [ ] Nội dung viết bằng **tiếng Việt**
- [ ] File đặt tên bằng **chữ thường và dấu gạch ngang**
- [ ] File theo đúng **cấu trúc template**
- [ ] **README.md của folder** đã được cập nhật
- [ ] Commit message theo đúng **định dạng quy định**
