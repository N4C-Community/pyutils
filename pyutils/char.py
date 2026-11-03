# pyutils - simple python library for character.
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


def _hexChar(c: str) -> str:
    return chr(int(c, 16))


# HEX Only
class ascii:
    # ===== Control Characters (0x00 - 0x1F) =====
    NUL = _hexChar("00")  # Null
    SOH = _hexChar("01")  # Start of Heading
    STX = _hexChar("02")  # Start of Text
    ETX = _hexChar("03")  # End of Text
    EOT = _hexChar("04")  # End of Transmission
    ENQ = _hexChar("05")  # Enquiry
    ACK = _hexChar("06")  # Acknowledge
    BEL = _hexChar("07")  # Bell
    BS = _hexChar("08")  # Backspace
    HT = _hexChar("09")  # Horizontal Tab
    LF = _hexChar("0A")  # Line Feed / Newline
    VT = _hexChar("0B")  # Vertical Tab
    FF = _hexChar("0C")  # Form Feed
    CR = _hexChar("0D")  # Carriage Return
    SO = _hexChar("0E")  # Shift Out
    SI = _hexChar("0F")  # Shift In
    DLE = _hexChar("10")  # Data Link Escape
    DC1 = _hexChar("11")  # Device Control 1 / XON
    DC2 = _hexChar("12")  # Device Control 2
    DC3 = _hexChar("13")  # Device Control 3 / XOFF
    DC4 = _hexChar("14")  # Device Control 4
    NAK = _hexChar("15")  # Negative Acknowledge
    SYN = _hexChar("16")  # Synchronous Idle
    ETB = _hexChar("17")  # End of Transmission Block
    CAN = _hexChar("18")  # Cancel
    EM = _hexChar("19")  # End of Medium
    SUB = _hexChar("1A")  # Substitute
    ESC = _hexChar("1B")  # Escape
    FS = _hexChar("1C")  # File Separator
    GS = _hexChar("1D")  # Group Separator
    RS = _hexChar("1E")  # Record Separator
    US = _hexChar("1F")  # Unit Separator

    # ===== Printable Characters (0x20 - 0x7E) =====
    SPACE = _hexChar("20")  # ' '
    EXCLAMATION = _hexChar("21")  # !
    DOUBLE_QUOTE = _hexChar("22")  # "
    HASH = _hexChar("23")  # #
    DOLLAR = _hexChar("24")  # $
    PERCENT = _hexChar("25")  # %
    AMPERSAND = _hexChar("26")  # &
    SINGLE_QUOTE = _hexChar("27")  # '
    LEFT_PAREN = _hexChar("28")  # (
    RIGHT_PAREN = _hexChar("29")  # )
    ASTERISK = _hexChar("2A")  # *
    PLUS = _hexChar("2B")  # +
    COMMA = _hexChar("2C")  # ,
    HYPHEN = _hexChar("2D")  # -
    PERIOD = _hexChar("2E")  # .
    SLASH = _hexChar("2F")  # /

    d0 = _hexChar("30")  # 0
    d1 = _hexChar("31")  # 1
    d2 = _hexChar("32")  # 2
    d3 = _hexChar("33")  # 3
    d4 = _hexChar("34")  # 4
    d5 = _hexChar("35")  # 5
    d6 = _hexChar("36")  # 6
    d7 = _hexChar("37")  # 7
    d8 = _hexChar("38")  # 8
    d9 = _hexChar("39")  # 9

    COLON = _hexChar("3A")  # :
    SEMICOLON = _hexChar("3B")  # ;
    LESS_THAN = _hexChar("3C")  # <
    EQUALS = _hexChar("3D")  # =
    GREATER_THAN = _hexChar("3E")  # >
    QUESTION = _hexChar("3F")  # ?
    AT = _hexChar("40")  # @

    A = _hexChar("41")
    B = _hexChar("42")
    C = _hexChar("43")
    D = _hexChar("44")
    E = _hexChar("45")
    F = _hexChar("46")
    G = _hexChar("47")
    H = _hexChar("48")
    I = _hexChar("49")
    J = _hexChar("4A")
    K = _hexChar("4B")
    L = _hexChar("4C")
    M = _hexChar("4D")
    N = _hexChar("4E")
    O = _hexChar("4F")
    P = _hexChar("50")
    Q = _hexChar("51")
    R = _hexChar("52")
    S = _hexChar("53")
    T = _hexChar("54")
    U = _hexChar("55")
    V = _hexChar("56")
    W = _hexChar("57")
    X = _hexChar("58")
    Y = _hexChar("59")
    Z = _hexChar("5A")

    LEFT_BRACKET = _hexChar("5B")  # [
    BACKSLASH = _hexChar("5C")  # \
    RIGHT_BRACKET = _hexChar("5D")  # ]
    CARET = _hexChar("5E")  # ^
    UNDERSCORE = _hexChar("5F")  # _
    GRAVE = _hexChar("60")  # `

    a = _hexChar("61")
    b = _hexChar("62")
    c = _hexChar("63")
    d = _hexChar("64")
    e = _hexChar("65")
    f = _hexChar("66")
    g = _hexChar("67")
    h = _hexChar("68")
    i = _hexChar("69")
    j = _hexChar("6A")
    k = _hexChar("6B")
    l = _hexChar("6C")
    m = _hexChar("6D")
    n = _hexChar("6E")
    o = _hexChar("6F")
    p = _hexChar("70")
    q = _hexChar("71")
    r = _hexChar("72")
    s = _hexChar("73")
    t = _hexChar("74")
    u = _hexChar("75")
    v = _hexChar("76")
    w = _hexChar("77")
    x = _hexChar("78")
    y = _hexChar("79")
    z = _hexChar("7A")

    LEFT_BRACE = _hexChar("7B")  # {
    PIPE = _hexChar("7C")  # |
    RIGHT_BRACE = _hexChar("7D")  # }
    TILDE = _hexChar("7E")  # ~

    # ===== Delete (0x7F) =====
    DEL = _hexChar("7F")


class ansii:
    # ANSI / VT100 escape sequences — built from ascii.ESC (0x1B)

    @staticmethod
    def _hexChar(c: str) -> str:
        return chr(int(c, 16))

    # ===== Reused from ascii =====
    ESC = ascii.ESC  # '\x1B' — root of all escape sequences
    BEL = ascii.BEL  # '\x07' — used as OSC terminator

    # ===== Building blocks =====
    CSI = ESC + "["  # Control Sequence Introducer
    OSC = ESC + "]"  # Operating System Command
    DCS = ESC + "P"  # Device Control String
    ST = ESC + "\\"  # String Terminator (ESC \)

    # ===== Cursor movement (default n=1) =====
    CURSOR_HOME = CSI + "H"
    CURSOR_UP = CSI + "A"
    CURSOR_DOWN = CSI + "B"
    CURSOR_FORWARD = CSI + "C"
    CURSOR_BACK = CSI + "D"
    CURSOR_NEXT_LINE = CSI + "E"
    CURSOR_PREV_LINE = CSI + "F"
    CURSOR_COL = CSI + "G"
    SAVE_CURSOR = CSI + "s"
    RESTORE_CURSOR = CSI + "u"
    SAVE_CURSOR_DEC = ESC + "7"
    RESTORE_CURSOR_DEC = ESC + "8"

    # ===== Erase =====
    ERASE_DOWN = CSI + "0J"  # cursor → end of screen
    ERASE_UP = CSI + "1J"  # start of screen → cursor
    ERASE_SCREEN = CSI + "2J"  # entire screen
    ERASE_SCREEN_SAVE = CSI + "3J"  # entire screen + scrollback (xterm)

    ERASE_EOL = CSI + "0K"  # cursor → end of line
    ERASE_BOL = CSI + "1K"  # start of line → cursor
    ERASE_LINE = CSI + "2K"  # entire line  ← your example

    # ===== Insert / Delete =====
    INSERT_CHARS = CSI + "@"
    DELETE_CHARS = CSI + "P"
    INSERT_LINES = CSI + "L"
    DELETE_LINES = CSI + "M"

    # ===== Scroll =====
    SCROLL_UP = CSI + "S"
    SCROLL_DOWN = CSI + "T"

    # ===== SGR — Style =====
    RESET = CSI + "0m"
    BOLD = CSI + "1m"
    DIM = CSI + "2m"
    ITALIC = CSI + "3m"
    UNDERLINE = CSI + "4m"
    BLINK = CSI + "5m"
    RAPID_BLINK = CSI + "6m"
    REVERSE = CSI + "7m"
    HIDDEN = CSI + "8m"
    STRIKETHROUGH = CSI + "9m"

    BOLD_OFF = CSI + "22m"
    ITALIC_OFF = CSI + "23m"
    UNDERLINE_OFF = CSI + "24m"
    BLINK_OFF = CSI + "25m"
    REVERSE_OFF = CSI + "27m"
    HIDDEN_OFF = CSI + "28m"
    STRIKE_OFF = CSI + "29m"

    # ===== SGR — Foreground =====
    FG_BLACK = CSI + "30m"
    FG_RED = CSI + "31m"
    FG_GREEN = CSI + "32m"
    FG_YELLOW = CSI + "33m"
    FG_BLUE = CSI + "34m"
    FG_MAGENTA = CSI + "35m"
    FG_CYAN = CSI + "36m"
    FG_WHITE = CSI + "37m"
    FG_DEFAULT = CSI + "39m"

    FG_BRIGHT_BLACK = CSI + "90m"
    FG_BRIGHT_RED = CSI + "91m"
    FG_BRIGHT_GREEN = CSI + "92m"
    FG_BRIGHT_YELLOW = CSI + "93m"
    FG_BRIGHT_BLUE = CSI + "94m"
    FG_BRIGHT_MAGENTA = CSI + "95m"
    FG_BRIGHT_CYAN = CSI + "96m"
    FG_BRIGHT_WHITE = CSI + "97m"

    # ===== SGR — Background =====
    BG_BLACK = CSI + "40m"
    BG_RED = CSI + "41m"
    BG_GREEN = CSI + "42m"
    BG_YELLOW = CSI + "43m"
    BG_BLUE = CSI + "44m"
    BG_MAGENTA = CSI + "45m"
    BG_CYAN = CSI + "46m"
    BG_WHITE = CSI + "47m"
    BG_DEFAULT = CSI + "49m"

    BG_BRIGHT_BLACK = CSI + "100m"
    BG_BRIGHT_RED = CSI + "101m"
    BG_BRIGHT_GREEN = CSI + "102m"
    BG_BRIGHT_YELLOW = CSI + "103m"
    BG_BRIGHT_BLUE = CSI + "104m"
    BG_BRIGHT_MAGENTA = CSI + "105m"
    BG_BRIGHT_CYAN = CSI + "106m"
    BG_BRIGHT_WHITE = CSI + "107m"

    # ===== Mode set / reset =====
    CURSOR_SHOW = CSI + "?25h"
    CURSOR_HIDE = CSI + "?25l"
    ALT_SCREEN_ON = CSI + "?1049h"
    ALT_SCREEN_OFF = CSI + "?1049l"
    BRACKET_PASTE_ON = CSI + "?2004h"
    BRACKET_PASTE_OFF = CSI + "?2004l"
    MOUSE_ON = CSI + "?1000h"
    MOUSE_OFF = CSI + "?1000l"

    # ===== Non-CSI (direct ESC) =====
    INDEX = ESC + "D"
    NEXT_LINE = ESC + "E"
    REVERSE_INDEX = ESC + "M"
    TAB_SET = ESC + "H"
    RESET_TERM = ESC + "c"

    # ===== Helpers for parameterized sequences =====
    @staticmethod
    def cursor_up(n: int = 1) -> str:
        return f"{ansii.CSI}{n}A"

    @staticmethod
    def cursor_down(n: int = 1) -> str:
        return f"{ansii.CSI}{n}B"

    @staticmethod
    def cursor_forward(n: int = 1) -> str:
        return f"{ansii.CSI}{n}C"

    @staticmethod
    def cursor_back(n: int = 1) -> str:
        return f"{ansii.CSI}{n}D"

    @staticmethod
    def cursor_pos(row: int = 1, col: int = 1) -> str:
        return f"{ansii.CSI}{row};{col}H"

    @staticmethod
    def erase_line(mode: int = 2) -> str:
        return f"{ansii.CSI}{mode}K"

    @staticmethod
    def erase_screen(mode: int = 2) -> str:
        return f"{ansii.CSI}{mode}J"

    @staticmethod
    def fg_256(n: int) -> str:
        return f"{ansii.CSI}38;5;{n}m"

    @staticmethod
    def bg_256(n: int) -> str:
        return f"{ansii.CSI}48;5;{n}m"

    @staticmethod
    def fg_rgb(r: int, g: int, b: int) -> str:
        return f"{ansii.CSI}38;2;{r};{g};{b}m"

    @staticmethod
    def bg_rgb(r: int, g: int, b: int) -> str:
        return f"{ansii.CSI}48;2;{r};{g};{b}m"

    @staticmethod
    def set_title(title: str) -> str:
        return f"{ansii.OSC}0;{title}{ansii.BEL}"
