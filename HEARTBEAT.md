# HEARTBEAT.md

Them task duoi day de Bot kiem tra dinh ky.

---

## Tasks

### Phap luat moi

- name: check-new-laws
  interval: 24h
  prompt: |
    Kiem tra thong tin phap luat moi cua Viet Nam.

    1. Tim kiem web: "quyet dinh mới ban hanh phap luat Viet Nam 2025 2026" va "nghi dinh moi 2025 2026"
    2. Neu co van ban phap luat moi, kiem tra xem da co trong van-ban/ chua.
    3. Neu chua co, ghi nhan vao MEMORY.md voi:
       - Ten van ban
       - Ngay ban hanh
       - Noi dung tom tat
       - Lien ket nguon
    4. Neu co van ban cu can cap nhat, ghi nhan vao MEMORY.md de bao cao Sếp.
    5. Neu khong co gi moi, reply HEARTBEAT_OK.

### Cap nhat VBPL

- name: update-vbpl
  interval: 168h
  prompt: |
    Kiem tra cap nhatVbpl.vn cho cac van ban quan trong.

    1. Tim kiem: site:vbpl.vn "2025" OR "2026" moi nhat
    2. Kiem tra cac chu de: an ninh, phong chong tham nhung, bao hiem, dat dai
    3. Neu co cap nhat, kiem tra trong van-ban/ xem co can update khong.
    4. Neu can cap nhat, ghi nhan vao MEMORY.md de bao cao Sếp.
    5. Neu khong co gi thay doi, reply HEARTBEAT_OK.

### Theo doi Luat moi

- name: track-legislation
  interval: 72h
  prompt: |
    Theo doi tinh hinh luat moi cua Viet Nam.

    1. Tim kiem:
       - "du an luat" OR "lup tan" Viet Nam 2026
       - "thong tu moi" OR "quyet dinh moi" thang 5 nam 2026
    2. Kiem tra cac linh vuc: kinh te, phap ly, xa hoi
    3. Neu co luat dang duoc thao luan hoac ban hanh:
       - Ghi nhan vao MEMORY.md
       - Danh gia tien do (dang thao, lay y kien, ban hanh)
    4. Neu khong co gi moi, reply HEARTBEAT_OK.

### Kiem tra Toi

- name: check-today
  interval: 24h
  prompt: |
    Kiem tra nhung gi can lam hom nay.

    1. Doc memory/YYYY-MM-DD.md (hom nay) de xem cong viec da len lich.
    2. Neu co cong viec, thuc hien hoac bao cao tien do.
    3. Neu khong co gi, reply HEARTBEAT_OK.

---

## Quy tac thuc hien

- Chi thuc hien nhung task tren khi het han interval.
- Neu gap van de, reply HEARTBEAT_OK va ghi log vao MEMORY.md.
- Khong tu y tao file hay push khi chua duoc phep.
- Chi ghi nhan vao MEMORY.md de bao cao Sếp.