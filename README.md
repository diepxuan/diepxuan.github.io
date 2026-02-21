# Networking


| Interface | Cluster              | thd                  | kct1            |
| --------- | -------------------- | -------------------- | --------------- |
| VPN       | 10.20.1.0/24         | 10.20.1.1            | 10.20.1.2       |
| ROUTER    |                      | thd1 192.168.1.0/24  | 192.168.12.0/24 |
|           |                      | thd2 192.168.1.0/24  |                 |
| LAN       | 10.10.0.0/24         | 10.10.1.0/24         | 10.10.1.0/24    |
| Tailscale |                      | 100.67.131.1         |                 |


# Diagrams

```mermaid
flowchart TD

subgraph KCT1[Khu lang nghe]
end
subgraph VP[Van Phong]
    subgraph Master
    direction LR
    thd1router-."DHCP".->
    thd1router2
    thd1router2-."DHCP".->thd1client
    thd1router2-."DHCP".->thd1camera
    end
    subgraph Slave
    direction LR
    thd2router-."192.168.1.0/24".->
    thd2lan((clients))
    end
    subgraph Server
    direction LR
        subgraph SDN[Vitual NetWork]
        vnet
        end
        subgraph pve1[Proxmox 10.10.0.1/24]
        direction TB
        100 ~~~
        103 ~~~
        105 ~~~
        107 ~~~
        109 ~~~
        110
        end
        subgraph pve2[Proxmox 10.10.0.2/24]
        direction TB
        101 ~~~
        102 ~~~
        104 ~~~
        106 ~~~
        111
        end
    mikrotik
    pve1-.112.->mikrotik
    pve2-.112.->mikrotik
    %% pve1==>SDN
    %% pve2==>SDN
    vnet-."10.0.0.50".->mikrotik
    vnet-."10.0.0.52".->103
    vnet-."10.0.0.53".->107
    vnet-."10.0.0.54".->110
    vnet-."10.0.0.55".->111
    vnet-."10.0.0.56".->106
    vnet-."10.0.0.57".->104
    vnet-."10.0.0.58".->101
    vnet-."10.0.0.59".->100
    vnet-."10.0.0.60".->102
    end
    thd1router-."192.168.1.10".->mikrotik
    thd2router-."192.168.1.10".->mikrotik
end
internet(((Internet)))
internet<-..->VP
internet<-..->KCT1

thd1router[(Router 192.168.1.0/24)]
thd1router2[(Router 192.168.11.0/24)]
thd1client((client 192.168.11.0/24))
thd1camera((camera 192.168.11.0/24))
thd2router[(Router 192.168.1.0/24)]

vnet[(vnet 10.0.0.0/24)]

100[(100 DC1)]
101[(101 immich)]
102[(102 SQL1)]
103[(103 technitiumdns)]
104[(104 magento)]
105[(105 Xpemology)]
106[(106 portal)]
107[(107 adguard)]
109[(109 go2rtc)]
110[(110 opensearch)]
111[(111 DC)]
mikrotik[(MikroTik 10.10.1.0/24)]

style VP fill:none
style Master fill:none
style Slave fill:none
style Server fill:none
style SDN fill:none
```

---

# 📄 Company Documents

This website now includes a **Documents** section containing important company files:

## Available Documents

### User Manuals
- **Internet Services Manual** (`/documents/WEBHD_INTERNET_UM_v1.0.docx`) - Complete guide for Internet services

### Inventory & Reports
- **Inventory Report** (`/documents/TonKho/20251130.xlsx`) - Stock tracking spreadsheet (Nov 2025)

## Access Documents

- **Web Interface**: Visit https://docs.diepxuan.com/documents/
- **Direct Links**: Click on document names above to download
- **Git Repository**: All documents are version-controlled in the `documents/` directory
- **Domain**: docs.diepxuan.com (primary website domain)

## Document Management

- **Location**: All documents are stored in `/documents/` directory
- **Version Control**: Git-tracked for change history
- **Future Plans**: Convert to Markdown for better web viewing

---

*Website last updated: 2026-02-21*
