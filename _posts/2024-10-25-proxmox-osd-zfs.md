---
layout: post
title: "Create Ceph OSD over ZFS"
categories: [Linux, Proxmox, OSD, ZFS]
---

How to Create Ceph OSD over ZFS
---

### **Tạo một khối ZFS mới (ví dụ: tank/osd0) để sử dụng làm OSD:**
   ```bash
   zfs create -V 2T rpool/osd0
   ```
   Option `-V 2T` cài đặt size cho khối ZFS nhằm fix lỗi `lsblk: /dev/zvol/rpool/osd0: not a block device`

   Xác minh Khối ZFS đã Tạo
   Để đảm bảo rằng khối ZFS đã được tạo thành công, bạn có thể kiểm tra bằng lệnh sau:
   ```bash
   zfs list
   ```

### **Đăng ký OSD với Ceph**
   ```bash
   ceph-volume lvm create --data /dev/zvol/rpool/osd0
   ```
   Tuỳ  phiên bản Proxmox thì sẽ có vị trí keyring khác nhau, đôi khi sẽ gặp lỗi `auth: unable to find a keyring on /etc/pve/priv/ceph.client.bootstrap-osd.keyring: (2) No such file or  directory`
   Để khắc phục lỗi này, bạn cần tạo keyring cho OSD bootstrap client.
   Kiểm tra và tạo thư mục
   ```bash
   mkdir -p /etc/pve/priv
   mkdir -p /var/lib/ceph/bootstrap-osd/
   ```
   Lấy thông tin keyring từ danh sánh
   ```
   $ ceph auth ls
   ...
   client.bootstrap-osd
           key: AQA...DRA==
           caps: [mon] allow profile bootstrap-osd
   ...
   ```
   Cấu hình và cài đặt keyring
   ```bash
   ceph-authtool /etc/pve/priv/ceph.client.bootstrap-osd.keyring --create-keyring --gen-key -n client.bootstrap-osd
   ceph-authtool /etc/pve/priv/ceph.client.bootstrap-osd.keyring -n client.bootstrap-osd --add-key AQA...DRA==
   ceph-authtool /etc/pve/priv/ceph.client.bootstrap-osd.keyring -n client.bootstrap-osd --cap mon "allow profile bootstrap-osd"
   ceph-authtool /var/lib/ceph/bootstrap-osd/ceph.keyring --create-keyring --gen-key -n client.bootstrap-osd
   ceph-authtool /var/lib/ceph/bootstrap-osd/ceph.keyring -n client.bootstrap-osd --add-key AQA...DRA==
   ceph-authtool /var/lib/ceph/bootstrap-osd/ceph.keyring -n client.bootstrap-osd --cap mon "allow profile bootstrap-osd"
   ```

   Lỗi "Cannot use /dev/zd256: device is rejected by filter config" xuất hiện khi Ceph không cho phép sử dụng một thiết bị do cấu hình filter. Đây là một vấn đề phổ biến khi bạn cố gắng tạo OSD từ một ZFS volume.
   Để giải quyết vấn đề này, bạn cần đảm bảo rằng cấu hình filter cho phép sử dụng các thiết bị ZFS (zvol). Dưới đây là các bước chi tiết để khắc phục lỗi này: 

### **Kiểm tra Cấu hình LVM**

1. **Mở file cấu hình LVM**:
   Thông thường, file cấu hình Ceph sẽ nằm trong `/etc/etc/lvm/lvm.conf`.
   ```bash
   nano /etc/lvm/lvm.conf
   ```

2. **Kiểm tra các cấu hình filter**:
   Tìm dòng có chứa `global_filter=["r|/dev/zd.*|","r|/dev/rbd.*|"]` hoặc tương tự:
   ```ini
   devices {
       # added by pve-manager to avoid scanning ZFS zvols and Ceph rbds
       # global_filter=["r|/dev/zd.*|","r|/dev/rbd.*|"]
       global_filter=["r|/dev/rbd.*|"]
   }
   ```

3. **Lưu và đóng file**:
   Nếu bạn đang sử dụng `nano`, nhấn `CTRL + O`, sau đó `Enter` để lưu và `CTRL + X` để thoát.

### **Tạo OSD từ ZFS Volume**

1. **Tạo OSD**:
   Sau khi đã thay đổi cấu hình, hãy thử tạo OSD một lần nữa:
   ```bash
   ceph-volume lvm create --data /dev/zvol/rpool/osd0
   ```

### **Kiểm tra OSD**

   Sau khi thực hiện lệnh trên, kiểm tra lại trạng thái OSD:
   ```bash
   ceph osd tree
   ```

### **Khởi động lại Dịch vụ Ceph (Nếu cần)**

   Nếu bạn vẫn gặp lỗi sau khi thay đổi cấu hình, có thể bạn cần khởi động lại dịch vụ Ceph:
   ```bash
   systemctl restart ceph.target
   ```
