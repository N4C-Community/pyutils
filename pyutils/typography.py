# pyutils - simple python library for typography.
# Copyright (c) 2026 RAPLI-DEV N4C
# SPDX-License-Identifier: GPL-3.0-only
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

import ctypes
import os
import sys
from typing import Final

__all__ = ["styles"]

_ENABLE_VIRTUAL_TERMINAL_PROCESSING: Final[int] = 0x0004
_STD_OUTPUT_HANDLE: Final[int] = -11


def _enable_windows_vt() -> bool:
    if sys.platform != "win32":
        return True
    try:
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(_STD_OUTPUT_HANDLE)
        mode = ctypes.c_uint32()
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        return bool(
            kernel32.SetConsoleMode(
                handle,
                mode.value | _ENABLE_VIRTUAL_TERMINAL_PROCESSING,
            )
        )
    except Exception:
        return False


def _ansi_enabled() -> bool:
    if "NO_COLOR" in os.environ:
        return False
    if "FORCE_COLOR" in os.environ:
        return True
    if not sys.__stdout__.isatty():
        return False
    return _enable_windows_vt()


_ANSI: Final[bool] = _ansi_enabled()


def _code(sequence: str) -> str:
    return f"\033[{sequence}m" if _ANSI else ""


def _fg(index: int) -> str:
    if not 0 <= index <= 255:
        raise ValueError("index must be 0..255")
    return f"\033[38;5;{index}m" if _ANSI else ""


def _bg(index: int) -> str:
    if not 0 <= index <= 255:
        raise ValueError("index must be 0..255")
    return f"\033[48;5;{index}m" if _ANSI else ""

def _cursor(sequence: str) -> str:
    return f"\033[{sequence}" if _ANSI else ""

def _validate_rgb(r: int, g: int, b: int) -> None:
    for name, value in (("r", r), ("g", g), ("b", b)):
        if not isinstance(value, int) or not 0 <= value <= 255:
            raise ValueError(f"{name} must be int 0..255")


class styles:
    RESET = _code("0")
    RESET_FG = _code("39")
    RESET_BG = _code("49")

    # Text styles
    BOLD = _code("1")
    DIM = _code("2")
    ITALIC = _code("3")
    UNDERLINE = _code("4")
    BLINK = _code("5")
    RAPID_BLINK = _code("6")
    REVERSE = _code("7")
    HIDDEN = _code("8")
    STRIKETHROUGH = _code("9")

    # Reset styles
    RESET_BOLD = _code("22")   # also resets DIM
    RESET_DIM = _code("22")    # also resets BOLD
    RESET_ITALIC = _code("23")
    RESET_UNDERLINE = _code("24")
    RESET_BLINK = _code("25")
    RESET_REVERSE = _code("27")
    RESET_HIDDEN = _code("28")
    RESET_STRIKETHROUGH = _code("29")

    # Foreground standard 16
    BLACK = _code("30")
    MAROON = _code("31")
    GREEN = _code("32")
    OLIVE = _code("33")
    NAVY = _code("34")
    PURPLE = _code("35")
    TEAL = _code("36")
    SILVER = _code("37")
    GREY = _code("90")
    RED = _code("91")
    LIME = _code("92")
    YELLOW = _code("93")
    BLUE = _code("94")
    FUCHSIA = _code("95")
    CYAN = _code("96")
    WHITE = _code("97")

    # Background standard 16
    BG_BLACK = _code("40")
    BG_MAROON = _code("41")
    BG_GREEN = _code("42")
    BG_OLIVE = _code("43")
    BG_NAVY = _code("44")
    BG_PURPLE = _code("45")
    BG_TEAL = _code("46")
    BG_SILVER = _code("47")
    BG_GREY = _code("100")
    BG_RED = _code("101")
    BG_LIME = _code("102")
    BG_YELLOW = _code("103")
    BG_BLUE = _code("104")
    BG_FUCHSIA = _code("105")
    BG_CYAN = _code("106")
    BG_WHITE = _code("107")

    # Alias bright
    BRIGHT_BLACK = GREY
    BRIGHT_RED = RED
    BRIGHT_GREEN = LIME
    BRIGHT_YELLOW = YELLOW
    BRIGHT_BLUE = BLUE
    BRIGHT_MAGENTA = FUCHSIA
    BRIGHT_WHITE = WHITE

    @staticmethod
    def fg256(index: int) -> str:
        return _fg(index)

    @staticmethod
    def bg256(index: int) -> str:
        return _bg(index)

    @staticmethod
    def fg_rgb(r: int, g: int, b: int) -> str:
        _validate_rgb(r, g, b)
        return f"\033[38;2;{r};{g};{b}m" if _ANSI else ""

    @staticmethod
    def bg_rgb(r: int, g: int, b: int) -> str:
        _validate_rgb(r, g, b)
        return f"\033[48;2;{r};{g};{b}m" if _ANSI else ""

    @staticmethod
    def hide_cursor() -> None:
        """Menyembunyikan kursor CLI jika terminal mendukung ANSI."""
        cmd = _cursor("?25l")
        if cmd:
            sys.__stdout__.write(cmd)
            sys.__stdout__.flush()

    @staticmethod
    def show_cursor() -> None:
        """Menampilkan kursor CLI kembali jika terminal mendukung ANSI."""
        cmd = _cursor("?25h")
        if cmd:
            sys.__stdout__.write(cmd)
            sys.__stdout__.flush()
