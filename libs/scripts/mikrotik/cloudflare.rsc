# Version: 0.1
/ip address print
/interface print


:local url "https://docs.diepxuan.com/libs/scripts/mikrotik/cloudflare.rsc"
:local localVersion "1.0"  # Replace with the current script version
:local remoteVersion ""
:local newScript "update-script.rsc"

# Step 1: Download the script file from the URL
/tool fetch url=$url mode=http dst-path=$newScript

# Step 2: Read the remote version from the downloaded file
:delay 2  # Wait a bit to ensure the file is downloaded
:if ([file find name=$newScript] != "") do={
    :local content [/file get $newScript contents]
    
    # Extract the version number from the downloaded script
    :set remoteVersion [:pick $content 10 13]  # Adjust if version format changes
    
    # Step 3: Compare versions
    :if ($remoteVersion > $localVersion) do={
        :put "New version found: $remoteVersion. Updating script."

        # Import the new script and update the current one
        /import file-name=$newScript
        :set localVersion $remoteVersion
        :put "Script updated to version $remoteVersion."
    } else={
        :put "No update required. Current version: $localVersion"
    }
} else={
    :put "Failed to download the update script."
}
