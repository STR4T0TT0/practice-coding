## check my lab infrastructure##
import subprocess

def ping_server(IpAdd):
    command = ["ping", "-c", "1", IpAdd]
    try:
        output = subprocess.check_output(command)
        return True
    except subprocess.CalledProcessError:
        return False
    except Exception as e:
        print("Error in output command")
        return False

# IP addresses of labs servers
SrvIps_set = {"158.178.193.181","34.172.222.249"}

for SrvIp in SrvIps_set:
    TestAliv = ping_server(SrvIp)
    if TestAliv == False:
        print(SrvIp, " : Server 1 DOWN!")
    else:
        print(SrvIp, " : Server 1 up and running")
# End
print("Done")