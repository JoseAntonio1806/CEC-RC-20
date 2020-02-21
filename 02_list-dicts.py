hostnames=["R1", "R2", "R3", "S1", "S2"]
type(hostnames)

len(hostnames)

hostnames

hostnames[0]

hostnames[-1]

hostnames[0]= "RTR1"
hostnames

del hostnames[3]
hostnames

ipAddress = {"R1":"10.1.1.1", "R2":"10.2.2.1", "R3":"10.3.3.1"}
type(ipAddress)

ipAddress

ipAddress["R1"]

ipAddress["S1"]="10.1.1.10"
ipAddress
"R3" in ipAddress
