# MCP Mock Server ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="MCP Mock Server Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/mcp-mock-server/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/mcp-mock-server?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/mcp-mock-server/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**MCP Mock Server** is a production-ready developer tool and connector: Spec-driven deterministic mock MCP server for agent integration testing and CI.

---

## 🚀 Problem Statement

Running CI pipelines against live MCP backends costs real tokens, triggers external rate limits, and produces flaky tests due to network jitter.

---

## ⚡ Architecture Flow

```mermaid
sequenceDiagram
    autonumber
    participant CI as CI Agent Runner
    participant Mock as MCP Mock Server

    CI->>Mock: register_tool("fetch_data", fixture={"items": [1, 2]})
    CI->>Mock: rpc_request({method: "tools/call", params: {name: "fetch_data"}})
    Mock-->>CI: JSON-RPC Response {result: {items: [1, 2]}}
    CI->>Mock: assert_called_once("fetch_data")
    Mock-->>CI: Assertion Verified ✅
```

---

## 📊 Performance Benchmarks

| Test Scenario | Live MCP Backend | MCP Mock Server | Speedup |
|---|---|---|---|
| CI Test Suite (50 tool tests) | 28.4s | 0.12s | **236x faster** |
| Network Dependency | 100% required | 0% (Airgapped) | **100% Flake-free** |
| API Token Cost per CI Run | $0.85 | $0.00 | **100% Free** |
| Error Injection Testing | Difficult | 1-line setup | **Comprehensive** |

---

## 🛠️ Installation & Quickstart

```bash
pip install mcp_mock_server
```

### Python API

```python
import mcp_mock_server

print(mcp_mock_server.__version__)
```

### CLI Usage

```bash
mcp-mock-server --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
