# CDBK Chess game with AI

This is a Python-based chess game featuring an AI opponent. The project includes a graphical interface using `pygame` and intelligent move calculation using `python-chess`. The AI supports minimax with alpha-beta pruning for move evaluation.

---

## Features

- **Player vs AI**: Play as White against a Black AI opponent.
- **Checkmate and Check Detection**: Audio feedback for checks and checkmates.
- **Customizable Assets**: Supports external image and audio files for a personalized experience.
- **AI Logic**: Minimax algorithm with alpha-beta pruning for intelligent move selection.

---

## Project Structure

```
project/
├── audio/                # Folder containing audio files
│   ├── win_jingle.mp3
│   ├── loss_jingle.mp3
│   ├── check_jingle.mp3
│   └── chess_titans_jingle
├── images/               # Folder containing image files of all chess pieces
│   ├── board.png
│   ├── white_king.png
│   ├── black_queen.png
│   └── ...
├── main.py               # Main script for running the game
├── ai_logic.py           # AI-related logic
├── logic.py              # Additional game logic
├── player_cont.py        # Player control logic
├── dynam.py              # Dynamic path calculation
├── dimens.py             # Dimensions or settings
└── requirements.txt      # Python dependencies
```

---

## Requirements

- Python 3.8+
- `pygame`
- `python-chess`

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/chess-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chess-game
   ```
3. Run the game:
   ```bash
   python main.py
   ```

---

## Customization

### Audio Files
- Place your audio files in the `audio/` folder.
- Update filenames in the code to use your custom sounds.

### Image Files
- Replace the images in the `images/` folder with your own graphics.
- Ensure filenames match those referenced in the code.

---

## Features to Add

- Multiplayer mode (local or online).
- Pawn promotion
- Check sounds
- Avoid move repetitions
- Draws
- Replay system to review past games.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- [python-chess](https://python-chess.readthedocs.io/) for chess logic and move validation.
- [pygame](https://www.pygame.org/) for the graphical interface.
- [green_chess](https://greenchess.net/info.php?item=downloads) for the chess piece images.
- [Anthony Cassimiro](https://www.youtube.com/watch?v=EarwdD8Eq_0) for the in game sounds.

---

## Contact

If you have any questions or suggestions, feel free to contact me:

- Email: pravaalofficial@gmail.com
- GitHub: [CodeBreak-Matrix](https://github.com/CodeBreak-Matrix)
