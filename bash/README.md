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

* Determine the space available on the disks (**df**)
```
sudo df -h
```
* Determine the space available on the disks (**du**)
```
sudo du -hsc * # size on disk
sudo du -hbc * # real size of files
sudo du -hs /var
sudo du -h | sort -h # sort output
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

* Flush disk cache
```bash
sync; echo 3 > /proc/sys/vm/drop_caches
```


* Shows lines of an output file with grep
```bash
grep -n <pattern> <file> 
cat -n <file> | grep <pattern>
```
* Color the grep-match for easy reading.
```bash
alias grep='grep -inE --color=auto'
```
* Show linenumners in ```nano```
```bash
nano -l <file>
alias nano='nano -l'
```

* Relevant articles
    - https://askubuntu.com/questions/1224/how-do-i-determine-the-total-size-of-a-directory-folder-from-the-command-line
    - https://askubuntu.com/questions/343066/how-to-delete-a-non-working-kernel-after-update
    - https://unix.stackexchange.com/questions/218074/how-to-know-number-of-cores-of-a-system-in-linux
    - https://unix.stackexchange.com/questions/19480/how-to-display-line-number-while-doing-grep-on-a-file
    - https://www.tecmint.com/learn-nano-text-editor-in-linux/

### Troubleshoot network connection

* Use ```tcpdump``` utility to monitor desired ports
```bash
sudo tcpdump port 443 and '(tcp-syn|tcp-ack)!=0'
```
* Active TCP connections
```
netstat -plunt
```
* Display all active Internet connections
```
netstat -natp
```

### Configurations

* https://www.tecmint.com/restrict-ssh-user-to-directory-using-chrooted-jail/

### Useful cli utils

* ```bat``` or ```batcat``` - syntax highlighting for a large number of programming and markup languages
    - ```apt install bat```
    - https://github.com/sharkdp/bat
* ```exa``` -> ls alternative
    - have to be compiled on Ubuntu
    - https://github.com/ogham/exa


    
