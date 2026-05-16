import grpc
import test_pb2
import test_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50055')
    stub = test_pb2_grpc.SquareRootServiceStub(channel)
    
    response = stub.SquareRoot(test_pb2.Number(input=9))
    print(f"Result: {response.resulta}")

if __name__ == "__main__":
    main()