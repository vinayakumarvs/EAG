# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
from pywinauto.application import Application
import win32gui
import win32con
import time
from win32api import GetSystemMetrics
import pyautogui
import os
from pywinauto import mouse, keyboard

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# Initialize global variables
paint_app = None

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

@mcp.tool()
async def draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """
    Draws a recursive spiral rectangle pattern in Microsoft Paint using screen automation.

    This function assumes that Microsoft Paint is already open and accessible through the 
    `paint_app` global object. It first ensures Paint is focused, selects the rectangle tool, 
    and then draws a spiral pattern of rectangles starting from a given point.

    Parameters:
    x1 (int): X-coordinate of the starting point (unused in this implementation, but reserved for future updates).
    y1 (int): Y-coordinate of the starting point (unused in this implementation, but reserved for future updates).
    x2 (int): X-coordinate of the end point (unused in this implementation, but reserved for future updates).
    y2 (int): Y-coordinate of the end point (unused in this implementation, but reserved for future updates).

    Returns:
    dict: A response dictionary containing either success text or an error message.

    System Prompt Usage:
    You can invoke this functionality with a prompt like: 
    "Draw a recursive rectangle pattern on Paint starting from coordinates (x1, y1)."

    Note:
    - Requires `pyautogui`, `time`, and a valid `paint_app` global reference.
    - Make sure Paint is open using the `open_paint` function before calling this.
    """
    global paint_app
    try:
        if not paint_app:
            return {
                "content": [
                    {"type": "text", "text": "Paint is not open. Please call open_paint first."}
                ]
            }

        paint_window = paint_app.window(class_name='MSPaintApp')

        if not paint_window.has_focus():
            paint_window.set_focus()
            time.sleep(0.5)

        
 
        pyautogui.click(826,433)
        distance = 200
        # 826,433
 
 
        while distance > 100:
            pyautogui.dragRel(distance * 2, 0, duration=0.2) # move right
            distance = distance - 5
            pyautogui.dragRel(0, distance, duration=0.2) # move down
 
            pyautogui.dragRel(-distance * 2, 0, duration=0.2) #move left
            distance = distance - 5
 
            pyautogui.dragRel(0, -distance, duration=0.2) #move up

        return {
            "content": [
                {"type": "text", "text": f"recursive rectangle pattern drawn from ({x1},{y1}))"}
            ]
        }

    except Exception as e:
        return {
            "content": [
                {"type": "text", "text": f"Error drawing rectangle: {str(e)}"}
            ]
        }

@mcp.tool()
async def add_text_in_paint(text: str) -> dict:
    """
    Adds the given text to the Microsoft Paint canvas using UI automation.

    This function simulates keyboard and mouse actions to:
    1. Activate the Paint window.
    2. Select the text tool.
    3. Click a predefined point on the canvas.
    4. Type the provided text.
    5. Exit text input mode.

    Parameters:
    text (str): The string to be typed onto the Paint canvas.

    Returns:
    dict: A dictionary with a confirmation message if successful, or an error message if it fails.

    System Prompt Usage:
    You can call this functionality with a system prompt like:
    - "Add the text 'Hello World' in Paint."
    - "Type 'Meeting at 3 PM' on the Paint canvas."

    Note:
    - Ensure Microsoft Paint is already open using the `open_paint` function.
    - Requires `pyautogui`, `time`, and access to the `paint_app` global variable.
    - Text will appear at a predefined position on the canvas (around x=950, y=500).
    """
    global paint_app
    try:
        if not paint_app:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Paint is not open. Please call open_paint first."
                    )
                ]
            }
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Ensure Paint window is active
        if not paint_window.has_focus():
            paint_window.set_focus()
            time.sleep(0.5)
        
        # Click on the Rectangle tool
        # paint_window.click_input(coords=(528, 92))
        # time.sleep(0.5)
        
        # Get the canvas area
        canvas = paint_window.child_window(class_name='MSPaintView')
        
        # Select text tool using keyboard shortcuts
        paint_window.type_keys('t')
        time.sleep(0.5)
        paint_window.type_keys('x')
        time.sleep(0.5)
        
        # Click where to start typing
        # canvas.click_input(coords=(950, 500))
        pyautogui.click(950,500)
        time.sleep(0.5)
        
        # Type the text passed from client
        paint_window.type_keys(text)
        time.sleep(0.5)
        
        # Click to exit text mode
        pyautogui.click(1125, 580)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Text:'{text}' added successfully"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error: {str(e)}"
                )
            ]
        }


@mcp.tool()
async def open_paint() -> dict:
    """
    Launches Microsoft Paint in maximized mode on the primary monitor.

    This function:
    1. Closes any existing instance of Paint (if running).
    2. Launches a new instance of Microsoft Paint (`mspaint.exe`).
    3. Maximizes the Paint window.
    4. Brings the window into focus.

    Returns:
    dict: A dictionary containing a success message or an error message if the launch fails.

    System Prompt Usage:
    This function can be triggered using prompts like:
    - "Open Microsoft Paint."
    - "Launch Paint in maximized mode."
    - "Start Paint so I can draw something."

    Note:
    - This function uses `pywinauto`, `win32gui`, and `win32con` to interact with the window.
    - A global `paint_app` variable is used to manage the Paint process.
    - Waits briefly between steps to allow the UI to initialize properly.
    """
    global paint_app
    try:
        # Close any existing Paint instance first
        try:
            if paint_app:
                paint_app.kill()
                time.sleep(0.5)
        except:
            pass
            
        # Start Paint application
        paint_app = Application().start('mspaint.exe')
        time.sleep(0.5)
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Maximize the window immediately
        win32gui.ShowWindow(paint_window.handle, win32con.SW_MAXIMIZE)
        time.sleep(0.5)
        
        # Ensure Paint window is active
        if not paint_window.has_focus():
            paint_window.set_focus()
            time.sleep(0.2)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Paint opened successfully in maximized mode"
                )
            ]
        }
    except Exception as e:
        # Make sure paint_app is None if we failed
        paint_app = None
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error opening Paint: {str(e)}"
                )
            ]
        }



    
    

# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
