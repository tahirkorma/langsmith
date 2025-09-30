# LangSmith

This repository demonstrates how to integrate **[LangSmith](https://docs.smith.langchain.com/)** across different levels of LLM application complexity — starting from simple projects, moving into sequential chains, retrieval-augmented generation (RAG) systems, agent workflows, and finally into advanced **LangGraph**-based orchestration.  

The examples show how to **trace and monitor** not only `Runnable` objects but also custom functions, tools, and complete workflows using LangSmith’s built-in **tracing and observability features**.

---

## 🚀 What is LangSmith?
[LangSmith](https://docs.smith.langchain.com/) is a platform for:
- **Tracing**: Capturing execution details of chains, agents, tools, and custom code.
- **Debugging**: Inspecting intermediate steps, inputs, outputs, and errors.
- **Evaluation**: Measuring performance, latency, and quality of LLM applications.
- **Monitoring**: Observing tokens, costs, and metadata in production.

By wrapping your LLM application with LangSmith, you gain full visibility into how data flows through your pipelines — from input → intermediate steps → output.

---

## 📂 Repository Structure

This repo is organized to progressively show how LangSmith integrates into increasingly complex systems:

### 1. **Basic LLM Project**
- Traces a simple `Runnable` (e.g., an LLM call).
- Demonstrates how to capture inputs, outputs, and metadata.

### 2. **Sequential Chains**
- Combines multiple steps into a pipeline.
- Shows LangSmith tracing for the entire chain, including intermediate function calls.

### 3. **RAG-based Chatbot**
- Integrates LangSmith into a **retrieval-augmented generation (RAG)** chatbot.
- Demonstrates:
  - Tracing custom functions using the `@traceable` decorator.
  - Monitoring entire workflows from top to bottom.
  - Adding a **vector index** for similarity search to improve retrieval speed and relevance.
  - Capturing inputs, retrieved documents, and final responses.

### 4. **Agent Workflows**
- Shows LangSmith integration with agents that use external tools.
- Example: An agent with two tools — **search** and **weather fetcher**.
- LangSmith records each tool invocation, intermediate reasoning, and final answers.

### 5. **Complex LangGraph Workflows**
- Demonstrates LangSmith in a **LangGraph** (stateful workflow orchestration) setup
- Branching logic and intermediate node activity  
- Provides **end-to-end observability** for complex multi-agent or multi-step workflows.

---

## 🛠️ Key Concepts Used

- **`Runnable`**: Core abstraction in LangChain for composable building blocks.
- **`@traceable` decorator**: Used to wrap custom Python functions so LangSmith can trace them like standard LangChain components.
- **LangSmith Client & Tracer**: The bridge between your application and the LangSmith platform.
- **Vector Index for RAG**: Used to perform fast similarity search before answering questions.
- **Agents & Tools**: Demonstrates how LangSmith traces every tool invocation and decision made by an agent.
- **LangGraph**: Enables advanced workflows with branching, memory, and state — all monitored by LangSmith.
