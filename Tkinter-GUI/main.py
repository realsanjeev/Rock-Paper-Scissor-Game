"""
Modern GUI-based Rock Paper Scissors game using Tkinter.

This module implements a beautiful, modern rock-paper-scissors game with:
- Premium gradient-inspired color scheme
- Smooth animations and visual feedback
- Emoji-enhanced interface
- Score tracking with color-coded results
- Hover effects on buttons
- Professional typography

External libraries:
- glob: File path handling
- random: Computer choice generation
- tkinter: GUI framework
- PIL: Image processing
"""

import glob
import random
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk

# Modern Color Palette (matching other implementations)
COLORS = {
    'bg_primary': '#0f0c29',      # Deep purple-blue
    'bg_secondary': '#1a1640',    # Secondary background
    'bg_card': '#252147',         # Card background
    'accent_primary': '#667eea',  # Purple accent
    'accent_secondary': '#764ba2', # Deeper purple
    'text_primary': '#ffffff',    # White text
    'text_secondary': '#b8b8d1',  # Light gray
    'success': '#4facfe',         # Blue for wins
    'danger': '#fa709a',          # Pink for losses
    'warning': '#ffd700',         # Gold for ties
    'button_hover': '#8b9aff',    # Button hover color
}

# Game state
COMPUTER_WIN = 0
USER_WIN = 0
TIES = 0

# Image settings
IMAGE_DIR_PATH = glob.glob('images/*.PNG')
SIZE = (120, 120)

# Initialize main window
root = tk.Tk()
root.title('🎮 Rock Paper Scissors')
root.geometry('800x650')
root.configure(bg=COLORS['bg_primary'])
root.resizable(False, False)

# Set icon
try:
    large_icon = tk.PhotoImage(file="images/icons/icon-32.png")
    root.iconphoto(True, large_icon)
except Exception as err:
    print(f"[INFO]: Could not load icon: {err}")

# Custom fonts
try:
    TITLE_FONT = tkfont.Font(family="Helvetica", size=42, weight="bold")
    HEADER_FONT = tkfont.Font(family="Helvetica", size=24, weight="bold")
    SCORE_FONT = tkfont.Font(family="Helvetica", size=48, weight="bold")
    LABEL_FONT = tkfont.Font(family="Helvetica", size=14, weight="bold")
    RESULT_FONT = tkfont.Font(family="Helvetica", size=20, weight="bold")
    RULES_FONT = tkfont.Font(family="Helvetica", size=12)
except:
    TITLE_FONT = ("Arial", 42, "bold")
    HEADER_FONT = ("Arial", 24, "bold")
    SCORE_FONT = ("Arial", 48, "bold")
    LABEL_FONT = ("Arial", 14, "bold")
    RESULT_FONT = ("Arial", 20, "bold")
    RULES_FONT = ("Arial", 12)

def create_gradient_frame(parent, color1, color2, height=3):
    """Create a gradient-like separator using a canvas"""
    canvas = tk.Canvas(parent, height=height, bg=COLORS['bg_primary'], 
                      highlightthickness=0)
    canvas.create_rectangle(0, 0, 800, height, fill=color1, outline='')
    return canvas

def create_card_frame(parent, bg_color=None):
    """Create a modern card-style frame"""
    if bg_color is None:
        bg_color = COLORS['bg_card']
    
    frame = tk.Frame(parent, bg=bg_color, highlightbackground=COLORS['accent_primary'],
                    highlightthickness=2, relief=tk.FLAT)
    return frame

# Header section with gradient effect
header_frame = tk.Frame(root, bg=COLORS['bg_primary'])
header_frame.pack(pady=20)

# Title with emoji
title_label = tk.Label(
    header_frame,
    text='🎮 Rock Paper Scissors',
    font=TITLE_FONT,
    fg=COLORS['accent_primary'],
    bg=COLORS['bg_primary']
)
title_label.pack()

# Subtitle
subtitle_label = tk.Label(
    header_frame,
    text='Choose your weapon wisely!',
    font=LABEL_FONT,
    fg=COLORS['text_secondary'],
    bg=COLORS['bg_primary']
)
subtitle_label.pack(pady=(5, 0))

# Gradient separator
separator1 = create_gradient_frame(root, COLORS['accent_primary'], COLORS['bg_primary'])
separator1.pack(fill=tk.X, pady=10)

# Score board in a modern card
score_card = create_card_frame(root)
score_card.pack(pady=15)

score_container = tk.Frame(score_card, bg=COLORS['bg_card'])
score_container.pack(padx=30, pady=20)

# Score labels
you_label = tk.Label(score_container, text='You', font=LABEL_FONT,
                    fg=COLORS['text_secondary'], bg=COLORS['bg_card'])
you_label.grid(row=0, column=0, padx=40)

vs_label = tk.Label(score_container, text=':', font=SCORE_FONT,
                   fg=COLORS['text_secondary'], bg=COLORS['bg_card'])
vs_label.grid(row=1, column=1, padx=10)

computer_label = tk.Label(score_container, text='Computer', font=LABEL_FONT,
                         fg=COLORS['text_secondary'], bg=COLORS['bg_card'])
computer_label.grid(row=0, column=2, padx=40)

user_score_label = tk.Label(score_container, text='0', font=SCORE_FONT,
                           fg=COLORS['accent_primary'], bg=COLORS['bg_card'])
user_score_label.grid(row=1, column=0)

computer_score_label = tk.Label(score_container, text='0', font=SCORE_FONT,
                               fg=COLORS['accent_primary'], bg=COLORS['bg_card'])
computer_score_label.grid(row=1, column=2)

# Result display
result_frame = tk.Frame(root, bg=COLORS['bg_primary'])
result_frame.pack(pady=15)

result_label = tk.Label(
    result_frame,
    text='Make your first move!',
    font=RESULT_FONT,
    fg=COLORS['text_primary'],
    bg=COLORS['bg_primary'],
    height=2
)
result_label.pack()

choice_label = tk.Label(
    result_frame,
    text='',
    font=RULES_FONT,
    fg=COLORS['text_secondary'],
    bg=COLORS['bg_primary']
)
choice_label.pack()

# Game rules card
rules_card = create_card_frame(root)
rules_card.pack(pady=10)

rules_container = tk.Frame(rules_card, bg=COLORS['bg_card'])
rules_container.pack(padx=20, pady=10)

rules_text = "🪨 Rock crushes Scissors  •  📄 Paper covers Rock  •  ✂️ Scissors cut Paper"
rules_label = tk.Label(
    rules_container,
    text=rules_text,
    font=RULES_FONT,
    fg=COLORS['text_secondary'],
    bg=COLORS['bg_card']
)
rules_label.pack()

# Button frame
button_frame = tk.Frame(root, bg=COLORS['bg_primary'])
button_frame.pack(pady=20)

# Game logic functions
def computer_guess():
    """Generate random computer choice"""
    return random.choice(['rock', 'paper', 'scissor'])

def update_score_display():
    """Update score labels with current scores and colors"""
    user_score_label.config(text=str(USER_WIN))
    computer_score_label.config(text=str(COMPUTER_WIN))
    
    # Color code based on who's winning
    if USER_WIN > COMPUTER_WIN:
        user_score_label.config(fg=COLORS['success'])
        computer_score_label.config(fg=COLORS['danger'])
    elif USER_WIN < COMPUTER_WIN:
        user_score_label.config(fg=COLORS['danger'])
        computer_score_label.config(fg=COLORS['success'])
    else:
        user_score_label.config(fg=COLORS['accent_primary'])
        computer_score_label.config(fg=COLORS['accent_primary'])

def animate_result(result_type):
    """Animate result label based on outcome"""
    colors = {
        'win': COLORS['success'],
        'lose': COLORS['danger'],
        'tie': COLORS['warning']
    }
    result_label.config(fg=colors.get(result_type, COLORS['text_primary']))

def who_win(user_guess):
    """Determine winner and update UI"""
    global USER_WIN, COMPUTER_WIN, TIES
    
    cpu_guess = computer_guess()
    
    # Emoji mapping
    emoji_map = {
        'rock': '🪨',
        'paper': '📄',
        'scissor': '✂️'
    }
    
    # Update choice display
    choice_text = f"You chose {emoji_map[user_guess]} {user_guess.capitalize()}  |  Computer chose {emoji_map[cpu_guess]} {cpu_guess.capitalize()}"
    choice_label.config(text=choice_text)
    
    # Determine result
    if user_guess == cpu_guess:
        TIES += 1
        result_label.config(text='🤝 It\'s a Tie!')
        animate_result('tie')
    elif (user_guess == 'rock' and cpu_guess == 'scissor') or \
         (user_guess == 'paper' and cpu_guess == 'rock') or \
         (user_guess == 'scissor' and cpu_guess == 'paper'):
        USER_WIN += 1
        result_label.config(text='🎉 You Won!')
        animate_result('win')
    else:
        COMPUTER_WIN += 1
        result_label.config(text='😢 You Lost!')
        animate_result('lose')
    
    update_score_display()

def on_button_hover(event, button, choice):
    """Handle button hover effect"""
    button.config(bg=COLORS['button_hover'], cursor='hand2')

def on_button_leave(event, button, original_color):
    """Handle button leave effect"""
    button.config(bg=original_color, cursor='')

def create_choice_button(parent, choice, emoji, color, column):
    """Create a modern choice button with hover effects"""
    button_container = tk.Frame(parent, bg=COLORS['bg_primary'])
    button_container.grid(row=0, column=column, padx=15)
    
    # Load and display image
    img_label = None
    try:
        # Find image path case-insensitively
        img_path = None
        for p in IMAGE_DIR_PATH:
            if choice.lower() in p.lower():
                img_path = p
                break
        
        if img_path:
            image = Image.open(img_path)
            image.thumbnail(SIZE)
            photo = ImageTk.PhotoImage(image)
            
            img_label = tk.Label(button_container, image=photo, bg=COLORS['bg_primary'], cursor='hand2')
            img_label.image = photo  # Keep reference
            img_label.pack()
            # Make image clickable
            img_label.bind('<Button-1>', lambda e: who_win(choice))
        else:
            # If no image found, show emoji as placeholder
            img_label = tk.Label(
                button_container, 
                text=emoji, 
                font=("Arial", 60),
                bg=COLORS['bg_primary'],
                fg=COLORS['text_primary'],
                cursor='hand2'
            )
            img_label.pack()
            # Make emoji clickable
            img_label.bind('<Button-1>', lambda e: who_win(choice))
    except Exception as e:
        print(f"[INFO]: Could not load image for {choice}: {e}")
        # Show emoji as fallback
        img_label = tk.Label(
            button_container, 
            text=emoji, 
            font=("Arial", 60),
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            cursor='hand2'
        )
        img_label.pack()
        # Make emoji clickable
        img_label.bind('<Button-1>', lambda e: who_win(choice))
    
    # Modern button
    button = tk.Button(
        button_container,
        text=f"{emoji} {choice.capitalize()}",
        font=LABEL_FONT,
        bg=color,
        fg=COLORS['text_primary'],
        activebackground=COLORS['button_hover'],
        activeforeground=COLORS['text_primary'],
        relief=tk.FLAT,
        bd=0,
        padx=20,
        pady=10,
        command=lambda: who_win(choice),
        cursor='hand2'
    )
    button.pack(pady=(10, 0))
    
    # Bind hover effects
    button.bind('<Enter>', lambda e: on_button_hover(e, button, choice))
    button.bind('<Leave>', lambda e: on_button_leave(e, button, color))
    
    return button

# Create choice buttons
rock_button = create_choice_button(button_frame, 'rock', '🪨', COLORS['accent_primary'], 0)
paper_button = create_choice_button(button_frame, 'paper', '📄', COLORS['success'], 1)
scissor_button = create_choice_button(button_frame, 'scissor', '✂️', COLORS['danger'], 2)

# Reset button
reset_frame = tk.Frame(root, bg=COLORS['bg_primary'])
reset_frame.pack(pady=10)

def reset_game():
    """Reset the game scores and display"""
    global USER_WIN, COMPUTER_WIN, TIES
    USER_WIN = 0
    COMPUTER_WIN = 0
    TIES = 0
    update_score_display()
    result_label.config(text='Make your first move!', fg=COLORS['text_primary'])
    choice_label.config(text='')

reset_button = tk.Button(
    reset_frame,
    text='🔄 Reset Game',
    font=LABEL_FONT,
    bg=COLORS['bg_card'],
    fg=COLORS['text_primary'],
    activebackground=COLORS['accent_secondary'],
    activeforeground=COLORS['text_primary'],
    relief=tk.FLAT,
    bd=0,
    padx=30,
    pady=8,
    command=reset_game,
    cursor='hand2'
)
reset_button.pack()

# Hover effect for reset button
reset_button.bind('<Enter>', lambda e: reset_button.config(bg=COLORS['accent_secondary']))
reset_button.bind('<Leave>', lambda e: reset_button.config(bg=COLORS['bg_card']))

# Footer
footer_label = tk.Label(
    root,
    text='Made with ❤️ using Python & Tkinter',
    font=("Arial", 9),
    fg=COLORS['text_secondary'],
    bg=COLORS['bg_primary']
)
footer_label.pack(side=tk.BOTTOM, pady=10)

if __name__ == "__main__":
    root.mainloop()
