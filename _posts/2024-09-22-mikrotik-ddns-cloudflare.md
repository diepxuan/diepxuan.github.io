---
layout: post
title: "[MikroTik Script] Cloudflare API v4 DDNS"
categories: [MikroTik Script]
---

# [MikroTik Script] _Cloudflare API v4 DDNS_

```
:global currentIp
:local newIp [:resolve myip.opendns.com server=208.67.222.222]

:if ($newIp != $currentIp) do={
  :local cfToken "******"
  :local cfZoneId "******"
  :local cfDnsId "******"
  :local dnsType "A"
  :local dnsName "kct1.dc.diepxuan.io.vn"
  :local dnsTTL "1"
  :local dnsProxied "false"

  :local apiUrl "https://api.cloudflare.com/client/v4/zones/$cfZoneId/dns_records/$cfDnsId"

  :local headers "Authorization: Bearer $cfToken"
  :local payload "{\"type\":\"$dnsType\",\"name\":\"$dnsName\",\"content\":\"$newIp\",\"ttl\":$dnsTTL,\"proxied\":$dnsProxied}"

  :do {
    :local response [/tool fetch http-method="put" url=$apiUrl http-header-field=$headers http-data=$payload as-value output=user]

    :if ($response->"status" = "finished") do={
        :log info "DDNS: $dnsName changed $currentIp to $newIp"

        # update $currentIp with the new one
        :set currentIp $newIp
    }
  } on-error {
    :log error "DDNS: failed to change $dnsName IP $currentIp to $newIp"
  }
}
```
