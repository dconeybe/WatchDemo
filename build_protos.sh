#!/bin/bash -xev

# Requirements:
# pip install protobuf grpcio-tools

exec python \
  -m grpc_tools.protoc \
  --proto_path=proto \
  --python_out=. \
  --grpc_python_out=. \
  $(find proto -name '*.proto')
