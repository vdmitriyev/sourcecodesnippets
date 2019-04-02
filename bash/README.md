### About

Collection of various bash commands.

### Bash

* Kill/stop all process with particular port

```
kill $(ps aux | grep 8888 | awk '{print $2}')
```

