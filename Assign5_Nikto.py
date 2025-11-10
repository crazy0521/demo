$ sudo apt update
     Updates your system's list of available software packages. It's good practice to run this before installing anything.

$ sudo apt install nikto
     nstalls the nikto web server scanner on your system.

$ nikto -help
     Displays the help menu, showing all available options and syntax for the nikto command.

$ nikto -h linuxhint.com
    Starts a basic scan on the web server at linuxhint.com using the default HTTP port (80).

$ nikto -h pbs.org -ssl
     Starts a scan on pbs.org specifically using SSL (HTTPS) on the default port 443.

$ sudo ifconfig
     Shows your computer's network interface details, including your local IP address. (Note: ip addr is a more modern alternative)

$ sudo nmap -p 80 192.168.0.0/24 -oG linuxhint.txt
     Change the last digit of ip to 0/24 and instead of linuxhint.txt you can give any name the file will be saved by that name.
     This is an Nmap command. It scans your entire local network