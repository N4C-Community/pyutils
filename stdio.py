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

import sys
from typography import styles

class stdio:
    @staticmethod
    def inp(
        msg: str,
        prompt: str = "λ",
        start: str = "",
        end: str = "\r",
        colorM: str = styles.BRIGHT_CYAN,
        colorP: str = styles.LIME,
        colorIn: str = styles.SILVER,
    ) -> str:
        sys.__stdout__.write(f"{start}{colorP}{prompt}{styles.WHITE} {colorM}{msg}>{colorIn} ")
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
    def suc(cls, msg:str) -> None:
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

    @staticmethod
    def clear() -> None:
        sys.__stdout__.write("\033[H\033[J")
        sys.__stdout__.flush()
        sys.__stdout__.write(styles.RESET)

    @staticmethod
    def copyright() -> None:
        sys.__stdout__.write("Copyright (c) 2026 RAPLI-DEV N4C\nSPDX-License-Identifier: GPL-3.0-only.")
