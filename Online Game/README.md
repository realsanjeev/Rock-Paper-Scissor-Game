# 🎮 Rock Paper Scissors - Online Multiplayer

A modern, real-time multiplayer Rock Paper Scissors game built with Python, Pygame, and socket programming. Features a stunning UI with glassmorphism effects, smooth animations, and professional design.

## ✨ Features

- **Real-time Multiplayer**: Play against another player over a network
- **Modern UI Design**: Premium glassmorphism effects and gradient backgrounds
- **Smooth Animations**: Hover effects, scaling, and transitions
- **Visual Feedback**: Color-coded game states and emoji indicators
- **Client-Server Architecture**: Robust socket-based networking
- **Professional Typography**: Custom fonts with fallback support

## 🎨 Design Highlights

- **Gradient Backgrounds**: Deep purple-blue color scheme
- **Glassmorphism Cards**: Semi-transparent UI elements with blur effects
- **Emoji Indicators**: 🪨 Rock, 📄 Paper, ✂️ Scissors
- **Animated Buttons**: Interactive hover states with smooth scaling
- **Color-Coded States**:
  - 🔵 Blue for wins
  - 🔴 Pink for losses
  - 🟡 Gold for locked moves
  - ⚪ Gray for waiting

## 📋 Requirements

- Python 3.7+
- Pygame 2.0+

## 🚀 Installation

1. **Install dependencies:**
   ```bash
   pip install pygame
   ```

   Or using the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify installation:**
   ```bash
   python -c "import pygame; print(pygame.version.ver)"
   ```

## 🎯 How to Play

### Starting the Server

1. Open a terminal and navigate to the Online Game directory:
   ```bash
   cd "Online Game"
   ```

2. Start the server:
   ```bash
   python server.py
   ```

   You should see:
   ```
   ########## <your-hostname>
   <socket info>
   Waiting for connection, Server started
   ```

### Connecting Players

1. **Player 1** - Open a new terminal and run:
   ```bash
   python client.py
   ```

2. **Player 2** - Open another terminal and run:
   ```bash
   python client.py
   ```

3. Both players will see the menu screen. Click to start playing!

### Game Rules

- 🪨 **Rock** crushes **Scissors**
- 📄 **Paper** covers **Rock**
- ✂️ **Scissors** cut **Paper**

### Gameplay

1. Wait for both players to connect
2. Click on your choice (Rock, Paper, or Scissors)
3. Once both players have chosen, the result is revealed
4. The game automatically resets for the next round

## 🏗️ Architecture

### Project Structure

```
Online Game/
├── server.py           # Game server handling connections
├── client.py           # Game client with modern UI
├── game.py             # Game logic and state management
├── connection.py       # Network connection handler
├── button_handler.py   # Modern button UI component
├── requirements.txt    # Python dependencies
└── assets/
    ├── images/         # Game icons
    └── fonts/          # Custom fonts (optional)
```

### Components

#### `server.py`
- Manages client connections using sockets
- Handles game state synchronization
- Supports multiple concurrent games
- Uses threading for simultaneous player handling

#### `client.py`
- Renders the modern game UI using Pygame
- Handles user input and interactions
- Communicates with server via Network class
- Features:
  - Gradient backgrounds
  - Glassmorphism effects
  - Smooth animations
  - Emoji indicators
  - Hover effects

#### `game.py`
- Manages game state and logic
- Determines winners based on moves
- Tracks player actions
- Handles game resets

#### `connection.py`
- Establishes socket connection to server
- Sends and receives game data using pickle
- Handles network errors gracefully

#### `button_handler.py`
- Modern button component with glassmorphism
- Smooth hover animations
- Dynamic scaling effects
- Emoji support

## 🔧 Technical Details

### Technologies Used

- **Python**: Core programming language
- **Pygame**: GUI framework for rendering
- **Socket**: Network communication
- **Pickle**: Data serialization
- **Threading**: Concurrent client handling

### Network Configuration

- **Protocol**: TCP/IP
- **Default Port**: 1222
- **Host**: `socket.gethostname()` (local network)
- **Max Players per Game**: 2

### Game States

1. **Waiting**: Waiting for opponent to connect
2. **Ready**: Both players connected, waiting for moves
3. **Locked**: Player has made their choice
4. **Revealed**: Both players have chosen, showing results
5. **Reset**: Preparing for next round

## 🎨 UI Color Palette

```python
COLORS = {
    'bg_dark': (15, 12, 41),           # Deep purple-blue
    'bg_secondary': (26, 22, 64),      # Secondary background
    'accent_primary': (102, 126, 234), # Purple accent
    'success': (79, 172, 254),         # Blue (wins)
    'danger': (250, 112, 154),         # Pink (losses)
    'warning': (255, 215, 0),          # Gold (locked)
    'tie': (255, 193, 7),              # Amber (tie)
}
```

## 🐛 Troubleshooting

### "Connection refused" error
- Make sure the server is running before starting clients
- Check that both server and clients are on the same network
- Verify the port (1222) is not blocked by firewall

### "pygame.error: video system not initialized"
- This occurs when running in headless environments
- Ensure you have a display available (X11, Wayland, etc.)
- For remote servers, use X11 forwarding or VNC

### "EOFError: Ran out of input"
- Server disconnected or crashed
- Restart the server and reconnect clients
- Check server terminal for error messages

### Players can't connect
- Ensure both players use the same hostname/IP
- Check firewall settings
- Verify pygame is installed: `pip install pygame`

## 🎯 Future Enhancements

- [ ] Add score tracking across multiple rounds
- [ ] Implement game statistics and leaderboards
- [ ] Add sound effects for game actions
- [ ] Support for more than 2 players
- [ ] Add chat functionality
- [ ] Implement matchmaking system
- [ ] Add replay functionality
- [ ] Create spectator mode

## 📝 Notes

- The server must be running before clients can connect
- Each game supports exactly 2 players
- The server can handle multiple games simultaneously
- Game state is synchronized in real-time
- Network latency may affect gameplay experience

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available for educational purposes.

---

**Enjoy playing Rock Paper Scissors online with friends! 🎮✨**