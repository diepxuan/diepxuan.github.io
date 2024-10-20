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
}

:local pppIP [/ip address get [find interface="ISP2"] address]
:local extractedIP [:pick $pppIP 0 [:find $pppIP "/"]]
:if ([:len $extractedIP] > 0 && [:pick $extractedIP 0 3] != "10." && [:pick $extractedIP 0 4] != "192." && [:pick $extractedIP 0 8] != "172.16.") do={
    :set $publicIP $extractedIP
}

else={
    # If no public IP from PPPoE, use external service to get public IP
    /tool fetch url="http://ifconfig.me/ip" mode=http output=user as-value
    :local externalIP [:pick [find name="fetch-output"] value 0]
    :set $publicIP $externalIP
}

# Log the detected public IP (optional)
:log info "Public IP detected: $publicIP"
