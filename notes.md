# gRPC & Protocol Buffers — Learning Notes

---

## What is Protocol Buffers (Protobuf)?

Created by Google to ensure efficient data transfer, particularly for communication between microservices.

Protocol Buffers is a method of **serializing and deserializing structured data**. While JSON is widely used, it is not efficient for microservice systems — which is why Protocol Buffers is preferred over JSON or XML in those contexts.

### Why Protobuf over JSON?

|                  | Protobuf              | JSON       |
| ---------------- | --------------------- | ---------- |
| Format           | Binary (0s and 1s)    | Plain text |
| Speed            | Fast                  | Slower     |
| Bandwidth        | Low                   | Higher     |
| Human readable   | No                    | Yes        |
| Interoperability | High (multi-language) | High       |

**Use Protobuf when:** communicating between internal services where speed and efficiency matter.

**Use JSON when:** data needs to be human-readable, or when sending data to a web browser.

### Key Concepts

- **Serialization** — converting structured data (like a Python object) into a format that can be transmitted over a network.
- **Deserialization** — converting that transmitted data back into a usable object on the receiving end.
- **Schema** — a defined structure that describes what fields a message contains and their types. Both sender and receiver share the same schema, which is what makes Protobuf safe and reliable.
- **Interoperability** — Protobuf schemas can generate code in multiple languages (Python, Go, Java, etc.), so services written in different languages can still communicate using the same contract.

### How data travels

In JSON, every message carries both the field name and the value:

```json
{ "task_execution_id": "abc-123", "status": "success" }
```

In Protobuf, only a **field number** travels over the wire — the field name stays in the `.proto` schema file. This is why Protobuf messages are smaller and faster.

---

## The `.proto` File

`.proto` is the file extension for Protocol Buffer schema definitions. You write your message structures and service contracts here.

Example:

```protobuf
syntax = "proto3";

message Number {
    int32 input = 1;   // field number 1
}
```

The `= 1` is not a default value — it is the **field number**, used to identify the field in the binary encoding.

---

## What is gRPC?

gRPC (**Google Remote Procedure Call**) is a framework built on top of Protocol Buffers. It lets one service call a function on another service over the network as if it were a local function call — using the `.proto` file as the contract.

---

## Setup — Installing the Required Modules

Two Python packages are needed:

```bash
pip install grpcio grpcio-tools
```

- **`grpcio`** — the core gRPC runtime for Python. Handles the actual network communication.
- **`grpcio-tools`** — contains the code generator (`protoc`) that reads your `.proto` file and generates Python classes from it.

---

## Generating Python Code from a `.proto` File

Once your `.proto` file is written, run this command to auto-generate the Python files:

```bash
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. protos/test.proto
```

### Command breakdown

| Part                          | What it does                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| `python -m grpc_tools.protoc` | Runs the protobuf compiler via Python                                               |
| `-I./protos`                  | Tells the compiler where to look for `.proto` files (`-I` = include path)           |
| `--python_out=.`              | Generates the message classes (e.g. `test_pb2.py`) in the current directory         |
| `--grpc_python_out=.`         | Generates the gRPC service stubs (e.g. `test_pb2_grpc.py`) in the current directory |
| `protos/test.proto`           | The specific `.proto` file to compile                                               |

### Files generated

- **`test_pb2.py`** — contains the message classes (do not edit manually)
- **`test_pb2_grpc.py`** — contains the server servicer base class and the client stub (do not edit manually)

---
