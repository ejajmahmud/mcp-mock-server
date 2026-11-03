"""Unit tests for MockMCPServer."""
import unittest
from mcp_mock_server.mock import MockMCPServer

class TestMockMCPServer(unittest.TestCase):
    def test_list_tools(self):
        mock = MockMCPServer()
        mock.register_tool("t1", "static_val")
        res = mock.handle_rpc({"method": "tools/list", "id": 10})
        self.assertEqual(len(res["result"]["tools"]), 1)
        self.assertEqual(res["result"]["tools"][0]["name"], "t1")

    def test_call_tool_dynamic(self):
        mock = MockMCPServer()
        mock.register_tool("double", lambda args: args["num"] * 2)
        res = mock.handle_rpc({"method": "tools/call", "params": {"name": "double", "arguments": {"num": 21}}})
        self.assertEqual(res["result"], 42)
        self.assertTrue(mock.assert_called("double", 1))

    def test_unknown_tool_error(self):
        mock = MockMCPServer()
        res = mock.handle_rpc({"method": "tools/call", "params": {"name": "unknown"}})
        self.assertIn("error", res)

if __name__ == "__main__":
    unittest.main()
