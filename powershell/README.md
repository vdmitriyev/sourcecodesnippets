## About

List of commands for powershell

## Hints

* Adding a custom methods to $PROFILE of powershell by using
    ```
    notepad $PROFILE
    ```
    
## Hosts in SSH config

* List all hosts in the `.ssh/config` file
    ```
    Select-String -Path "$env:USERPROFILE\.ssh\config" -Pattern "^Host\s+" | ForEach-Object { $_.Line.Split()[1] }
    ```
* Or an alias to `$PROFILE`
    ```
    function Get-SSHHosts {
        $configFile = "$env:USERPROFILE\.ssh\config"
        if (Test-Path $configFile) {
          Select-String -Path "$env:USERPROFILE\.ssh\config" -Pattern "^Host\s+" | ForEach-Object { $_.Line.Split()[1] }
       }
    }

    Set-Alias -Name sshlist -Value Get-SSHHosts
    ```
* Use it
    ```
    sshlist | grep jump
    ```

## Search in all history

* Search history commands
```
function search-history-all {
    param(
        [Parameter(ValueFromRemainingArguments = $true)]
        [string[]]$Patterns
    )

    $results = Get-Content (Get-PSReadLineOption).HistorySavePath | Select-Object -Unique

    foreach ($pattern in $Patterns) {
        $results = $results | Where-Object { $_ -match $pattern }
    }

    if ($Patterns.Count -gt 0) {
        $e = [char]27
        $combinedPattern = ($Patterns | ForEach-Object { "($_)" }) -join '|'
        $results = $results | ForEach-Object {
            $_ -replace $combinedPattern, "$e[1;32m`$0$e[0m"
        }
    }

    $results
}

# Optional: creates aliases
Set-Alias -Name histall -Value search-history-all
Set-Alias -Name historyall -Value search-history-all
Set-Alias -Name searchhist -Value search-history-all
Set-Alias -Name searchhistory -Value search-history-all
```
* Use it
    ```
    searchhistory code
    ```

### Built-In Autocomplete Setup

* Built-In autocomplete setup (no further install needed)
    ```
    # Search command history based on what you have already typed
    Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
    Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward

    # Show an interactive menu of matching commands/files when pressing Tab
    Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete
    ```

## git: aliases

* Create a shorter alias name for the function (e.g., 'ggc')
    ```
    function ggit-commit-custom {
        Write-Host 'Run: ' -ForegroundColor Cyan -NoNewline
        Write-Host 'git commit' -ForegroundColor Yellow
        git commit
    }

    # Optional: Create a shorter alias name for the function (e.g., 'ggc')
    Set-Alias -Name ggc -Value ggit-commit-custom
    ```
