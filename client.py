import grpc

import ip_to_address_pb2_grpc
import ip_to_address_pb2

#opening a channel to listen to the port

channel = grpc.insecure_channel('localhost:50051')

#create a user or client
stub = ip_to_address_pb2_grpc.IpLocationStub(channel)

#sending request
address = ip_to_address_pb2.Ip(ip = "45.64.161.176")
#calling server
response = stub.GetLocationIp(address)

print(response.ip)