import grpc
from concurrent import futures
import proto.lobby_service_pb2 as lobby_service_pb2
import proto.lobby_service_pb2_grpc as lobby_service_pb2_grpc
# import lobby_service_pb2
# import lobby_service_pb2_grpc


# Example gRPC service implementation for the LobbyService.
class LobbyServiceServicer(lobby_service_pb2_grpc.LobbyServiceServicer):
    # Lists all lobbies for the ListLobbies RPC.
    def ListLobbies(self, request, context):
        response = lobby_service_pb2.ListLobbiesResponse()
        # Send dummy data as example.
        response.lobbies.add(id="lobby-1")
        response.lobbies.add(id="lobby-2")
        return response


# Start the gRPC server.
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lobby_service_pb2_grpc.add_LobbyServiceServicer_to_server(
        LobbyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Python grpc server started on port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
