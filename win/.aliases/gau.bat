@echo off
powershell write-host -fore Cyan 'Run: ' -NoNewline
powershell write-host -fore Yellow 'git add -u'
git add -u
