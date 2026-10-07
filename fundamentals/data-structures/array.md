# Mảng (Array)

## Tại sao nó ra đời?
Trong lúc code, ta thường dùng biến để lưu trữ giá trị.
Nhưng có những trường hợp ta cần lưu **một danh sách các giá trị cùng kiểu** có ý nghĩa như nhau —
nếu dùng từng biến riêng lẻ thì rất lãng phí và khó quản lý.
Array sinh ra để giải quyết vấn đề này: một cấu trúc duy nhất chứa cả tập hợp các giá trị liên quan.

## Nó là gì?
Array là một **cấu trúc dữ liệu tuyến tính** lưu trữ một tập hợp các phần tử với các đặc điểm sau:
- Tất cả phần tử phải **cùng kiểu dữ liệu** (ví dụ: toàn `int`, toàn `string`)
- Các phần tử được lưu ở các **ô nhớ liên tiếp nhau**
- Các phần tử được **đánh số (index) bắt đầu từ 0**
- Array có **kích thước cố định** — phải khai báo kích thước khi tạo
  *(Mảng động trong các ngôn ngữ hiện đại thực chất vẫn dùng mảng cố định bên dưới, chỉ là được xử lý tự động)*

## Nó hoạt động thế nào?
Vì các phần tử được lưu ở **ô nhớ liên tiếp**, máy tính chỉ cần biết:
- **Địa chỉ của phần tử đầu tiên** (base address)
- **Index** (khoảng dịch so với vị trí đầu)

→ Có thể nhảy thẳng đến bất kỳ phần tử nào trong **O(1)**.

Các thao tác trên array xoay quanh **3 nhóm cốt lõi** dựa trên cơ chế tính địa chỉ này:

### 1. Đọc / Ghi — O(1)
Nhảy thẳng đến ô nhớ cần thiết bằng `base address + index`. Rất nhanh.

### 2. Thêm / Xóa
- Thêm vào **cuối** (còn chỗ trống): O(1) — chỉ cần ghi vào ô tiếp theo.
- Thêm/xóa ở **đầu hoặc giữa**: O(n) — phải dịch chuyển toàn bộ phần tử phía sau để nhường/lấp chỗ.

### 3. Mảng động (bên dưới)
Khi mảng động (ví dụ: `Array` trong JavaScript, `list` trong Python, `vector` trong C++) bị đầy:
1. Hệ thống cấp phát một mảng mới lớn hơn (thường **gấp đôi kích thước**)
2. Toàn bộ phần tử được **sao chép** sang mảng mới
3. Phần tử mới được thêm vào

Bước copy tốn O(n) nhưng hiếm xảy ra, nên chi phí trung bình (*amortized*) vẫn gần O(1).

## Ví dụ

**Mảng cố định trong Java** (minh họa kích thước cố định và kiểu dữ liệu cố định):

```java
// Khai báo mảng 5 số nguyên
int[] numbers = new int[5];

// 1. Ghi — O(1)
numbers[0] = 10;
numbers[1] = 20;
numbers[2] = 30;

// 2. Đọc — O(1)
System.out.println(numbers[1]); // Kết quả: 20

// 3. Thêm vào cuối (ô index 3 còn trống) — O(1)
numbers[3] = 40;

// 4. Chèn vào giữa (chèn số 15 vào index 1) — O(n)
// Phải dịch chuyển các phần tử sang phải trước
numbers[4] = numbers[3]; // Dịch 40 → index 4
numbers[3] = numbers[2]; // Dịch 30 → index 3
numbers[2] = numbers[1]; // Dịch 20 → index 2
numbers[1] = 15;         // Chèn 15 vào index 1
```

## Tóm tắt

- Array lưu phần tử ở **ô nhớ liên tiếp** → truy cập ngẫu nhiên theo index **O(1)**.
- **Đọc/Ghi rất nhanh** (O(1)), nhưng **chèn/xóa ở giữa chậm** (O(n)) do phải dịch chuyển phần tử.
- Array có **kích thước cố định**; mảng động tự resize bằng cách copy sang mảng lớn hơn (amortized O(1)).
- Nên dùng khi: biết trước kích thước, thao tác chủ yếu là **tra cứu theo index**.
- Không nên dùng khi: thường xuyên **chèn hoặc xóa** ở đầu hoặc giữa.

## Tài liệu tham khảo

- [Array Data Structure — GeeksforGeeks](https://www.geeksforgeeks.org/array-data-structure/)
- [Array — MDN Web Docs (JavaScript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)