````markdown
# Aim Trainer 🎯
[![CI](https://github.com/Devparth7-coder/AimTrainerbyDevParth/actions/workflows/main.yml/badge.svg)](https://github.com/Devparth7-coder/AimTrainerbyDevParth/actions)

A Python-based aiming practice game built with Pygame that challenges your precision, speed, and reflexes.


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Mechanics](#game-mechanics)
- [Controls](#controls)
- [Scoring](#scoring)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Tips for Improvement](#tips-for-improvement)
- [Development](#development)
- [License](#license)
- [Contributing](#contributing)

## Overview

Aim Trainer is designed to help improve your mouse accuracy and reaction time. The game presents targets that you must click as quickly and accurately as possible. As you progress, the difficulty increases with smaller targets and faster spawn rates.

## Features

- 🎯 **Progressive Difficulty** - Targets get smaller and appear faster over time  
- 📊 **Real-time Statistics** - Track your score, accuracy, and remaining time  
- 🎮 **Simple Controls** - Easy to learn, difficult to master  
- ⏱️ **Timed Sessions** - 30-second rounds for quick practice sessions  
- 🏆 **Performance Metrics** - Detailed post-game statistics  
- 🎨 **Clean Interface** - Minimalist design that stays out of your way  
- 🔄 **Multiple Game States** - Menu, gameplay, and results screens  

## Installation

### Prerequisites
- Python 3.6 or higher
- Pip package manager

### Step-by-Step Installation

```bash
# Clone or download the game files
git clone https://github.com/yourusername/aim-trainer.git
cd aim-trainer

# Install Pygame
pip install pygame

# Run the game
python aim_trainer.py
````

### Alternative: Direct Download

1. Download `aim_trainer.py` from the repository
2. Open terminal/command prompt in the download directory
3. Install Pygame: `pip install pygame`
4. Run: `python aim_trainer.py`

## How to Play

### Starting the Game

1. Launch the game to see the main menu
2. Click **Start Game** to begin a 30-second session
3. Click on red targets as they appear on screen

### During Gameplay

* Targets appear randomly on the screen
* Click each target before it disappears
* Avoid clicking where there are no targets (counts as a miss)
* Watch the timer in the top-right corner

### Game Completion

* After 30 seconds, the game ends automatically
* View your final score and accuracy percentage
* Choose to play again or return to the main menu

## Game Mechanics

### Target Behavior

* **Appearance**: Red circles with concentric white rings
* **Spawning**: Random locations, avoiding screen edges
* **Lifetime**: 2 seconds initially, decreases with difficulty
* **Size**: Starts at 30px radius, shrinks to 15px minimum

### Difficulty Progression

* Every 5 seconds, the game increases in difficulty
* Targets spawn faster (down to 0.3 seconds between spawns)
* Targets become smaller (down to 15px radius)
* Target lifetime decreases (down to 1 second)

## Controls

| Action     | Control                       |
| ---------- | ----------------------------- |
| Start Game | Click "Start Game" button     |
| Aim        | Move mouse                    |
| Shoot      | Left mouse click              |
| Restart    | Click "Play Again" after game |
| Main Menu  | Click "Main Menu" after game  |
| Quit Game  | Close window or press Alt+F4  |

## Scoring

### Points System

* **Hit Target**: +1 point
* **Missed Click**: +0 points (counts against accuracy)
* **Expired Target**: +0 points (counts against accuracy)

### Accuracy Calculation

```
Accuracy = (Hits ÷ (Hits + Misses)) × 100%
```

### Performance Metrics

* **Novice**: 0–15 points
* **Intermediate**: 16–30 points
* **Advanced**: 31–45 points
* **Expert**: 46+ points

## Customization

### Easy Modifications

**Game Duration**

```python
self.game_duration = 30  # Change to desired seconds
```

**Target Size**

```python
self.radius = 30  # Initial target size
```

**Difficulty Settings**

```python
self.spawn_delay = 1.0  # Initial spawn delay
self.difficulty_interval = 5  # Seconds between difficulty increases
```

### Color Scheme

```python
BACKGROUND = (20, 20, 35)    # Dark blue
TARGET_COLOR = (220, 60, 60) # Red
TEXT_COLOR = (240, 240, 240) # White
```

## Troubleshooting

### Common Issues

**Game won't start:**

* Ensure Python is installed: `python --version`
* Verify Pygame installation: `pip list | grep pygame`
* Check file is named `aim_trainer.py`

**Game runs slowly:**

* Close other applications to free up system resources
* Reduce screen resolution if needed
* Update graphics drivers

**Targets not responding to clicks:**

* Check mouse is functioning properly
* Ensure game window is active/focused
* Verify no other applications are capturing mouse events

### System Requirements

* **OS**: Windows 7+, macOS 10.9+, or Linux
* **RAM**: 2GB minimum, 4GB recommended
* **Storage**: 10MB free space
* **Display**: 800×600 resolution minimum

## Tips for Improvement

1. **Focus on Accuracy** – It's better to hit fewer targets accurately than to spam clicks
2. **Use Your Peripheral Vision** – Don't just watch your cursor, scan the entire screen
3. **Practice Regularly** – Short, frequent sessions are more effective than long ones
4. **Stay Relaxed** – Tension in your hand reduces precision
5. **Find Your Rhythm** – Develop a consistent clicking tempo

## Development

This game was developed using:

* **Python 3.x**
* **Pygame** library
* Object-oriented programming principles

The code is structured with clear separation between game logic, rendering, and user interface components.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to:

* Report bugs
* Suggest new features
* Submit pull requests
* Improve documentation

---

**Happy Training!** 🎯 Improve your aim and beat your high score!


