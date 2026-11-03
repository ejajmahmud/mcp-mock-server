"""Command-line interface for MCP Mock Server."""
import argparse
from .mock import MockMCPServer

def main():
    parser = argparse.ArgumentParser(description="MCP Mock Server CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate mock server tool handling")
    args = parser.parse_args()

    mock = MockMCPServer()
    mock.register_tool("get_metric", lambda args: {"val": 42, "unit": args.get("unit", "ms")})
    res = mock.handle_rpc({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": "get_metric", "arguments": {"unit": "sec"}}
    })
    print("Mock RPC response:", res)
    print("Assertion verified:", mock.assert_called("get_metric", 1))

if __name__ == "__main__":
    main()
