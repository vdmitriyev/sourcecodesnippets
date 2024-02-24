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

### Interesting and useful articles and ideas

* [It's time for you to install Windows Terminal](https://www.hanselman.com/blog/its-time-for-you-to-install-windows-terminal)
   - Edit own "settings"file
   - Useful commands to run terminal 
	   ```
	   wt -d . -p "Ubuntu-18.04"
	   ```
* [How to remote desktop fullscreen RDP with just SOME of your multiple monitors](https://www.hanselman.com/blog/how-to-remote-desktop-fullscreen-rdp-with-just-some-of-your-multiple-monitors)

### Additional Infomation

* [win-issues.md](win-issues.md)
