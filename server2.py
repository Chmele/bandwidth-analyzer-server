import iperf3
from dbhelper import insert_data

server = iperf3.Server()
server2 = iperf3.Server()
# print('Running server: {0}:{1}'.format(server.bind_address, server.port))
server2.port = 5202
while True:
    result = server.run()
    result2 = server2.run()
    print(result)
    print(result2)
    insert_data(result)
    insert_data(result2)
