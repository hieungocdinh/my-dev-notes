# Danh sách liên kết (Linked List)

## Tại sao nó ra đời?
<!-- Vấn đề gì tồn tại TRƯỚC khi có nó? Nỗi đau nào nó giải quyết? -->
Danh sách liên kết (Linked List) ra đời chủ yếu để khắc phục 3 nhược điểm lớn của **Mảng (Array)**:

1. **Kích thước cố định (Fixed size):** Khi tạo array phải xác định trước số lượng phần tử. Nếu cần lưu trữ vượt quá giới hạn này, ta phải tạo một mảng mới lớn hơn và copy dữ liệu sang rất phiền và tốn chi phí. Thêm nữa, nếu không dùng hết só lượng ô nhớ đã định nghĩa từ đầu thì các ô nhớ này cũng k thể  tái sử dụng vào việc khác => gây lãng phí tài nguyên.
2. **Yêu cầu vùng nhớ liên tục:** Các phần tử trong array phải nằm sát địa chỉ ô nhớ của nhau. Hệ điều hành sẽ rất vất vả để tìm được một dãy dài các ô nhớ trống liên tiếp nhau nếu mảng có kích thước quá lớn.
3. **Thêm/xóa dữ liệu chậm (O(n)):** Nếu muốn chèn hoặc xóa một phần tử vào **đầu** hoặc **giữa** mảng, ta bắt buộc phải "dịch chuyển" toàn bộ các phần tử đằng sau nó.

**=> Giải pháp của Linked List:** 
Không cần khai báo trước kích thước (khắc phục 1), các ô nhớ có thể nằm rải rác khắp nơi (khắc phục 2) và việc chèn/xóa phần tử (ở đầu) diễn ra chớp nhoáng với thời gian O(1) (khắc phục 3).

## Nó là gì?
<!-- Định nghĩa rõ ràng bằng lời của bạn. -->
**Danh sách liên kết (Linked List)** là một cấu trúc dữ liệu dạng chuỗi (tuyến tính). Tuy nhiên, thay vì xếp thành một hàng liền nhau trong bộ nhớ như mảng, nó bao gồm các thành phần rời rạc được gọi là các **Node (Mắt xích / Nút)**.

Mỗi **Node** luôn lưu trữ 2 thành phần:
1. **Dữ liệu (Data):** Giá trị mà bạn muốn lưu trữ (ví dụ: số `5`, chữ `A`,...).
2. **Con trỏ (Pointer/Next):** Một mũi tên (hoặc địa chỉ) trỏ đến **Node** tiếp theo trong danh sách.

*Lưu ý: Node cuối cùng trong danh sách sẽ trỏ vào `Null` (hoặc `None`), báo hiệu điểm kết thúc của danh sách.*

## Nó hoạt động thế nào?
<!-- Giải thích cơ chế, nội tại, và mô hình tư duy. -->
Để quản lý một Linked List, ta luôn cần một biến **`Head`** để lưu giữ địa chỉ của Node đầu tiên. Nếu mất `Head`, ta sẽ mất toàn bộ danh sách vì không thể tìm lại các ô nhớ rời rạc.

Các thao tác cơ bản hoạt động như sau:

1. **Duyệt (Đọc/Tìm kiếm): $O(n)$**
   - Bắt đầu từ `Head`, ta nhảy qua từng Node dựa vào con trỏ `Next` cho đến khi gặp `Null`. 
   - *Nhược điểm:* Không có số Index như Array. Để tìm phần tử thứ 100, bắt buộc phải duyệt tuần tự qua 99 phần tử trước đó (không có Random Access).

2. **Thêm/Xóa ở ĐẦU (Head): $O(1)$**
   - Chỉ cần tạo Node mới, cho Node mới trỏ vào `Head` cũ, và cập nhật biến `Head` thành Node mới. Rất chớp nhoáng vì không phần tử nào bị dịch chuyển.

3. **Thêm/Xóa ở CUỐI (Tail): $O(n)$ hoặc $O(1)$**
   - Mặc định: Phải duyệt từ `Head` đến Node cuối cùng mất $O(n)$, sau đó trỏ Node cuối vào Node mới.
   - Nếu tối ưu (thường dùng): Ta dùng thêm một biến `Tail` lưu sẵn địa chỉ Node cuối, lúc này thao tác thêm vào cuối sẽ chỉ mất $O(1)$.

4. **Thêm/Xóa ở GIỮA: $O(n)$ đi tìm + $O(1)$ ngắt nối**
   - Thao tác ngắt/nối các con trỏ với nhau chỉ tốn $O(1)$ (vượt trội hơn Array vì Array bắt buộc phải dịch chuyển dữ liệu mất $O(n)$).
   - Tuy nhiên, để **đi tới** được vị trí giữa đó, ta vẫn phải duyệt từ đầu mất $O(n)$.

**=> Mô hình tư duy (Sự đánh đổi - Trade-off):** 
Linked list chấp nhận hy sinh **Tốc độ đọc ngẫu nhiên (chậm hơn Array)** và **Tốn thêm một chút RAM cho con trỏ** để đổi lấy **Khả năng co giãn vô hạn** và **Tốc độ chèn/xóa cực nhanh ($O(1)$)** khi đã ở đúng vị trí.

## Ví dụ
<!-- Code block hoặc ví dụ thực tế. -->
Dưới đây là đoạn code bằng **Java** tái hiện lại một Linked List đơn giản, bao gồm cấu trúc Node và thao tác thêm phần tử vào cuối danh sách để bạn dễ hình dung:

```java
// 1. Định nghĩa cấu trúc của một Mắt xích (Node)
class Node {
    int data;     // Dữ liệu lưu trữ
    Node next;    // Con trỏ tới phần tử tiếp theo

    public Node(int data) {
        this.data = data;
        this.next = null; // Mặc định khi tạo ra, nó chưa trỏ đi đâu cả
    }
}

// 2. Định nghĩa Cấu trúc Quản lý Danh sách (LinkedList)
class LinkedList {
    Node head; // Biến quan trọng nhất: lưu địa chỉ Node đầu tiên

    // Hàm Thêm một phần tử vào CUỐI danh sách
    public void append(int data) {
        Node newNode = new Node(data);

        // Trường hợp danh sách trống: Node mới chính là Head
        if (head == null) {
            head = newNode;
            return;
        }

        // Trường hợp đã có phần tử: Duyệt từ Head để tìm Node cuối cùng
        Node current = head;
        while (current.next != null) {
            current = current.next; // Nhảy sang Node tiếp theo
        }
        
        // Cập nhật mũi tên của Node cuối cùng trỏ vào Node mới
        current.next = newNode;
    }

    // Hàm Duyệt để in danh sách
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}

// 3. Chạy thử chương trình
public class Main {
    public static void main(String[] args) {
        LinkedList myList = new LinkedList();
        
        myList.append(10);
        myList.append(20);
        myList.append(30);
        
        myList.printList(); 
        // Kết quả in ra: 10 -> 20 -> 30 -> null
    }
}
```

## Tóm tắt
- **Mục đích sinh ra:** Khắc phục nhược điểm "kích thước cố định" và "chèn/xóa chậm chạp" của Mảng (Array).
- **Cấu tạo cốt lõi:** Gồm các `Node` nằm rải rác trong bộ nhớ. Mỗi `Node` chứa **Dữ liệu** và **Con trỏ** trỏ đến Node tiếp theo. Luôn cần có biến `Head` để giữ điểm bắt đầu.
- **Khi nào nên dùng (Trade-off):** Cực kỳ phù hợp cho bài toán cần **thêm/xóa phần tử liên tục**. KHÔNG NÊN dùng cho bài toán cần **đọc/truy cập dữ liệu ngẫu nhiên theo vị trí** (vì không có index).

## ⚠️ LƯU Ý QUAN TRỌNG (Sự thật về độ phức tạp O(1))
Nhiều người lầm tưởng chèn/xóa ở Linked List luôn nhanh hơn Mảng. Nhưng sự thật là: **Đi tìm vị trí mất $O(n)$ + Ngắt nối con trỏ mất $O(1)$ = Tổng thời gian thực tế vẫn là $O(n)$!**

Đối với thao tác tìm một vị trí ngẫu nhiên ở giữa để chèn/xóa, Linked List không hề nhanh hơn Array. Thậm chí trong thực tế còn **chậm hơn** vì Array được CPU tối ưu duyệt rất nhanh (nhờ các ô nhớ nằm liền kề).

**Vậy Linked List thực sự "chiếm ưu thế" so với Array trong trường hợp nào?**
1. **Chỉ làm việc ở 2 đầu (Head/Tail):** Điển hình là Hàng đợi (Queue) hay Ngăn xếp (Stack). Cứ thêm vào cuối và rút ra ở đầu, thao tác chuẩn xác là $O(1)$ tuyệt đối vì có sẵn con trỏ, không phải tìm kiếm.
2. **Duyệt và Xóa/Chèn LIÊN TỤC:** Giả sử bạn duyệt mảng 1 triệu phần tử và cần xóa 1000 phần tử thõa mãn điều kiện.
   - Mảng (Array): Mỗi lần xóa 1 phần tử, bạn phải "kéo" hàng trăm ngàn phần tử phía sau lên lấp chỗ trống. Lặp lại 1000 lần sẽ khiến hệ thống treo ($O(n^2)$).
   - Linked List: Vừa đi bộ vừa tiện tay ngắt dây vứt phần tử ra ngoài ($O(1)$). Không ai phía sau bị ảnh hưởng. Kết quả chỉ tốn đúng 1 vòng duyệt ($O(n)$) để xong việc.

## Tài liệu tham khảo
<!-- - [Tiêu đề](URL) -->
- [Linked List Data Structure](https://www.geeksforgeeks.org/dsa/linked-list-data-structure/)
