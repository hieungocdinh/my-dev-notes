#!/usr/bin/env python3
"""
new-note.py — Tạo ghi chú từ template và cập nhật tất cả README index.

Cách dùng:
    python scripts/new-note.py <đường-dẫn> <tên-file> [tiêu-đề]

Tham số:
    đường-dẫn   Đường dẫn folder tương đối trong repo (dùng forward slash).
                Ví dụ: fundamentals/data-structures   topics/react
    tên-file    Tên file KHÔNG có đuôi .md. Phải là chữ-thường-gạch-ngang.
                Ví dụ: linked-list   event-loop   binary-search
    tiêu-đề     (Tùy chọn) Tiêu đề hiển thị cho ghi chú.
                Mặc định là Title Case của tên file.
                Ví dụ: "Danh sách liên kết"

Ví dụ:
    python scripts/new-note.py fundamentals/data-structures linked-list "Danh sách liên kết"
    python scripts/new-note.py topics/react use-effect "useEffect"
    python scripts/new-note.py fundamentals/algorithms binary-search
"""

import sys
import os
import re
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_FILE = Path(__file__).parent / "templates" / "note.md"
README_TEMPLATE_FILE = Path(__file__).parent / "templates" / "leaf_readme.md"

# Anchor comment đánh dấu vị trí chèn hàng vào bảng trong mỗi README.
# Các anchor này được nhúng sẵn trong file README để script luôn tìm đúng chỗ.
ANCHOR_LEAF   = "<!-- new-note: insert leaf row above -->"
ANCHOR_CAT    = "<!-- new-note: insert category row above -->"
ANCHOR_ROOT_T = "<!-- new-note: insert topics row above -->"
ANCHOR_ROOT_F = "<!-- new-note: insert fundamentals row above -->"


# ── Helpers ───────────────────────────────────────────────────────────────────

def to_title(s: str) -> str:
    """linked-list → Linked List"""
    return " ".join(w.capitalize() for w in s.replace("-", " ").split())


def read(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def write(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def link_exists(lines: list[str], fragment: str) -> bool:
    """Trả về True nếu `fragment` đã xuất hiện ở đâu đó trong file."""
    return any(fragment in line for line in lines)


def insert_before_anchor(lines: list[str], anchor: str, new_row: str) -> bool:
    """Chèn `new_row` vào dòng ngay trước anchor comment."""
    for i, line in enumerate(lines):
        if anchor in line:
            lines.insert(i, new_row)
            return True
    return False


# ── Template ──────────────────────────────────────────────────────────────────

def load_template(title: str) -> str:
    """Đọc scripts/templates/note.md và thay {{title}} bằng tiêu đề thực."""
    if not TEMPLATE_FILE.exists():
        print(f"[ERROR] Không tìm thấy file template: {TEMPLATE_FILE}")
        sys.exit(1)
    raw = TEMPLATE_FILE.read_text(encoding="utf-8")
    return raw.replace("{{title}}", title)


# ── README updaters ───────────────────────────────────────────────────────────

def _append_to_readme(readme: Path, anchor: str, row: str, unique_link: str) -> None:
    """Hàm dùng chung để đọc file, kiểm tra tồn tại link và chèn hàng vào bảng."""
    lines = read(readme)
    if link_exists(lines, unique_link):
        _skip(readme)
        return

    if insert_before_anchor(lines, anchor, row):
        write(readme, lines)
        _ok("Cập nhật", readme)
    else:
        print(f"[WARNING] Không tìm thấy anchor trong {_rel(readme)} — vui lòng thêm hàng thủ công")


def update_leaf_readme(folder: Path, note_name: str) -> None:
    """Thêm hàng cho ghi chú mới vào README của folder hiện tại."""
    readme = folder / "README.md"
    link   = f"./{note_name}.md"
    row    = f"| [{note_name}.md]({link}) | <!-- description --> |"

    if not readme.exists():
        _create_leaf_readme(folder, readme, row)
        return

    _append_to_readme(readme, ANCHOR_LEAF, row, f"{note_name}.md")


def _create_leaf_readme(folder: Path, readme: Path, first_row: str) -> None:
    folder_title = to_title(folder.name)
    
    if not README_TEMPLATE_FILE.exists():
        print(f"[ERROR] Không tìm thấy file template: {README_TEMPLATE_FILE}")
        sys.exit(1)
        
    raw = README_TEMPLATE_FILE.read_text(encoding="utf-8")
    content = raw.replace("{{folder_title}}", folder_title)\
                 .replace("{{first_row}}", first_row)\
                 .replace("{{ANCHOR_LEAF}}", ANCHOR_LEAF)
                 
    readme.write_text(content, encoding="utf-8")
    _ok("Đã tạo", readme)


def update_category_readme(section_readme: Path, category_folder: Path) -> None:
    """Đảm bảo folder danh mục được liệt kê trong README của section (ví dụ: fundamentals/README.md)."""
    cat_name = category_folder.name
    link     = f"./{cat_name}/README.md"
    row      = f"| [{cat_name}/]({link}) | <!-- description --> |"

    if not section_readme.exists():
        _skip(section_readme, "(không tìm thấy file)")
        return

    _append_to_readme(section_readme, ANCHOR_CAT, row, f"{cat_name}/")


def update_root_readme(section: str, category_folder: Path) -> None:
    """Đảm bảo danh mục xuất hiện trong bảng điều hướng của README gốc."""
    readme   = REPO_ROOT / "README.md"
    cat_name = category_folder.name
    cat_title = to_title(cat_name)
    link     = f"./{section}/{cat_name}/README.md"
    row      = f"| [{cat_title}]({link}) | <!-- description --> |"

    anchor = ANCHOR_ROOT_F if section == "fundamentals" else ANCHOR_ROOT_T

    if not readme.exists():
        _skip(readme, "(không tìm thấy README gốc)")
        return

    _append_to_readme(readme, anchor, row, f"{section}/{cat_name}/README.md")


# ── Pretty print ──────────────────────────────────────────────────────────────

def _rel(p: Path) -> str:
    return str(p.relative_to(REPO_ROOT))

def _ok(verb: str, p: Path) -> None:
    print(f"  [OK] {verb:<10} {_rel(p)}")

def _skip(p: Path, reason: str = "(đã tồn tại)") -> None:
    print(f"  [-]  Bỏ qua   {_rel(p)} {reason}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    rel_path  = sys.argv[1].replace("\\", "/")   # ví dụ: "fundamentals/data-structures"
    note_name = sys.argv[2]                       # ví dụ: "linked-list"
    title     = sys.argv[3] if len(sys.argv) > 3 else to_title(note_name)

    # Kiểm tra tên file
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", note_name):
        print(f"[ERROR] Tên file phải là chữ-thường-gạch-ngang. Nhận được: '{note_name}'")
        sys.exit(1)

    parts = rel_path.strip("/").split("/")   # ["fundamentals", "data-structures"]

    folder    = REPO_ROOT / Path(*parts)
    file_path = folder / f"{note_name}.md"

    if file_path.exists():
        print(f"[ERROR] File đã tồn tại: {_rel(file_path)}")
        sys.exit(1)

    # Tạo folder nếu chưa có
    folder.mkdir(parents=True, exist_ok=True)

    print(f"\n--> Đang tạo ghi chú: {_rel(file_path)}")
    print(f"    Tiêu đề: {title}\n")

    # 1. Tạo file ghi chú (copy từ template.md, thay tiêu đề)
    file_path.write_text(load_template(title), encoding="utf-8")
    _ok("Đã tạo", file_path)

    # 2. Cập nhật README của folder hiện tại (ví dụ: fundamentals/data-structures/README.md)
    update_leaf_readme(folder, note_name)

    # 3. Cập nhật README của section (ví dụ: fundamentals/README.md)
    if len(parts) >= 2:
        section_readme = REPO_ROOT / parts[0] / "README.md"
        update_category_readme(section_readme, folder)

    # 4. Cập nhật README gốc
    if len(parts) >= 2:
        update_root_readme(parts[0], folder)

    print(f"\n*** Xong! Mở file và bắt đầu viết:")
    print(f"    {file_path}\n")


if __name__ == "__main__":
    main()
