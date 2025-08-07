# PowerShell script to set up WSL for Android APK building
# Run this as Administrator

Write-Host "=========================================" -ForegroundColor Green
Write-Host "Card Game Generator - WSL Setup" -ForegroundColor Green  
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""

# Check if running as administrator
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERROR: This script must be run as Administrator!" -ForegroundColor Red
    Write-Host "Right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Step 1: Installing WSL..." -ForegroundColor Yellow
try {
    wsl --install
    Write-Host "✓ WSL installation initiated" -ForegroundColor Green
} catch {
    Write-Host "✗ WSL installation failed: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "Step 2: Installing Ubuntu..." -ForegroundColor Yellow
try {
    wsl --install -d Ubuntu
    Write-Host "✓ Ubuntu installation initiated" -ForegroundColor Green
} catch {
    Write-Host "✗ Ubuntu installation failed: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Green
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""
Write-Host "IMPORTANT: You must restart your computer now!" -ForegroundColor Red
Write-Host ""
Write-Host "After restart, follow these steps:" -ForegroundColor Yellow
Write-Host "1. Open Command Prompt or PowerShell"
Write-Host "2. Type: wsl"
Write-Host "3. Navigate to: cd /mnt/c/Users/Admin/card_game/android_app/"
Write-Host "4. Follow the build steps in BUILD_APK_GUIDE.md"
Write-Host ""

$restart = Read-Host "Do you want to restart now? (y/n)"
if ($restart -eq "y" -or $restart -eq "Y") {
    Write-Host "Restarting computer in 10 seconds..." -ForegroundColor Yellow
    Start-Sleep -Seconds 10
    Restart-Computer -Force
} else {
    Write-Host "Please restart manually when ready." -ForegroundColor Yellow
}
