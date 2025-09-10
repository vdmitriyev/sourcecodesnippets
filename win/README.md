## Command Lines

## Hot keys

* To move a full-screen application to another monitor using a hotkey on Windows (e.g., to the left)
	```
 	Windows + Shift + Left Arrow
	```

## How to see which process binds a particular port

* Approach
   ```
   netstat -ano | findstr :<port_number>
   tasklist | findstr <PID>
   ```
* Example
   ```
   netstat -ano | findstr :8081
   tasklist | findstr 1234
   ```

## How to uses aliases on Windows

Initial ideas are from [stackoverflow](https://stackoverflow.com/questions/20530996/aliases-in-windows-command-prompt)

* Create new directory ```.aliases```
   ```
   mkdir %USERPROFILE%\.aliases
   ```
* Add location of the directory with aliases to the ```PATH```. Use "enviromental variables" or set it as follows:
   ```
   set PATH=%USERPROFILE%\.aliases;%PATH%
   ```
* Copy bat files from [.aliases](.aliases) to the newly created directory

## On using `make` on Windows

Instead of `make` use [taskfiles](https://taskfile.dev/)

* It is generally possible to use make with [MSYS2](https://github.com/vdmitriyev/learn-golang#gcc-minwg-etc-on-windows)
* How to `start` `bash-terminal` after MSYS2 installation into ```C:\\Compilers\msys64\\```
	```
	C:\\Compilers\msys64\\msys2_shell.cmd -defterm -here -no-start -ucrt64 -shell bash
	```
* However, `make` will not work properly on Windows host (many workaround required)
* Alternative: use [taskfile](https://taskfile.dev/) to create make-like tasks using YML

## SSH on Windows

* Main tools: Putty, WinSCP, MobaXTerm
* PuTTY Color Themes - https://github.com/AlexAkulov/putty-color-themes/tree/master
* (multitabs, did not use): SuperPuTTy - https://github.com/jimradford/superputty

## Interesting and useful articles and ideas

* [It's time for you to install Windows Terminal](https://www.hanselman.com/blog/its-time-for-you-to-install-windows-terminal)
   - Edit own "settings"file
   - Useful commands to run terminal
	   ```
	   wt -d . -p "Ubuntu-18.04"
	   ```
* [How to remote desktop fullscreen RDP with just SOME of your multiple monitors](https://www.hanselman.com/blog/how-to-remote-desktop-fullscreen-rdp-with-just-some-of-your-multiple-monitors)

### Additional

* [bat files: General](../bat/)
* [bat files: Python](../python/windows/)
* [win-issues.md](win-issues.md)
