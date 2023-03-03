python -m grpc_tools.protoc \
 -I. \
 --python_out=. \
 --pyi_out=. \
 --grpc_python_out=. \
 x_client/grpc/x_client.proto