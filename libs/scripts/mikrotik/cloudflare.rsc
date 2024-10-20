# Version: 0.1
/ip address print
/interface print

######### update scripts version ##########
:local url "https://docs.diepxuan.com/libs/scripts/mikrotik/cloudflare.rsc"
:local localVersion "0.1"
:local remoteVersion ""
:local newScript "cloudflare.rsc"

/tool fetch url=$url mode=http dst-path=$newScript
:delay 5
:if ([file find name=$newScript] != "") do={
    :local content [/file get $newScript contents]
    :set remoteVersion [:pick $content 10 13]
    :if ($remoteVersion > $localVersion) do={
        :put "New version found: $remoteVersion. Updating script."
        /import file-name=$newScript
        :set localVersion $remoteVersion
        :put "Script updated to version $remoteVersion."
    } else={
        :put "No update required. Current version: $localVersion"
    }
} else={
    :put "Failed to download the update script."
}

######### detect public IP ##########
:local publicIP ""

:local pppIP [/ip address get [find interface="ISP1"] address]
:local extractedIP [:pick $pppIP 0 [:find $pppIP "/"]]
:if ([:len $extractedIP] > 0 && [:pick $extractedIP 0 3] != "10." && [:pick $extractedIP 0 4] != "192." && [:pick $extractedIP 0 8] != "172.16.") do={
    :set $publicIP $extractedIP
} else={
    :set pppIP [/ip address get [find interface="ISP2"] address]
    :set extractedIP [:pick $pppIP 0 [:find $pppIP "/"]]
    :if ([:len $extractedIP] > 0 && [:pick $extractedIP 0 3] != "10." && [:pick $extractedIP 0 4] != "192." && [:pick $extractedIP 0 8] != "172.16.") do={
        :set $publicIP $extractedIP
    } else={
        # If no public IP from PPPoE, use external service to get public IP
        /tool fetch url="http://ifconfig.me/ip" mode=http output=user as-value
        :local externalIP [:pick [find name="fetch-output"] value 0]
        :set $publicIP $externalIP
    }
}
:log info "Public IP detected: $publicIP"

########## Cloudflare API v4 DDNS ##########
:global currentIp
:local newIp [:resolve myip.opendns.com server=208.67.222.222]

:if ($newIp != $currentIp) do={
  :local cfToken "******"
  :local cfZoneId "******"
  :local cfDnsId "******"
  :local dnsType "A"
  :local dnsName "***.dc.diepxuan.io.vn"
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
