"""
Màn hình chứa một ván Tic-Tac-Toe
======================================================
Nhúng TicTacToeLayout trong một Screen của Kivy và bổ sung nút
Back to Menu có màu sắc đồng bộ với các nút control khác.
"""

# ----------------------------- IMPORTS ------------------------------ #
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.app import App

from utils import style_round_button, enable_press_darken, enable_click_sound
from game_factory import create_game
from game_config import (
    BTN_RGBA,            
    BACK_LABEL,          
    DEFAULT_FONT,        
    BACK_BTN_W,          
    BACK_BTN_H,  
    SCREEN_HOME,        
)

# ------------------------------------------------------------------ #
#                           KIVY SCREEN                             #
# ------------------------------------------------------------------ #

class GameScreen(Screen):
    """`Screen` bao trọn một instance trò chơi Tic‑Tac‑Toe."""

    # --------------------------- KHỞI TẠO -----------------------------
    def __init__(
        self,
        mode: str,
        difficulty: str = "medium",
        rows: int = 5,
        cols: int = 5,
        win_len: int = 4,
        num_obstacles: int = 5,
        **kwargs,
    ):
        super().__init__(**kwargs)

        def _go_home(*_):
             # dừng nhạc trước khi về menu
            if hasattr(self.game_widget, "_sounds"):
                self.game_widget._sounds.stop_bg()
            App.get_running_app().root.current = SCREEN_HOME
            
        # 1) Sinh layout trò chơi qua factory
        self.game_widget = create_game(
            mode,
            difficulty,
            rows=rows,
            cols=cols,
            win_len=win_len,
            num_obstacles=num_obstacles,
            back_cb=_go_home,
        )
        self.add_widget(self.game_widget)

    # ----------------------- PUBLIC METHOD ---------------------------
    def apply_theme(self, theme):
        """Truyền theme mới xuống `TicTacToeLayout`."""
        if hasattr(self, "game_widget") and hasattr(self.game_widget, "apply_theme"):
            self.game_widget.apply_theme(theme)
