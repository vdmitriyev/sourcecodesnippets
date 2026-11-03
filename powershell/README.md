## About

List of commands for powershell

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

## Hints

* Adding a custom method to $PROFILE of powershell
    ```
    notepad $PROFILE
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
