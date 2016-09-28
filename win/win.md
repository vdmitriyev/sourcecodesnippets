
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
