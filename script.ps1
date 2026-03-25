# Scan de tous les dossiers du disque en incluant les dossiers masqués et système

# commande ==> powershell -ExecutionPolicy Bypass -File .\script.ps1



$dirs = Get-ChildItem C:\ -Directory -Force -ErrorAction SilentlyContinue
$i = 0
$results = @()

foreach ($dir in $dirs) {
    $i++
    Write-Host "Scanning $($dir.FullName) ($i / $($dirs.Count))"

    # Calcul taille totale dossier
    $size = (Get-ChildItem $dir.FullName -Recurse -File -Force -ErrorAction SilentlyContinue |
        Measure-Object Length -Sum).Sum

    $results += [PSCustomObject]@{
        Path = $dir.FullName
        SizeGB = [math]::Round($size / 1GB,2)
    }
}

# Trier par taille 
$results | Sort-Object SizeGB -Descending

# Exporter en csv
$results | Sort-Object SizeGB -Descending | Export-Csv "dossiers.csv" -NoTypeInformation

Write-Host "Scan terminé ! Fichier : dossiers.csv"




# -------------------Scan du contenu des 3 dossiers les plus volumineux trouvés


$results = Import-Csv "dossiers.csv"
# Prendre les 3 dossiers les plus volumineux
$top3 = $results | Sort-Object {[double]$_."SizeGB"} -Descending | Select-Object -First 3

$subResults = @()

foreach ($folder in $top3) {
    $rootPath = $folder.Path
    Write-Host "`nScanning top folder: $rootPath"

    $dirs = Get-ChildItem $rootPath -Directory -Force -ErrorAction SilentlyContinue
    $i = 0
    foreach ($dir in $dirs) {
        $i++
        Write-Host "  Subfolder $($dir.FullName) ($i / $($dirs.Count))"

        $size = (Get-ChildItem $dir.FullName -Recurse -File -Force -ErrorAction SilentlyContinue |
            Measure-Object Length -Sum).Sum

        $subResults += [PSCustomObject]@{
            RootFolder = $rootPath
            Path       = $dir.FullName
            SizeGB     = [math]::Round($size / 1GB,2)
        }
    }
}
$subResults | Sort-Object SizeGB -Descending | Export-Csv "sousdoss.csv" -NoTypeInformation

Write-Host "Scan des sous-dossiers terminé ! Fichier : sousdoss.csv"