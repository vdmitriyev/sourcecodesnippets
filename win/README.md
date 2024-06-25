### Command Lines

### How to see which process binds a particular port

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

### How to uses aliases on Windows

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

### Interesting and useful articles and ideas

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
