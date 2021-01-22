### About

Collection of various bash commands.

### Bash

* Kill/stop all process with particular port

```
kill $(ps aux | grep 8888 | awk '{print $2}')
```

### Linux Utils

* Cheat sheet on [Linux Performance](http://www.brendangregg.com/linuxperf.html)
![](http://www.brendangregg.com/Perf/linux_perf_tools_full.png?)


### Ubuntu (e.g. LTS 18.04) / Disk space problem

* Determine the space available on the disks
```
sudo df -h
sudo du -hsc * # size on disk
sudo du -hbc * # real size of files
sudo du -hs /var
```
* Information about disks
```
sudo lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL
```

* Remove some staff
```
sudo apt clean # remove cache
```

* Determine number of cores + CPUs
```
lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
```
```
echo "Cores = $(( $(lscpu | awk '/^Socket\(s\)/{ print $2 }') * $(lscpu | awk '/^Core\(s\) per socket/{ print $4 }') ))"
```

* List directory as tree (required: ```apt-get install tree```)
```
tree .
tree -a .
```

* Articles
    - https://askubuntu.com/questions/1224/how-do-i-determine-the-total-size-of-a-directory-folder-from-the-command-line
    - https://askubuntu.com/questions/343066/how-to-delete-a-non-working-kernel-after-update
    - https://unix.stackexchange.com/questions/218074/how-to-know-number-of-cores-of-a-system-in-linux
    
