import grpc
from concurrent import futures
import time

#import generated classes
import ip_to_address_pb2
import ip_to_address_pb2_grpc

#importing the function for location
import ip_to_address

#creating a class to define the server functions
class IpLocationServicer(ip_to_address_pb2_grpc.IpLocationServicer):
    #the function to find location is exposed here
    def GetLocationIp(self, request, context):
        #gets response that is location
        #assigning function to response variable
        response = ip_to_address_pb2.Ip()
        response.ip = ip_to_address.get_location_ip(request.ip)
        return response

#create a grpc server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#adding defined class to server
ip_to_address_pb2_grpc.add_IpLocationServicer_to_server(IpLocationServicer(),server)

#listening on port 50051
print("Starting server. Listening on port 50051")
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)