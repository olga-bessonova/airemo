# Function to get device information using Get-CimInstance
function Get-DeviceDetails {
    try {
        $deviceDetails = Get-CimInstance -ClassName Win32_PnPEntity -ErrorAction Stop | ForEach-Object {
            $deviceDetails = [PSCustomObject]@{
                DeviceName     = $_.Caption
                Manufacturer   = $_.Manufacturer
                Model          = $_.DeviceID
                SerialNumber   = $_.SerialNumber
                Driver         = $_.DriverVersion
                Status         = $_.Status
                Conflicts      = $_.ConfigManagerErrorCode -ne 0
            }
            $deviceDetails
        }

        # Output device details
        $deviceDetails | Format-Table -AutoSize

        # Save device details to a CSV file
        $deviceDetails | Export-Csv -Path "DeviceDetails.csv" -NoTypeInformation
    }
    catch {
        # Log errors to a file
        $errorMessage = "Error: $_"
        $errorLogPath = "ErrorLog.txt"
        Add-Content -Path $errorLogPath -Value $errorMessage

        # Exit the script or handle the error accordingly
        # You may choose to stop execution, continue, or take specific actions based on the error
        exit
    }
}

# Run the script silently
Start-Process powershell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$($MyInvocation.MyCommand.Path)`"" -Verb RunAs -WindowStyle Hidden

##############################

# Connect to SharePoint Online
$siteUrl = "https://your-sharepoint-site-url"
Connect-PnPOnline -Url $siteUrl -UseWebLogin

# Define SharePoint document library and Excel file details
$documentLibraryName = "YourDocumentLibrary"
$excelFileName = "YourExcelFile.xlsx"
$excelFilePath = "/$documentLibraryName/$excelFileName"

# Check if the Excel file exists
if (Get-PnPFile -ServerRelativeUrl $excelFilePath -AsFile) {
    # Access existing Excel file
    $excelFile = Get-PnPFile -ServerRelativeUrl $excelFilePath -AsFile
}
else {
    # Create a new Excel Online file
    $excelFile = Add-PnPFile -Path "C:\Path\To\Your\Local\Excel\File.xlsx" -Folder $documentLibraryName -NewFileName $excelFileName -Checkout $false -Publish $true
}

# Import-Excel and Export-Excel to add data to different tabs
# Note: Import-Excel and Export-Excel might not directly work with Excel Online
# You may need to use SharePoint cmdlets to update the Excel file in SharePoint

# Example: Update "Device Details" tab
$deviceDetailsData = Get-Content "DeviceDetails.csv"
Set-PnPFile -Url $excelFile.ServerRelativeUrl -Stream $deviceDetailsData -CheckIn -CheckInComment "Updated Device Details"

# Example: Update "Laptop Device" tab
# ... (similar process as above)

# Example: Update "Logging" tab
# ... (similar process as above)

# Disconnect from SharePoint Online
Disconnect-PnPOnline
