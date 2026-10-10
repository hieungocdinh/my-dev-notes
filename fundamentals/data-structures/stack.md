# Ngăn xếp (Stack)
## Tại sao nó ra đời?
<!-- Vấn đề gì tồn tại TRƯỚC khi có nó? Nỗi đau nào nó giải quyết? -->

### 1. Bối cảnh lịch sử
- **Thời sơ khai (ENIAC, ~1945):** Máy tính được lập trình bằng cách cắm dây vật lý, chương trình chưa được lưu trong bộ nhớ.
- **Thời kỳ chương trình lưu trữ (EDSAC, 1949):** Xuất hiện nhu cầu tái sử dụng các khối mã nguồn chung, từ đó khai sinh ra **hàm con (Subroutine)**.
- Khi các chương trình bắt đầu có các hàm gọi lồng nhau hoặc tự gọi chính nó, kiến trúc máy tính thời đó đối mặt với **2 bài toán bế tắc lớn**.

---

### 2. Hai bài toán cốt lõi thúc đẩy Stack ra đời

#### Bài toán 1: Lời gọi hàm lồng nhau & Đệ quy (Call Stack & Recursion)
Khi một hàm con thực thi xong, CPU cần biết phải **nhảy về dòng lệnh nào tiếp theo** để hàm cha chạy tiếp — đây là **Địa chỉ quay về (Return Address)**.
> **Phân biệt quan trọng:**
> - **Return Address (Địa chỉ quay về):** Vị trí dòng lệnh CPU cần nhảy về tiếp theo.
> - **Return Value (Giá trị trả về):** Dữ liệu/kết quả tính toán mà hàm trả về.
> 
> *Cái gây crash bộ nhớ kinh điển trước khi có Stack chính là việc ghi đè **Return Address**.*

**Cách giải quyết thời kỳ đầu (Cấp phát tĩnh - Static Allocation):**
Trình biên dịch gán trước một ô nhớ cố định cho mỗi hàm (ví dụ: FORTRAN đời đầu).
- **Hệ quả 1: Đệ quy bị cấm hoàn toàn.** Nếu hàm `fact(3)` gọi `fact(2)`, `fact(2)` sẽ ghi đè tham số và Return Address của `fact(3)` vào đúng ô nhớ đó $\rightarrow$ khi `fact(2)` kết thúc, CPU mất dấu dòng lệnh của `fact(3)`, chương trình rơi vào vòng lặp vô tận hoặc crash.
- **Hệ quả 2: Phá vỡ tính tái nhập (Non-reentrant) khi có Ngắt (Interrupt):**
  - Giả sử `tinh_tong(a, b)` đang chạy dở với `a=10, b=20`.
  - Một ngắt phần cứng (Hardware Interrupt từ đồng hồ hoặc bàn phím) chen ngang, và ngắt này cũng vô tình gọi `tinh_tong(1, 1)`.
  - Tham số `a, b` ở ô nhớ tĩnh bị ghi đè thành `1, 1`. Khi CPU quay lại tiếp tục tác vụ ban đầu, kết quả bị sai hoàn toàn (`1 + 1 = 2` thay vì `10 + 20 = 30`).
- **Hệ quả 3: Lãng phí RAM nghiêm trọng.** Bộ nhớ phải được dành sẵn cho toàn bộ các hàm xuyên suốt vòng đời chương trình, bất kể hàm đó có được gọi hay không.

#### Bài toán 2: Đánh giá biểu thức số học phức tạp (Arithmetic Expression Evaluation)
Máy tính chỉ có thể thực hiện một phép tính nhị phân tại một thời điểm ($A \text{ op } B$). Khi xử lý biểu thức lồng nhau:
$$(x + y) \cdot z + x \cdot y - (x + z)$$
- Máy tính phải ưu tiên tính trong ngoặc hoặc phép toán có độ ưu tiên cao hơn (`*`, `/` trước `+`, `-`).
- Trước khi có Stack, lập trình viên phải chia nhỏ biểu thức bằng tay và tự tay quản lý các thanh ghi / biến tạm trung gian.
- **Quy luật tự nhiên:** Phép toán hoặc dấu ngoặc mở xuất hiện sau cùng lại là thứ cần tính và thu dọn **đầu tiên** $\rightarrow$ Đây chính là bản chất **LIFO (Last-In, First-Out)**.
*(Năm 1957, Friedrich Bauer và Klaus Samelson phát minh ra nguyên lý Stack chính xác để phục vụ cho bộ phân tích cú pháp biểu thức).*

**Khi thu dọn:**
1. `fact(1)` tính xong $\rightarrow$ Hủy frame của `fact(1)`, CPU nhảy về địa chỉ ghi trong frame $\rightarrow$ khôi phục `fact(2)` với `n=2` nguyên vẹn.
2. `fact(2)` tính xong $\rightarrow$ Hủy frame của `fact(2)`, CPU nhảy về `fact(3)` với `n=3` nguyên vẹn.
3. Không ô nhớ nào bị ghi đè lẫn nhau, và bộ nhớ được giải phóng ngay lập tức!

=> Từ những lý do như vậy đã thúc đẩy `Stack` ra đời. 

## Nó là gì?
<!-- Định nghĩa rõ ràng bằng lời của bạn. -->

**Ngăn xếp (Stack)** là một cấu trúc dữ liệu tuyến tính hoạt động theo nguyên lý **LIFO (Last-In, First-Out)**: *phần tử nào đưa vào sau cùng sẽ được lấy ra đầu tiên*.

Về bản chất, Stack là một danh sách bị **hạn chế truy cập có chủ đích**: Bạn chỉ có thể thêm hoặc lấy dữ liệu tại **một đầu duy nhất gọi là Đỉnh (Top)**, đầu còn lại (Đáy - Bottom) bị chặn kín.

- **Mô hình tư duy (Mental model):** Giống hệt như một **chồng đĩa ăn** hoặc **hộp bóng tennis** — bạn chỉ có thể đặt đĩa mới lên trên cùng, và khi lấy đĩa ra dùng cũng bắt buộc phải nhấc từ cái trên cùng xuống.

## Nó hoạt động thế nào?
<!-- Giải thích cơ chế, nội tại, và mô hình tư duy. -->

### 1. Trái tim của Stack: Con trỏ Đỉnh (`top`)
Toàn bộ hoạt động của Stack chỉ xoay quanh **một biến duy nhất** gọi là `top` (trong kiến trúc máy tính gọi là `Stack Pointer - SP`):
- Khi Stack rỗng: `top = -1` (hoặc trỏ tới `null`).
- Mọi thao tác thêm/xóa/đọc đều quy về việc **dịch chuyển vị trí của `top`**.

---

### 2. Cơ chế các thao tác cốt lõi

#### Thao tác `push(x)` — Thêm vào đỉnh
1. *(Nếu dùng mảng cố định)*: Kiểm tra xem Stack đã đầy chưa (`isFull`). Nếu đầy $\rightarrow$ báo lỗi **Stack Overflow**.
2. Tăng con trỏ: `top = top + 1`.
3. Ghi giá trị `x` vào vị trí `top`.

#### Thao tác `pop()` — Lấy ra từ đỉnh
1. Kiểm tra xem Stack có đang rỗng không (`isEmpty`). Nếu rỗng $\rightarrow$ báo lỗi **Stack Underflow**.
2. Lấy giá trị tại vị trí `top` ra.
3. Giảm con trỏ: `top = top - 1`.
> **Bí mật nội tại:** Máy tính **không hề tốn công xóa dữ liệu cũ** trong bộ nhớ. Chỉ cần con trỏ `top` lùi xuống 1 bước, ô nhớ đó coi như "đã bị hủy" và sẽ bị ghi đè khi có lệnh `push` mới.

#### Thao tác `peek()` / `top()` — Xem trước đỉnh
- Chỉ đọc giá trị tại `top` mà **không thay đổi** giá trị của biến `top`.

---

### 3. Minh họa trực quan (Visual Walkthrough)

| Bước | Thao tác | Trạng thái (Đỉnh $\rightarrow$ Đáy) | Con trỏ `top` | Kết quả / Giải thích |
| :---: | :--- | :---: | :---: | :--- |
| **1** | Khởi tạo | `[ ]` | `-1` | Stack rỗng |
| **2** | `push(10)` | `[ 10 ]` | `0` | Đưa 10 vào đỉnh |
| **3** | `push(20)` | `[ 20, 10 ]` | `1` | 20 nằm trên 10 |
| **4** | `peek()` | `[ 20, 10 ]` | `1` | Trả về `20` (không xóa) |
| **5** | `pop()` | `[ 10 ]` | `0` | Lấy `20` ra khỏi đỉnh |
| **6** | `pop()` | `[ ]` | `-1` | Lấy `10` ra, stack rỗng trở lại |

---

### 4. Hai cách cài đặt bên dưới (Under the hood)

Mặc dù Stack có giao diện giống nhau, bên dưới thường được hiện thực hóa bằng 1 trong 2 cấu trúc:

| Tiêu chí | Cài đặt bằng Mảng (Array) | Cài đặt bằng Danh sách liên kết (Linked List) |
| :--- | :--- | :--- |
| **Cơ chế** | Dùng một mảng và biến chỉ số `top` | Dùng các Node, phần tử đầu (`Head`) đóng vai trò là `Top` |
| **Ưu điểm** | - Dữ liệu nằm liên tục trong RAM $\rightarrow$ Tận dụng CPU Cache cực tốt (chạy rất nhanh).<br>- Không tốn thêm RAM lưu con trỏ. | - Kích thước co giãn linh hoạt, không lo bị tràn dung lượng cố định (*Stack Overflow*). |
| **Nhược điểm** | - Giới hạn kích thước (với mảng tĩnh).<br>- Tốn chi phí cấp phát lại (*resize*) nếu dùng mảng động. | - Tốn thêm bộ nhớ cho từng con trỏ `next`.<br>- Các Node nằm rải rác trong RAM $\rightarrow$ Cache miss cao hơn. |

---

### 5. Hiệu năng tính toán (Complexity)
Do chỉ thao tác trên đúng một biến `top`:
- **Thời gian (Time Complexity):** Tất cả `push`, `pop`, `peek`, `isEmpty` đều là **$O(1)$** (hằng số thời gian, diễn ra tức thì).
- **Bộ nhớ (Space Complexity):** **$O(N)$** cho $N$ phần tử được lưu trữ.

## Ví dụ
<!-- Code block hoặc ví dụ thực tế. -->

### 1. Interface chung (Đặc tả ADT)
Trước khi cài đặt, ta định nghĩa Interface để thể hiện đúng bản chất Stack là một Kiểu dữ liệu trừu tượng (ADT):

```java
public interface MyStack<T> {
    void push(T value);
    T pop();
    T peek();
    boolean isEmpty();
    int size();
}
```

---

### 2. Cách 1: Cài đặt bằng Mảng tĩnh (Fixed-capacity Array Stack)
> **Đặc điểm:** Sử dụng một mảng (Array) để lưu trữ phần tử. Biến `topIndex` đóng vai trò là chỉ số của phần tử nằm trên cùng. Kích thước của Stack bị giới hạn bởi kích thước của mảng.
```java
import java.util.EmptyStackException;

public class ArrayStack<T> implements MyStack<T> {
    private Object[] data;
    private int topIndex = -1; // -1 nghĩa là stack đang rỗng
    private static final int DEFAULT_CAPACITY = 10;

    public ArrayStack(int capacity) {
        this.data = new Object[capacity];
    }

    public ArrayStack() {
        this(DEFAULT_CAPACITY);
    }

    @Override
    public void push(T value) {
        if (isFull()) {
            throw new IllegalStateException("Stack Overflow: Ngăn xếp đã đầy!");
        }
        data[++topIndex] = value;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T pop() {
        if (isEmpty()) throw new EmptyStackException();
        T value = (T) data[topIndex];
        data[topIndex--] = null; // Tránh memory leak trong Java (hỗ trợ Garbage Collection)
        return value;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T peek() {
        if (isEmpty()) throw new EmptyStackException();
        return (T) data[topIndex];
    }

    @Override
    public boolean isEmpty() {
        return topIndex == -1;
    }

    public boolean isFull() {
        return topIndex == data.length - 1;
    }

    @Override
    public int size() {
        return topIndex + 1;
    }
}
```

> **Lưu ý & Đào sâu:**
> - **Tại sao `pop()` lại có dòng `data[topIndex--] = null;`?**
>   - *Về bản chất Stack / phần cứng:* Máy tính **chỉ dịch chuyển con trỏ** `topIndex--`, dữ liệu cũ ở ô nhớ không cần tốn công xóa vì sẽ tự bị ghi đè khi `push` mới (nếu dùng kiểu nguyên thủy như `int[]` thì chỉ cần `return data[topIndex--];`).
>   - *Đặc thù của Generic trong Java:* Do mảng `Object[]` lưu **tham chiếu (Reference)** trỏ đến đối tượng trên Heap. Nếu chỉ lùi `topIndex`, mảng bên dưới vẫn âm thầm giữ liên kết đến object đó khiến Garbage Collector (GC) không thể dọn dẹp $\rightarrow$ gây ra lỗi rò rỉ bộ nhớ kinh điển gọi là **Loitering (Obsolete Reference)** (*Effective Java - Item 7*). Gán `null` là để cắt đứt liên kết cho GC giải phóng bộ nhớ.
> - **Ưu điểm mảng tĩnh (Fixed capacity):** Thể hiện trực quan điều kiện `isFull()` và trạng thái lỗi **Stack Overflow**. Mọi thao tác đều đạt **$O(1)$ tuyệt đối** (Worst-case).
> - **Mở rộng trong thực tế:** Nếu muốn Stack tự động co giãn kích thước khi đầy, ta có thể tích hợp cơ chế nhân đôi dung lượng (*resize*) - Mảng động

---

### 3. Cách 2: Cài đặt bằng Danh sách liên kết (Linked List-based Stack)
> **Đặc điểm:** Mỗi phần tử là một `Node`. Thao tác `push/pop` thực chất là thêm/xóa phần tử ở ngay đầu danh sách (`head`). Kích thước co giãn tự nhiên, không bao giờ lo tràn dung lượng mảng cố định.

```java
import java.util.EmptyStackException;

public class LinkedListStack<T> implements MyStack<T> {
    private static class Node<T> {
        T value;
        Node<T> next;

        Node(T value, Node<T> next) {
            this.value = value;
            this.next = next;
        }
    }

    private Node<T> top = null; // Đỉnh stack chính là head của Linked List
    private int size = 0;

    public LinkedListStack() {
        this.top = null;
        this.size = 0;
    }

    @Override
    public void push(T value) {
        // Tạo node mới, trỏ next về đỉnh cũ, rồi cập nhật đỉnh mới
        top = new Node<>(value, top);
        size++;
    }

    @Override
    public T pop() {
        if (isEmpty()) throw new EmptyStackException();
        T value = top.value;
        top = top.next; // Lùi đỉnh xuống node liền kề
        size--;
        return value;
    }

    @Override
    public T peek() {
        if (isEmpty()) throw new EmptyStackException();
        return top.value;
    }

    @Override
    public boolean isEmpty() {
        return top == null;
    }

    @Override
    public int size() {
        return size;
    }
}
```

---

### 4. Minh họa chạy thử (Demo)

```java
public class Main {
    public static void main(String[] args) {
        MyStack<Integer> stack = new ArrayStack<>(); // Hoặc: new LinkedListStack<>()
        
        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("Top: " + stack.peek()); // 30
        System.out.println("Pop: " + stack.pop());  // 30
        System.out.println("Pop: " + stack.pop());  // 20
        System.out.println("Size: " + stack.size()); // 1
    }
}
```

## Tóm tắt

- **Bản chất LIFO:** Stack hoạt động theo nguyên lý *Last-In, First-Out* — phần tử vào sau cùng sẽ ra đầu tiên; mọi thao tác chỉ diễn ra tại một đầu duy nhất là **Đỉnh (Top)**.
- **Lý do ra đời:** Xuất phát từ nhu cầu giải quyết 2 bài toán lớn trong lịch sử máy tính:
  1. *Quản lý lời gọi hàm & đệ quy:* Lưu ngữ cảnh và Return Address động qua từng **Stack Frame**, khắc phục lỗi ghi đè và thiếu tính tái nhập (*Non-reentrant*) của cấp phát tĩnh.
  2. *Đánh giá biểu thức số học phức tạp:* Tự động hóa việc lưu kết quả trung gian theo độ ưu tiên của toán tử và dấu ngoặc.
- **Hiệu năng vượt trội:** Mọi thao tác cốt lõi (`push`, `pop`, `peek`, `isEmpty`) đều đạt độ phức tạp thời gian **$O(1)$**.
- **Cách cài đặt:**
  - *Bằng Mảng:* Truy cập cực nhanh nhờ tận dụng CPU Cache; kích thước cố định nên có thể tràn (*Stack Overflow*) nếu vượt quá giới hạn.
  - *Bằng Danh sách liên kết:* Co giãn kích thước linh hoạt, không lo tràn bộ nhớ mảng nhưng tốn thêm RAM cho con trỏ liên kết.
- **Hai trạng thái lỗi kinh điển:**
  - *Stack Overflow:* Đẩy vào khi stack đã đầy (hoặc đệ quy vô hạn làm tràn Call Stack).
  - *Stack Underflow:* Lấy ra từ một stack đang rỗng.
- **Ứng dụng thực tế phổ biến:** Call Stack hệ thống, tính năng Undo/Redo ($Ctrl + Z$), nút Back/Forward của trình duyệt, kiểm tra tính hợp lệ của dấu ngoặc, thuật toán duyệt theo chiều sâu (DFS).

---

## Tài liệu tham khảo