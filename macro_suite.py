"""
JadeSCRIPTZ Macro Suite
-----------------------
Launcher unic pentru:
  - FishBot Pro       (fishing_macro.py)
  - PixelKey Macro    (pixelkey_macro.py)

Cele doua tool-uri sunt complet SEPARATE (cod, stare, fereastra proprie).
Launcher-ul doar le deschide, nu le combina intre ele.

Author: JadeSCRIPTZ
"""

import tkinter as tk

from fishing_macro import FishBotApp
from pixelkey_macro import PixelKeyMacro

# ---- Palette (Claude-inspired, warm grey + orange) ----
BG = "#1C1917"
BG2 = "#292524"
BG3 = "#302B28"
FG = "#E7E5E4"
FG_DIM = "#A8A29E"
ORG = "#D97706"
ORG_HOVER = "#F59E0B"
FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_SUB = ("Segoe UI", 10)
FONT_CARD_T = ("Segoe UI", 14, "bold")
FONT_CARD_D = ("Segoe UI", 9)


class ToolCard(tk.Frame):
    def __init__(self, master, emoji, title, desc, command, **kw):
        super().__init__(master, bg=BG2, highlightthickness=1,
                          highlightbackground=BG3, **kw)
        inner = tk.Frame(self, bg=BG2)
        inner.pack(fill="both", expand=True, padx=22, pady=20)

        tk.Label(inner, text=emoji, bg=BG2, fg=ORG,
                 font=("Segoe UI", 30)).pack(anchor="w")
        tk.Label(inner, text=title, bg=BG2, fg=FG,
                 font=FONT_CARD_T).pack(anchor="w", pady=(10, 2))
        tk.Label(inner, text=desc, bg=BG2, fg=FG_DIM, font=FONT_CARD_D,
                 wraplength=210, justify="left").pack(anchor="w", pady=(0, 14))

        btn = tk.Button(inner, text="Deschide ▸", command=command,
                         bg=ORG, fg="#1C1917", activebackground=ORG_HOVER,
                         activeforeground="#1C1917", relief="flat", bd=0,
                         font=("Segoe UI", 10, "bold"), cursor="hand2",
                         padx=14, pady=7)
        btn.pack(anchor="w")
        btn.bind("<Enter>", lambda e: btn.config(bg=ORG_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=ORG))


class MacroSuite:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("JadeSCRIPTZ Macro Suite")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)
        w, h = 560, 380
        sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry(f"{w}x{h}+{(sw - w)//2}+{(sh - h)//2}")

        # keep references so the child windows don't get garbage collected
        self._fishbot_win = None
        self._pixelkey_win = None

        tk.Frame(root, bg=ORG, height=3).pack(fill="x")

        header = tk.Frame(root, bg=BG)
        header.pack(fill="x", padx=28, pady=(20, 4))
        tk.Label(header, text="⚡ JadeSCRIPTZ Macro Suite", bg=BG, fg=FG,
                 font=FONT_TITLE).pack(anchor="w")
        tk.Label(header, text="Alege tool-ul pe care vrei sa il pornesti.",
                 bg=BG, fg=FG_DIM, font=FONT_SUB).pack(anchor="w", pady=(2, 0))

        cards = tk.Frame(root, bg=BG)
        cards.pack(fill="both", expand=True, padx=28, pady=18)
        cards.columnconfigure(0, weight=1)
        cards.columnconfigure(1, weight=1)

        ToolCard(cards, "🎣", "FishBot Pro",
                 "Macro dedicat pentru fishing: detecteaza bobber-ul prin "
                 "pixel color si trage/arunca automat undita.",
                 self.open_fishbot).grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        ToolCard(cards, "🎮", "PixelKey Macro",
                 "Macro general: secvente de taste/click-uri, mai multe "
                 "pixel watch-points, profile, Dry Run, panic hotkey.",
                 self.open_pixelkey).grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        tk.Label(root, text="Cele doua tool-uri ruleaza independent, in ferestre separate.",
                 bg=BG, fg=FG_DIM, font=("Segoe UI", 8)).pack(pady=(0, 10))

    # ---- Openers: each tool gets its own Toplevel + its own untouched class ----
    def open_fishbot(self):
        if self._fishbot_win is not None and self._fishbot_win.winfo_exists():
            self._fishbot_win.lift()
            self._fishbot_win.focus_force()
            return
        win = tk.Toplevel(self.root)
        app = FishBotApp(win)
        win.protocol("WM_DELETE_WINDOW", app.on_close)
        self._fishbot_win = win

    def open_pixelkey(self):
        if self._pixelkey_win is not None and self._pixelkey_win.winfo_exists():
            self._pixelkey_win.lift()
            self._pixelkey_win.focus_force()
            return
        win = tk.Toplevel(self.root)
        app = PixelKeyMacro(win)
        win.protocol("WM_DELETE_WINDOW", app.on_close)
        self._pixelkey_win = win


def main():
    root = tk.Tk()
    MacroSuite(root)
    root.mainloop()


if __name__ == "__main__":
    main()
