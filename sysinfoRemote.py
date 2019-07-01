import psutil,os,time,sys

outputString = []

cpuPercents = psutil.cpu_percent(interval=1,percpu=True)
cpuFreq = psutil.cpu_freq(percpu=True)
cpuTemp = psutil.sensors_temperatures()
print('<meta http-equiv="refresh" content="1">')
print('<HTML><body>')
print('<div>{0:2.2f}GB used of {1:2.2f}GB system memory</div>'.format(psutil.virtual_memory()[3]/1073741824,psutil.virtual_memory()[0]/1073741824))
for socket,cpuPackage in enumerate(cpuTemp):
	dies = [cpuDie for cpuDie in cpuTemp[cpuPackage] if cpuDie[0] == 'Tdie']
	for die,cpuDie in enumerate(dies):
		print("<div>Die#{} on CPU Socket#{} Temp: {}°C</div>".format(die,socket,dies[die][1]))

for index,cpu in enumerate(cpuPercents):
	print('<div>Core#{0:2d} : {1:6.1f}% :{2:7.2f}mhz</div>'.format(index,cpu,cpuFreq[index][0]))
print('</body</HTML>')
sys.stdout.flush()
