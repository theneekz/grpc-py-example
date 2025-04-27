# gRPC Python Example

A minimal example of a gRPC service defined in a proto implemented in python without bazel.

## Usage

To regenerate pb2 files from the root directory:

```bash
python -m grpc_tools.protoc -Igen_files=.  --proto_path=. --python_out=. --grpc_python_out=. --pyi_out=. ./lobby_service.proto
```

To run the server from the root directory:

```bash
python server.py
```

To send requests to the server with postman:

- Create a new gRPC request
- Enter the URL `localhost:50051`
- Import the `proto/lobby_service.proto` proto service definition
- Select the method `ListLobbies`
- Invoke
