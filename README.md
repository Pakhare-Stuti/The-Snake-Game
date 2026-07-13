# 🐍 Snake (Wrap-Around Edition)

A classic Snake game built from scratch in Python using **Pygame**, featuring wrap-around edge teleportation instead of traditional wall collisions. This project demonstrates core game development concepts including real-time input handling, grid-based movement, collision detection, and game state management.

## 🎮 Gameplay

Guide the snake around the grid to eat food and grow longer. Unlike traditional Snake, hitting the edge of the screen doesn't end the game — instead, the snake teleports to the opposite side. The only way to lose is by running into your own body.

## ✨ Features

- Wrap-around movement** — no wall collisions, only self-collision ends the game
- Grid-based rendering** on a 64×48 cell playfield
- Real-time score tracking** displayed on-screen
- Dynamic food spawning** at randomized grid positions
- Smooth directional controls** with reversal prevention (can't instantly double back on yourself)
- Clean game loop architecture** using Pygame's event and clock systems

## 🕹️ Controls

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |

## 🛠️ Requirements

- Python 3.x
- Pygame

## 📦 Installation

bash
# Clone the repository
git clone https://github.com/your-username/snake-wraparound.git
cd snake-wraparound

# Install dependencies
pip install pygame

# Run the game
python snake.py


## 📁 Project Structure

```
snake-wraparound/
├── The Snake Game.py       # Main game file
└── README.md       # Project documentation
```

## 🧠 What This Project Demonstrates

- Structuring a real-time game loop with Pygame
- Managing mutable game state (snake body, direction, score) across frames
- Implementing grid-based coordinate math, including modulo-based wrap-around logic
- Handling keyboard input responsively while preventing invalid state transitions
- Basic collision detection algorithms

## 🚀 Future Improvements

-  Increasing speed as score grows
-  High-score persistence (local file or database)
-  Start menu and pause functionality
-  Obstacles or power-ups
-  Sound effects and background music


## 🙋 Author

Built by Stuti Pakhare as a hands-on exercise in game development fundamentals with Python and Pygame.

---

⭐ If you found this project interesting, consider giving it a star!