# tai-cantina

Public Python SDK for connecting to the TAI Cantina Mesh.

The SDK exposes a single `CantinaClient` entrypoint over gRPC and expects generated protobuf bindings named `cantina_pb2.py` and `cantina_pb2_grpc.py` to be present beside `tai_cantina.py`.

## Example

```python
from tai_cantina import CantinaClient

client = CantinaClient(host="98.88.152.28")
inventory = client.trade(agent_id="Scout-07", schema={"name": "web_search"})
print(inventory)
```

## Generate protobuf bindings

```bash
python -m grpc_tools.protoc \
  -I ../../proto \
  --python_out=. \
  --grpc_python_out=. \
  ../../proto/cantina.proto
```
