# WebSocket Learning Project with OpenCV

This project is designed as a learning exercise for understanding how to implement WebSocket communication in a client-server architecture using Python, OpenCV, and WebSockets.

## Features

- Real-time communication between a WebSocket server and a client application.
- Demonstrates how to integrate OpenCV for video processing.
- Provides a foundation for learning about real-time interactions using WebSocket technology.

## Prerequisites

- Python 3.x
- OpenCV
- WebSockets (websockets library)
- Modern web browser with webcam support

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/WebSocket-Communication-Demo/websocket-learning-project.git
   cd websocket-learning-project

## Usage

1. Install the required Python packages:
```bash
pip install -r requirements.txt
2. Start the WebSocket server:
```bash
python server.py
3. Open the client application:
Open the client.html file in a modern web browser.
4. Grant necessary permissions:
Grant necessary permissions for webcam access.
5. Explore WebSocket communication:
The client will display the live webcam feed while demonstrating real-time communication through WebSockets.

## File
Server (server.py)
The server implements a simple WebSocket server that accepts video frames from the client and responds with a basic acknowledgment.

Client (client.html)
The client application captures video frames from the webcam and sends them to the server using WebSockets. The server acknowledges the received frames.

