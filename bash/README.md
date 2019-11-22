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
sudo du -hsc *
sudo du -hs /var
```

* Remove some staff
```
sudo apt clean # remove cache
```

* Articles
    - https://askubuntu.com/questions/1224/how-do-i-determine-the-total-size-of-a-directory-folder-from-the-command-line
    - https://askubuntu.com/questions/343066/how-to-delete-a-non-working-kernel-after-update
