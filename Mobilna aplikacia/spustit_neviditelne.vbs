Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "python -m http.server 8000", 0, False
WshShell.Run "msedge --app=http://localhost:8000", 0, False