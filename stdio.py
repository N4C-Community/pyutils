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
from .typography import styles


class stdio:
    @staticmethod
    def inp(
        msg: str,
        prompt: str = "λ",
        start: str = "",
        end: str = "\r",
        colorM: str = styles.CYAN,
        colorP: str = styles.LIME,
        colorIn: str = styles.SILVER,
    ) -> str:
        sys.__stdout__.write(
            f"{start}{colorP}{prompt}{styles.WHITE} {colorM}{msg}>{colorIn} "
        )
        sys.__stdout__.flush()
        i = sys.__stdin__.readline().rstrip("\r\n")
        sys.__stdout__.write(end)
        sys.__stdout__.flush()
        sys.__stdout__.write(styles.RESET)
        return i

    @staticmethod
    def out(
        msg: str,
        prompt: str = "",
        start: str = "",
        end: str = "\n",
        colorM: str = styles.SILVER,
        colorP: str = styles.SILVER,
    ) -> None:
        sys.__stdout__.write(f"{start}{colorP}{prompt}{colorM}{msg}{end}")
        sys.__stdout__.flush()
        sys.__stdout__.write(styles.RESET)

    @staticmethod
    def err(
        msg: str,
        prompt: str = "",
        start: str = "",
        end: str = "\n",
        colorM: str = styles.RED,
        colorP: str = styles.RED,
    ) -> None:
        sys.__stderr__.write(f"{start}{colorP}{prompt}{colorM}{msg}{end}")
        sys.__stderr__.flush()
        sys.__stderr__.write(styles.RESET)

    @classmethod
    def suc(cls, msg: str) -> None:
        cls.out(msg, prompt="[OK] ", colorP=styles.GREEN)

    @classmethod
    def wrn(cls, msg: str) -> None:
        cls.out(msg, prompt="[WRN] ", colorP=styles.YELLOW)

    @classmethod
    def inf(cls, msg: str) -> None:
        cls.out(msg, prompt="[INF] ", colorP=styles.BLUE)

    @classmethod
    def dbg(cls, msg: str) -> None:
        cls.out(msg, prompt="[DBG] ", colorP=styles.RESET)

    @classmethod
    def clear(cls) -> None:
        sys.__stdout__.write("\033[H\033[J")
        sys.__stdout__.flush()
        sys.__stdout__.write(styles.RESET)

    @staticmethod
    def copyright() -> None:
        sys.__stdout__.write(
            "Copyright (c) 2026 RAPLI-DEV N4C\nSPDX-License-Identifier: GPL-3.0-only."
        )

    @classmethod
    def _spin(
        cls, msgL: str = "Loading...", stop_event: threading.Event = None
    ) -> None:
        if stop_event is None:
            stop_event = threading.Event()
            _s = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
            try:
                while not stop_event.is_set():
                    for i in _s:
                        if stop_event.is_set():
                            break
                        cls.clear()
                        styles.hide_cursor()
                        cls.out(
                            i,
                            prompt=msgL,
                            end="",
                            colorP=styles.GREY,
                            colorM=styles.CYAN,
                        )
                        sys.__stdout__.flush()
                        time.sleep(0.025)
            except Exception:
                cls.out("Fail", prompt="✘ ", colorP=styles.RED)
            finally:
                styles.show_cursor()
                cls.out("Done", prompt="✔ ", colorP=styles.GREEN)
                sys.__stdout__.flush()

    @classmethod
    def loading(cls, func, msgL: str = "Loading... "):
        stop = threading.Event()
        t = threading.Thread(
            target=cls._spin, kwargs={"msgL": msgL, "stop_event": stop}, daemon=True
        )
        t.start()
        try:
            return func()
        finally:
            stop.set()
            t.join()
