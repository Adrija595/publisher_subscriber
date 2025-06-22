from concurrent import futures
import grpc
import store_pb2
import store_pb2_grpc

class StoreServiceServicer(store_pb2_grpc.StoreServiceServicer):
    def SaveRegress(self, request, context):
        print(f"[Regress] Model: {request.model_name}, Features: {request.features}, Prediction: {request.predicted_value}")
        return store_pb2.SaveResponse(success=True, message="Regression result saved.")

    def SaveClassify(self, request, context):
        print(f"[Classify] Model: {request.model_name}, Features: {request.features}, Label: {request.predicted_label}")
        return store_pb2.SaveResponse(success=True, message="Classification result saved.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    store_pb2_grpc.add_StoreServiceServicer_to_server(StoreServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("🚀 gRPC StoreService running on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()