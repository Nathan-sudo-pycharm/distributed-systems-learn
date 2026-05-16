import grpc
from concurrent import futures

import test_pb2
import test_pb2_grpc


class SquareRootServiceServicer(test_pb2_grpc.SquareRootServiceServicer):
    def SquareRoot(self, request, context):
        resulta = request.input * request.input
        return test_pb2.Result(resulta=resulta)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    test_pb2_grpc.add_SquareRootServiceServicer_to_server(SquareRootServiceServicer(), server)
    server.add_insecure_port('localhost:50055')
    server.start()
    print("Server started on port 50055")
    server.wait_for_termination()


if __name__ == "__main__":
    main()