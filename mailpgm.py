import subprocess

command = 'echo "Test Inhalt text" | mail -s "Test Betreff Mail" falk.wollatz@web.de'
result = subprocess.run([command], stdout=subprocess.PIPE)

print(result.stdout)


