import subprocess

#command = 'echo "Test Inhalt text" | mail -s "Test Betreff Mail" falk.wollatz@web.de'
#result = subprocess.run([command], stdout=subprocess.PIPE)

p1 = subprocess.Popen(['echo', '"Test Inhalt text"'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['mail', '-s', '"Test Betreff Mail"', 'falk.wollatz@web.de'], stdin=p1.stdout)

print(p2.stdout)


