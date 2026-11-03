# pyutils - simple python library for universal utils.
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
from .stdio import stdio
from .char import ansii


class feat:
    @staticmethod
    def parse(fe):
        return [
            (i, f.replace("#DIS", ""), False) if "#DIS" in f else (i, f, True)
            for i, f in enumerate(fe)
        ]

    @staticmethod
    def option(d, s=-1):
        return [
            f"[{i}] {d}" if s < 0 else f"{'▸' if j == s else ' '} [{i}] {d}"
            for j, (i, d, en) in enumerate(
                [(i, d, en) for i, d, en in feat.parse(d) if en]
            )
        ]

    @staticmethod
    def width(t, ls, p):
        return max([len(l) for l in ls] + [len(f" {t} ")]) + p

    @staticmethod
    def header(w, t, h):
        return f" {t} ".center(w, h)

    @staticmethod
    def footer(w, h):
        return w * h

    @staticmethod
    def generator(
        data: list[str],
        title: str = "MENU",
        pad: int = 5,
        hBorder: str = "─",
        selected: int = -1,
    ) -> dict:
        option = feat.option(data, selected)
        if not option:
            return {}

        width = feat.width(title, option, pad)
        if (width - len(f" {title} ")) % 2:
            width += 1

        return {
            "head": feat.header(width, title, hBorder),
            "option": option,
            "footer": feat.footer(width, hBorder),
        }

    @staticmethod
    def choice(data, title="MENU", pad=5, hBorder="─", default=0):
        enabled = [i for i, d in enumerate(data) if "#DIS" not in d]
        if not enabled:
            return None

        idx = max(0, min(default, len(enabled) - 1))
        height = 0

        try:
            sys.__stdout__.write(ansii.CURSOR_HIDE)
            sys.__stdout__.flush()

            while True:
                parts = feat.generator(data, title, pad, hBorder, selected=idx)
                if not parts:
                    return None

                lines = [parts["head"], *parts["option"], parts["footer"]]

                if height:
                    sys.__stdout__.write(f"\x1b[{height}A\x1b[J")
                sys.__stdout__.write("\n".join(lines) + "\n")
                sys.__stdout__.flush()
                height = len(lines)

                key = stdio.readkey()
                if key == "up":
                    idx = (idx - 1) % len(enabled)
                elif key == "down":
                    idx = (idx + 1) % len(enabled)
                elif key == "enter":
                    return enabled[idx]
                elif key in ("esc", "q"):
                    return None
                elif key.isdigit():
                    for k, orig in enumerate(enabled):
                        if orig == int(key):
                            idx = k
                            break
        finally:
            sys.__stdout__.write(ansii.CURSOR_SHOW)
            sys.__stdout__.flush()
