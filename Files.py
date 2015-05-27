import os
import swiftclient.client
import time


config = {'user':'username', 
          'key':'password',
          'tenant_name':'projekt',
          'authurl':'link'}
conn = swiftclient.client.Connection(auth_version=2, **config)

Listan=[]
totalsize=0
(response, obj_list) = conn.get_container('GenomeData')
pop = raw_input("What population do you want to download?: ")
for obj in obj_list: 
    if pop in obj['name'] and "bas" not in obj['name'] and "bai" not in obj['name']:
        totalsize+=float(obj['bytes'])
        Listan.append(obj['name']) 


print str(totalsize/1024/1024/1024) +" GBytes"
print str(len(Listan)) +" files"
dl=raw_input("Start download? (y/n)")
if dl =="y":
	for i in range(0, len(Listan)-1):
		
		
		start_time = time.time()
		response, object_body =conn.get_object('GenomeData',Listan[i])
		print("Done downloading " +Listan[i] +" time: %s seconds " % (time.time() - start_time))
		start_time = time.time()
		f = open('/home/ubuntu/GenomeData/'+Listan[i], 'wb')
		f.write(object_body)
		f.close()
		print("Done writing " + Listan[i] +" time: %s seconds " % (time.time() - start_time))

print "done"
