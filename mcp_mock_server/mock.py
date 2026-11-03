"""Deterministic mock MCP server for agent integration testing."""
from typing import Dict, Any, Callable, List, Optional


class MockMCPServer:
    def __init__(self):
        self._tools: Dict[str, Dict[str, Any]] = {}
        self._call_history: List[Dict[str, Any]] = []

    def register_tool(self, name: str, response_value_or_fn: Any, schema: Optional[Dict[str, Any]] = None) -> None:
        self._tools[name] = {
            "handler": response_value_or_fn,
            "schema": schema or {"type": "object", "properties": {}},
            "call_count": 0
        }

    def handle_rpc(self, request: Dict[str, Any]) -> Dict[str, Any]:
        req_id = request.get("id", 1)
        method = request.get("method")

        if method == "tools/list":
            tools_list = [{"name": k, "inputSchema": v["schema"]} for k, v in self._tools.items()]
            return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools_list}}

        if method == "tools/call":
            params = request.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name not in self._tools:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Tool '{name}' not found"}}

            tool = self._tools[name]
            tool["call_count"] += 1
            self._call_history.append({"tool": name, "arguments": args})

            handler = tool["handler"]
            if callable(handler):
                result = handler(args)
            else:
                result = handler

            return {"jsonrpc": "2.0", "id": req_id, "result": result}

        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

    def assert_called(self, tool_name: str, times: Optional[int] = None) -> bool:
        calls = [c for c in self._call_history if c["tool"] == tool_name]
        if times is not None:
            return len(calls) == times
        return len(calls) > 0
