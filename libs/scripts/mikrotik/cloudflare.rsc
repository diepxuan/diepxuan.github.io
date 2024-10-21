# Version: 0.4

######### detect public IP ##########
:local publicIP ""

:local pppIP [/ip address get [find interface="ISP1"] address]
:local extractedIP [:pick $pppIP 0 [:find $pppIP "/"]]
:if ([:len $extractedIP] > 0 && [:pick $extractedIP 0 3] != "10." && [:pick $extractedIP 0 4] != "192." && [:pick $extractedIP 0 8] != "172.16.") do={
    :set $publicIP $extractedIP
} else={
  :set pppIP [/ip address get [find interface="ISP2"] address]
  :set extractedIP [:pick $pppIP 0 [:find $pppIP "/"]]
  :if ($publicIP = "" && [:len $extractedIP] > 0 && [:pick $extractedIP 0 3] != "10." && [:pick $extractedIP 0 4] != "192." && [:pick $extractedIP 0 8] != "172.16.") do={
      :set $publicIP $extractedIP
  } else={
    :local externalIP [:resolve whoami.cloudflare server=1.1.1.1]
    :set $publicIP $externalIP
  }
}

:if ($publicIP = "") do={
  #/tool fetch url="http://ifconfig.me/ip" mode=http output=user as-value
  #:local externalIP [:pick [find name="fetch-output"] value 0]
  #:local externalIP [:resolve myip.opendns.com server=208.67.222.222]
  #:local externalIP [:resolve whoami.cloudflare server=1.1.1.1]
  :local response [/tool fetch url="http://ifconfig.me/ip" mode=http output=user as-value]
  :if ($response->"status" = "finished") do={
    :set $publicIP ($response->"data")
  }
}

:log info "[DDNS] Public IP detected: $publicIP"

########## Cloudflare API v4 DDNS ##########
:global currentIp
:local newIp $publicIP

:if ($newIp != $currentIp) do={
  :global cfToken
  :global cfZoneId
  :global cfDnsId
  :global dnsType
  :global dnsName
  :local dnsTTL "1"
  :local dnsProxied "false"

  :local apiUrl "https://api.cloudflare.com/client/v4/zones/$cfZoneId/dns_records/$cfDnsId"

  :local headers "Authorization: Bearer $cfToken"
  :local payload "{\"type\":\"$dnsType\",\"name\":\"$dnsName\",\"content\":\"$newIp\",\"ttl\":$dnsTTL,\"proxied\":$dnsProxied}"

  :do {
    :local response [/tool fetch http-method="put" url=$apiUrl http-header-field=$headers http-data=$payload as-value output=user]

    :if ($response->"status" = "finished") do={
        :log info "[DDNS] $dnsName changed $currentIp to $newIp"

        # update $currentIp with the new one
        :set currentIp $newIp
    }
  } on-error {
    :log error "[DDNS] failed to change $dnsName IP $currentIp to $newIp"
  }
}

########## update Wireguard peers enpoint IP ##########
foreach v in=[/interface/wireguard/peers find] do={
  :local peerName [/interface/wireguard/peers get $v value-name=name]
  :local peerHost [/interface/wireguard/peers get $v value-name=endpoint-address]
  :local peerAddr [/interface/wireguard/peers get $v value-name=current-endpoint-address]
  :if ($peerHost != "") do={
    :local peerNewAddr [:resolve $peerHost]
    :if ($peerAddr != $peerNewAddr) do={
      :log info "DDNS: Peer [$peerName] $peerHost - $peerAddr => $peerNewAddr"
      /interface/wireguard/peers set $v endpoint-address="$peerHost"
      # /interface/wireguard/peers set $v current-endpoint-address="$peerNewAddr"
    }
  }
}

######### update scripts version ##########
#:local url "https://docs.diepxuan.com/libs/scripts/mikrotik/cloudflare.rsc"
:local url "https://raw.githubusercontent.com/diepxuan/diepxuan.github.io/refs/heads/main/libs/scripts/mikrotik/cloudflare.rsc"
:local localVersion "0.4"
:local remoteVersion ""
:local newScript "cloudflare.rsc"

/tool fetch url=$url mode=https dst-path=$newScript
#:delay 5
:if ([file find name=$newScript] != "") do={
    :local content [/file get $newScript contents]
    :set remoteVersion [:pick $content 10 13]
    :if ($remoteVersion > $localVersion) do={
        :log info "[DDNS] New version found: $remoteVersion. Updating script."
        /import file-name=$newScript
        :set localVersion $remoteVersion
        :log info "[DDNS] Script updated to version $remoteVersion."
    } else={
        :log info "[DDNS] No update required. Current version: $localVersion"
    }
} else={
    :log error "[DDNS] Failed to download the update script."
}