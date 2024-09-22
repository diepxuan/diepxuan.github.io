---
layout: post
title: "[MikroTik Script] Update Peer Ip has DDNS"
categories: [MikroTik Script]
---

# [MikroTik Script] _Update Peer Ip has DDNS_

```
foreach v in=[/interface/wireguard/peers find] do={
  :local peerName [/interface/wireguard/peers get $v value-name=name]
  :local peerHost [/interface/wireguard/peers get $v value-name=endpoint-address]
  :local peerAddr [/interface/wireguard/peers get $v value-name=current-endpoint-address]
  :local peerNewAddr [:resolve $peerHost]
  :if ($peerAddr != $peerNewAddr) do={
    :log info "DDNS: Peer [$peerName] $peerHost - $peerAddr => $peerNewAddr"
    /interface/wireguard/peers set $v endpoint-address="$peerHost"
    # /interface/wireguard/peers set $v current-endpoint-address="$peerNewAddr"
  }
}
```
