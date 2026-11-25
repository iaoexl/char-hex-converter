# -*- coding: utf-8 -*-
"""
字符 ↔ 十六进制双向转换器
使用 Python + tkinter 实现「十六进制转换器」功能。

编码约定：GBK（支持中文字符）
Hex 输出格式：每字节两位大写十六进制，空格分隔，例如 "74 78 74 CE C4 B1 BE B2 E2 CA D4"
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox


# ---------------------------------------------------------------------------
# 核心转换函数
# ---------------------------------------------------------------------------

def ascii_to_hex(text: str) -> str:
    """字符串文本 → 十六进制文本（GBK 编码，空格分隔，大写）"""
    raw = text.encode("gbk")
    return " ".join(f"{b:02X}" for b in raw)


def hex_to_ascii(hex_text: str) -> str:
    """十六进制文本 → 字符串文本（GBK 解码）"""
    # 去掉所有空白字符，允许用户用空格、换行等分隔
    cleaned = "".join(hex_text.split())
    if not cleaned:
        return ""
    if len(cleaned) % 2 != 0:
        raise ValueError("十六进制文本长度必须为偶数")
    try:
        raw = bytes.fromhex(cleaned)
    except ValueError as e:
        raise ValueError(f"无效的十六进制字符：{e}") from e
    return raw.decode("gbk")


# ---------------------------------------------------------------------------
# GUI 主窗口
# ---------------------------------------------------------------------------

class HexConverterApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("十六进制转换器")
        self.root.geometry("780x560")
        self.root.minsize(640, 460)

        self._build_menu()
        self._build_widgets()

    # ---- 菜单 -----------------------------------------------------------
    def _build_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="打开Txt文件", command=self.open_txt)
        file_menu.add_command(label="打开Hex文件", command=self.open_hex)
        file_menu.add_separator()
        file_menu.add_command(label="Txt文件另存为", command=self.save_txt)
        file_menu.add_command(label="Hex文件另存为", command=self.save_hex)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)

        menubar.add_cascade(label="文件", menu=file_menu)
        self.root.config(menu=menubar)

    # ---- 控件布局 -------------------------------------------------------
    def _build_widgets(self):
        # 使用 grid 让两个编辑框各自占满一整行，中间放按钮条
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)   # 字符串区 Text
        self.root.rowconfigure(4, weight=1)   # 十六进制区 Text

        # 字符串区
        tk.Label(self.root, text="字符串文本 (Ascii)", anchor="w").grid(
            row=0, column=0, sticky="ew", padx=8, pady=(8, 2)
        )
        self.ascii_text = tk.Text(self.root, wrap="word", undo=True)
        self.ascii_text.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0, 6))

        # 按钮区
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=2, column=0, pady=6)

        tk.Button(btn_frame, text="Ascii ↓ Hex", width=16,
                  command=self.do_ascii_to_hex).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Clear", width=10,
                  command=self.do_clear).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Hex ↑ Ascii", width=16,
                  command=self.do_hex_to_ascii).pack(side="left", padx=6)

        # 十六进制区
        tk.Label(self.root, text="十六进制文本 (Hex)", anchor="w").grid(
            row=3, column=0, sticky="ew", padx=8, pady=(4, 2)
        )
        self.hex_text = tk.Text(self.root, wrap="word", undo=True)
        self.hex_text.grid(row=4, column=0, sticky="nsew", padx=8, pady=(0, 8))

    # ---- 按钮回调 -------------------------------------------------------
    def do_ascii_to_hex(self):
        text = self.ascii_text.get("1.0", "end-1c")
        try:
            result = ascii_to_hex(text)
        except Exception as e:
            messagebox.showerror("转换失败", f"字符串转十六进制时出错：\n{e}")
            return
        self.hex_text.delete("1.0", "end")
        self.hex_text.insert("1.0", result)

    def do_hex_to_ascii(self):
        hex_str = self.hex_text.get("1.0", "end-1c")
        try:
            result = hex_to_ascii(hex_str)
        except Exception as e:
            messagebox.showerror("转换失败", f"十六进制转字符串时出错：\n{e}")
            return
        self.ascii_text.delete("1.0", "end")
        self.ascii_text.insert("1.0", result)

    def do_clear(self):
        self.ascii_text.delete("1.0", "end")
        self.hex_text.delete("1.0", "end")

    # ---- 文件菜单回调 ---------------------------------------------------
    def _read_file(self, path: str) -> str:
        """优先按 GBK 读取，失败再回退 UTF-8，最后回退 latin-1。"""
        for enc in ("gbk", "utf-8", "latin-1"):
            try:
                with open(path, "r", encoding=enc) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        # 实在不行用二进制读出，按 GBK 容错解码
        with open(path, "rb") as f:
            return f.read().decode("gbk", errors="replace")

    def open_txt(self):
        path = filedialog.askopenfilename(
            title="打开Txt文件",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")],
        )
        if not path:
            return
        try:
            content = self._read_file(path)
        except OSError as e:
            messagebox.showerror("打开失败", f"无法读取文件：\n{e}")
            return
        self.ascii_text.delete("1.0", "end")
        self.ascii_text.insert("1.0", content)

    def open_hex(self):
        path = filedialog.askopenfilename(
            title="打开Hex文件",
            filetypes=[("十六进制文件", "*.hex;*.bin;*.txt"), ("所有文件", "*.*")],
        )
        if not path:
            return
        try:
            content = self._read_file(path)
        except OSError as e:
            messagebox.showerror("打开失败", f"无法读取文件：\n{e}")
            return
        self.hex_text.delete("1.0", "end")
        self.hex_text.insert("1.0", content)

    def save_txt(self):
        content = self.ascii_text.get("1.0", "end-1c")
        path = filedialog.asksaveasfilename(
            title="Txt文件另存为",
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")],
        )
        if not path:
            return
        try:
            with open(path, "w", encoding="gbk") as f:
                f.write(content)
        except OSError as e:
            messagebox.showerror("保存失败", f"无法写入文件：\n{e}")

    def save_hex(self):
        content = self.hex_text.get("1.0", "end-1c")
        path = filedialog.asksaveasfilename(
            title="Hex文件另存为",
            defaultextension=".hex",
            filetypes=[("十六进制文件", "*.hex"), ("所有文件", "*.*")],
        )
        if not path:
            return
        try:
            with open(path, "w", encoding="gbk") as f:
                f.write(content)
        except OSError as e:
            messagebox.showerror("保存失败", f"无法写入文件：\n{e}")


# ---------------------------------------------------------------------------

def main():
    root = tk.Tk()
    HexConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
