# 🔁 Restart Anki Addon

Một addon đơn giản cho phép bạn **khởi động lại Anki nhanh chóng** thông qua menu hoặc tổ hợp phím tắt.

---

## ✅ Tính năng

- Thêm menu **"Restart Anki"** trong mục **Tools**.
- Cho phép khởi động lại Anki bằng **tổ hợp phím tắt** (mặc định: `Alt + Shift + F4`).
- Hỗ trợ **thay đổi phím tắt** dễ dàng qua file `config.json`.

---

## 🧩 Cài đặt

1. Tải file `restart_anki.zip` và giải nén.
2. Chép thư mục `restart_anki/` đã giải nén vào:
   ```
   C:\Users\<tên người dùng>\AppData\Roaming\Anki2\addons21\
   ```
3. Mở lại Anki để addon hoạt động.

---

## 🖱️ Cách sử dụng

- Vào menu **Tools → Restart Anki** để khởi động lại ứng dụng.
- Hoặc nhấn **phím tắt** để thực hiện thao tác nhanh.

---

## ⚙️ Thay đổi phím tắt

1. Mở file `config.json` trong thư mục addon.
2. Sửa dòng `"shortcut"` theo định dạng Qt, ví dụ:
   ```json
   {
     "shortcut": "Ctrl+Alt+R"
   }
   ```
3. Lưu lại file và **khởi động lại Anki** để áp dụng.

Một số ví dụ hợp lệ:
- `"Ctrl+R"`
- `"Alt+Shift+F4"`
- `"Ctrl+Alt+Shift+Q"`

---

## 🛠 Ghi chú kỹ thuật

- Addon dùng `mw.addAction()` để phím tắt hoạt động toàn cục.
- Mã nguồn tương thích tốt với Anki 2.1.55 trở lên (QT6).

---

## 👤 Tác giả

- Phát triển bởi Nguyễn Văn Phán
- Phiên bản: 1.0
- Cập nhật lần cuối: 2025-06-30
