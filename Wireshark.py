# Step 1: install wireshark

# Step 2: under capture select any running option, 

# Step 3: add filter to see sepcific things like TCP/UDP

# Step 4: to capture packets of external websites 

# in terminal command : 
# ubuntu : host www.google.com, dig +short www.google.com
# cmd: ping www.google.com
# # will get the ip address of google

# in filter section : ip.addr == <google_ip_address>
# ex:
# ip.addr == 103.102.166.224

# to only see tcp: tcp and ip.addr == 103.102.166.224