# pyutils - simple python library for stdio.
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

import sys, time, threading
from .char import ansii, ascii


class stdio:
    @staticmethod
    def inp(
        msg: str,
        prompt: str = "λ",
        start: str = "",
        end: str = "\r",
        colorM: str = ansii.FG_BRIGHT_CYAN,
        colorP: str = ansii.FG_BRIGHT_GREEN,
        colorIn: str = ansii.FG_WHITE,
    ) -> str:
        sys.__stdout__.write(
            f"{start}{colorP}{prompt}{ansii.FG_WHITE} {colorM}{msg}>{colorIn} "
        )
        sys.__stdout__.flush()
        try:
            return sys.__stdin__.readline().rstrip("\r\n")
        finally:
            sys.__stdout__.write(end)
            sys.__stdout__.flush()
            sys.__stdout__.write(ansii.RESET)

    @staticmethod
    def out(
        msg: str,
        prompt: str = "",
        start: str = "",
        end: str = "\n",
        colorM: str = ansii.FG_WHITE,
        colorP: str = ansii.FG_WHITE,
    ) -> None:
        sys.__stdout__.write(f"{start}{colorP}{prompt}{colorM}{msg}{end}")
        sys.__stdout__.flush()
        sys.__stdout__.write(ansii.RESET)

    @staticmethod
    def err(
        msg: str,
        prompt: str = "",
        start: str = "",
        end: str = "\n",
        colorM: str = ansii.FG_BRIGHT_RED,
        colorP: str = ansii.FG_BRIGHT_RED,
    ) -> None:
        sys.__stderr__.write(f"{start}{colorP}{prompt}{colorM}{msg}{end}")
        sys.__stderr__.flush()
        sys.__stderr__.write(ansii.RESET)

    @classmethod
    def suc(cls, msg: str) -> None:
        cls.out(msg, prompt="[OK] ", colorP=ansii.FG_GREEN)

    @classmethod
    def wrn(cls, msg: str) -> None:
        cls.out(msg, prompt="[WRN] ", colorP=ansii.FG_YELLOW)

    @classmethod
    def inf(cls, msg: str) -> None:
        cls.out(msg, prompt="[INF] ", colorP=ansii.FG_BLUE)

    @classmethod
    def dbg(cls, msg: str) -> None:
        cls.out(msg, prompt="[DBG] ", colorP=ansii.RESET)

    @classmethod
    def clear(cls) -> None:
        sys.__stdout__.write("\033[H\033[J")
        sys.__stdout__.flush()
        sys.__stdout__.write(ansii.RESET)

    @classmethod
    def clearln(cls) -> None:
        sys.__stdout__.write("\x1b[2K")
        sys.__stdout__.flush()
        sys.__stdout__.write(ansii.RESET)

    @staticmethod
    def copyright() -> None:
        sys.__stdout__.write(
            "Copyright (c) 2026 RAPLI-DEV N4C\nSPDX-License-Identifier: GPL-3.0-only."
        )

    @classmethod
    def _spin(
        cls,
        stop_event: threading.Event = None,
        msgL: str = "Loading...",
        msgS: str = "Done",
        msgF: str = "Fail",
    ) -> None:
        if stop_event is None:
            stop_event = threading.Event()
        _s = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        try:
            while not stop_event.is_set():
                for i in _s:
                    if stop_event.is_set():
                        break
                    sys.__stdout__.write(ansii.CURSOR_HIDE)
                    cls.out(
                        i,
                        prompt=f"{msgL} ",
                        start="\r\x1b[2K",
                        end="",
                        colorP=ansii.FG_BRIGHT_BLACK,
                        colorM=ansii.FG_CYAN,
                    )
                    sys.__stdout__.flush()
                    time.sleep(0.025)
        except Exception:
            cls.out(msgF, prompt="✘ ", start="\r\x1b[2K", colorP=ansii.FG_RED)
        finally:
            sys.__stdout__.write(ansii.CURSOR_SHOW)
            cls.out(msgS, prompt="✔ ", start="\r\x1b[2K", colorP=ansii.FG_GREEN)
            sys.__stdout__.flush()

    @classmethod
    def loading(
        cls,
        func,
        msgL: str = "Loading... ",
        msgS: str = "Done",
        msgF: str = "Fail",
    ):
        stop = threading.Event()
        t = threading.Thread(
            target=cls._spin,
            kwargs={"msgL": msgL, "msgS": msgS, "msgF": msgF, "stop_event": stop},
            daemon=True,
        )
        t.start()
        try:
            return func()
        finally:
            stop.set()
            t.join()

    def readkey() -> str:
        try:
            import msvcrt

            ch = msvcrt.getwch()
            if ch in ("\x00", "\xe0"):
                return {"H": "up", "P": "down", "K": "left", "M": "right"}.get(
                    msvcrt.getwch(), ""
                )  # return key down | up | right | left string
            if ch == "\r":
                return "enter"  # return enter string
            if ch == "\x1b":
                return "esc"  # return esc string
            if ch == "b'\r'":
                return "enter"  # return enter string
            if ch == "\x03":
                raise KeyboardInterrupt
            return ch.lower()
        except ImportError:
            # DEVELOPMENT FOR LINUX
            import termios, tty, select

            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
                if ch == "\x1b":
                    r, _, _ = select.select([sys.stdin], [], [], 0.05)
                    if not r:
                        return "esc"
                    seq = sys.stdin.read(2)
                    return {"[A": "up", "[B": "down", "[D": "left", "[C": "right"}.get(
                        seq, "esc"
                    )
                if ch in ("\r", "\n"):
                    return "enter"
                return ch.lower()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
