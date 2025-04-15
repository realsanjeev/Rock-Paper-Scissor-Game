# 🎮 Rock Paper Scissors - Tkinter GUI

A beautiful, modern desktop Rock Paper Scissors game built with Python and Tkinter. Features a premium UI with card-based layout, smooth animations, and professional design.

## ✨ Features

- **Modern UI Design**: Premium purple-blue color scheme with card-based layout
- **Interactive Gameplay**: Click on images or buttons to make your choice
- **Visual Feedback**: Color-coded results and dynamic score updates
- **Emoji Integration**: 🪨 Rock, 📄 Paper, ✂️ Scissors throughout the interface
- **Score Tracking**: Real-time score updates with color indicators
- **Reset Functionality**: Start a new game anytime
- **Hover Effects**: Interactive button states for better UX
- **Professional Typography**: Clean, modern fonts with visual hierarchy

## 🎨 Design Highlights

- **Card-Based Layout**: Modern glassmorphism-inspired design
- **Color-Coded States**:
  - 🔵 Blue for winning
  - 🔴 Pink for losing
  - 🟡 Gold for ties
- **Dynamic Scoring**: Score colors change based on who's leading
- **Gradient Separators**: Visual section dividers
- **Hover Effects**: Buttons respond to mouse interaction
- **Professional Spacing**: Clean, organized layout

## 📋 Requirements

- Python 3.7+
- Tkinter (usually included with Python)
- Pillow (PIL) for image handling

## 🚀 Installation

1. **Install Pillow:**
   ```bash
   pip install pillow
   ```

   Or using the virtual environment:
   ```bash
   source ../venv/bin/activate  # On Linux/Mac
   # or
   ..\venv\Scripts\activate     # On Windows
   
   pip install pillow
   ```

2. **Verify installation:**
   ```bash
   python -c "from PIL import Image; print('Pillow installed successfully!')"
   ```

## 🎯 How to Play

1. **Run the game:**
   ```bash
   python main.py
   ```

2. **Make your choice:**
   - Click on any of the three images (Rock, Paper, or Scissors)
   - Or click on the buttons below the images
   - Both are clickable!

3. **View results:**
   - The result appears immediately
   - Scores update automatically
   - Color-coded feedback shows win/loss/tie

4. **Reset game:**
   - Click the "🔄 Reset Game" button to start fresh
   - All scores reset to 0

### Game Rules

- 🪨 **Rock** crushes **Scissors**
- 📄 **Paper** covers **Rock**
- ✂️ **Scissors** cut **Paper**

## 🏗️ Project Structure

```
Tkinter-GUI/
├── main.py              # Main game application
├── images/              # Game assets
│   ├── rock.PNG        # Rock image
│   ├── paper.PNG       # Paper image
│   ├── scissor.PNG     # Scissors image
│   └── icons/          # Window icons
└── README.md           # This file
```

## 🔧 Technical Details

### Technologies Used

- **Python**: Core programming language
- **Tkinter**: GUI framework (built-in with Python)
- **PIL/Pillow**: Image processing and display
- **glob**: File path handling
- **random**: Computer choice generation

### Key Components

#### Main Window
- Size: 800x650 pixels
- Background: Deep purple-blue gradient theme
- Non-resizable for consistent layout

#### Color Palette
```python
COLORS = {
    'bg_primary': '#0f0c29',      # Deep purple-blue
    'bg_card': '#252147',         # Card background
    'accent_primary': '#667eea',  # Purple accent
    'success': '#4facfe',         # Blue (wins)
    'danger': '#fa709a',          # Pink (losses)
    'warning': '#ffd700',         # Gold (ties)
}
```

#### Game Functions

- `computer_guess()`: Generates random computer choice
- `who_win(user_guess)`: Determines winner and updates UI
- `update_score_display()`: Updates scores with color coding
- `animate_result(result_type)`: Colors result based on outcome
- `reset_game()`: Resets all scores and displays
- `create_choice_button()`: Creates interactive choice buttons
- `on_button_hover()` / `on_button_leave()`: Hover effects

### UI Elements

1. **Header**
   - Title with emoji
   - Subtitle for context
   - Gradient separator

2. **Score Card**
   - Large, readable scores
   - "You : Computer" layout
   - Dynamic color coding

3. **Result Display**
   - Outcome message with emoji
   - Player choices with emojis
   - Color-coded feedback

4. **Rules Card**
   - Compact game rules
   - Emoji indicators

5. **Choice Buttons**
   - Clickable images
   - Text buttons below
   - Hover effects
   - Hand cursor

6. **Reset Button**
   - Clear game state
   - Hover effect

## 🎨 UI Features

### Interactive Elements

- **Clickable Images**: Both images and buttons are clickable
- **Hover Cursors**: Hand pointer on interactive elements
- **Color Transitions**: Smooth color changes on hover
- **Dynamic Updates**: Real-time score and result updates

### Visual Feedback

- **Win State**: Blue colors, 🎉 emoji
- **Loss State**: Pink colors, 😢 emoji
- **Tie State**: Gold colors, 🤝 emoji
- **Leading Score**: Success color (blue)
- **Trailing Score**: Danger color (pink)

## 🐛 Troubleshooting

### "No module named 'PIL'" error
```bash
pip install pillow
```

### Images not displaying
- Ensure the `images/` folder exists
- Check that image files are present (rock.PNG, paper.PNG, scissor.PNG)
- Images will fall back to large emojis if not found

### Window too small/large
- The window is fixed at 800x650 pixels
- If it doesn't fit your screen, you can modify the `root.geometry()` line in `main.py`

### Buttons not responding
- Make sure you're clicking on either the images or the buttons below them
- Both should be clickable with a hand cursor on hover

## 🎯 Future Enhancements

- [ ] Add sound effects for game actions
- [ ] Implement game statistics and history
- [ ] Add difficulty levels (computer AI)
- [ ] Create tournament mode
- [ ] Add themes/skins
- [ ] Implement achievements
- [ ] Add animation effects for choices

## 📝 Code Overview

The application follows a clean structure:

1. **Imports**: Required libraries (tkinter, PIL, random, glob)
2. **Constants**: Colors, fonts, and configuration
3. **Window Setup**: Main window initialization
4. **Helper Functions**: UI creation utilities
5. **UI Components**: Header, score board, buttons, etc.
6. **Game Logic**: Winner determination and score tracking
7. **Event Bindings**: Click and hover handlers
8. **Main Loop**: Tkinter event loop

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available for educational purposes.

## 📚 References

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Window Icon in Tkinter](https://pythonassets.com/posts/window-icon-in-tk-tkinter/)

---

**Enjoy playing Rock Paper Scissors on your desktop! 🎮✨**