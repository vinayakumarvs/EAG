# MCP Server with Math and Paint Automation Tools

## Description

This project demonstrates a Model Context Protocol (MCP) server implemented in Python (`server.py`) that exposes various tools, including:

*   Basic mathematical operations (add, subtract, multiply, divide, etc.)
*   String manipulation (ASCII value conversion)
*   List operations (summing exponentials, Fibonacci)
*   GUI automation for Microsoft Paint (Windows only):
    *   Opening Paint
    *   Drawing rectangles
    *   Adding text (currently linked to the final answer from the LLM)

A corresponding client (`client.py`) connects to this MCP server. The client uses the Google Gemini generative AI model to interpret a natural language query, decide which server tool(s) to call, execute them via the MCP server, and potentially chain multiple calls together to achieve a result. The final result (or intermediate steps) can trigger actions like drawing in Paint.

## Features

*   MCP server exposing multiple tools.
*   Client using Google Gemini for task decomposition and tool execution.
*   Mathematical function execution via MCP.
*   Windows GUI automation for Microsoft Paint using `pywinauto`.
*   Example workflow involving text processing and Paint interaction.

## Setup

1.  **Clone the repository or download the files.**
2.  **Navigate to the `Assignment-4` directory:**
    ```bash
    cd d:\EAG\Session-4\Assignment-4
    ```
3.  **Create a Python virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```
    Activate it:
    *   Windows (Command Prompt): `.venv\Scripts\activate`
    *   Windows (PowerShell): `.venv\Scripts\Activate.ps1`
    *   macOS/Linux: `source .venv/bin/activate`
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You might need to find and add the specific MCP library package names to `requirements.txt` if they are not standard PyPI packages).*
5.  **Configure Environment Variables:**
    *   Create a file named `.env` in the `Assignment-4` directory.
    *   Add your Google Gemini API key to the `.env` file:
        ```dotenv
        GEMINI_API_KEY=YOUR_API_KEY_HERE
        ```

## Usage

1.  **Run the MCP Server:**
    Open a terminal in the `Assignment-4` directory and run:
    ```bash
    python server.py
    ```
    The server will start and wait for a client connection.

2.  **Run the Client:**
    Open *another* terminal in the `Assignment-4` directory (ensure the virtual environment is activated if you created one). Run:
    ```bash
    python client.py
    ```
    The client will connect to the server, interact with the Gemini model based on the hardcoded query in `client.py`, call the necessary tools on the server (including opening and drawing in Paint), and print the results/actions to the console.

## Important Notes

*   **Windows Only:** The Paint automation features rely on `pywinauto` and Windows-specific application details (`mspaint.exe`, window class names). It will not work on macOS or Linux.
*   **GUI Automation Fragility:** The Paint automation uses hardcoded coordinates (e.g., for clicking tools) and timings. These might need adjustment based on your screen resolution, Paint version, and system performance. If Paint actions fail, check the coordinates and `time.sleep()` values in `server.py`.
*   **Requires Paint:** Microsoft Paint must be installed and accessible as `mspaint.exe`.
*   **API Key:** A valid Google Gemini API key is required for the client to function.
*   **MCP Library:** Ensure the correct MCP library is installed. The `requirements.txt` might need updating with the specific package name.
