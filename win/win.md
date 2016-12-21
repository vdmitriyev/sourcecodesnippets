
### 0x490 error or UNMOUNTABLE_BOOT_VOLUME

You need to enter "Repair Mode" and then (depends on the entrance point) select something like "Advanced diagnostic tools" and the start command prompt. Then yo need to use command from below, some times both commands are required (and also ```chkdisk /r```).

* To fix MBR
```
cd /d c:\
C:\bootrec.exe /FixMbr
```
* To fix Boot
```
cd /d c:\
C:\bootrec.exe /FixBoot
```

### Update from pure Windows 7 to Windows 7 SP1 with

* Install Windows 7 SP1 or prove that it already was installed
    + [Download Windows 7 and Server 2008 R2 Service Pack 1 (SP1)](http://www.askvg.com/download-windows-7-service-pack-1-now/)
* Recommends to install updates manually after stooping "windows update" service (actually set to "manual" state)
    + KB3050265 (installed)
    + KB3065987 (installed)
    + KB3102810 (installed)
    + KB3135445 (installed)
    + KB3138612 (installed)
    + KB3161664 (installed)
    + KB3020369 (installed)
    + KB3172605 (installed)
        - taken from here http://www.askvg.com/fix-windows-7-keeps-checking-for-updates-for-hours/
    * [Windows 7 SP1 Windows Update stuck checking for updates](http://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates)
* Then, after windows update service functioning properly (not stacking and hanging) it's good idea to install *Rollup Package*
    + [Install All Post-SP1 Updates Offline in Windows 7 Using Convenience Rollup Package](http://www.askvg.com/install-all-post-sp1-updates-offline-in-windows-7-using-convenience-rollup-package/)
* Then in case of any troubles use proper utility from Microsoft for further troubleshooting
