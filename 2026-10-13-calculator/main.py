import tkinter as tk

ALLOWED = set("0123456789+-*/.() ")


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.resizable(False, False)

        self.entry = tk.Entry(root, font=("Arial", 22), justify="right", bd=8)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        buttons = [
            ["C", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, text in enumerate(row):
                color = "#ff9500" if text == "=" else "#e0e0e0"
                btn = tk.Button(
                    root, text=text, font=("Arial", 18), width=4, height=2,
                    bg=color, command=lambda t=text: self.on_click(t)
                )
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        root.bind("<Return>", lambda e: self.calculate())
        root.bind("<Escape>", lambda e: self.clear())

    def on_click(self, text):
        if text == "C":
            self.clear()
        elif text == "⌫":
            self.entry.delete(len(self.entry.get()) - 1, tk.END)
        elif text == "=":
            self.calculate()
        else:
            self.entry.insert(tk.END, text)

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        expression = self.entry.get()
        if not expression or not set(expression) <= ALLOWED:
            self.show("Помилка")
            return
        try:
            result = eval(expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.show(str(result))
        except ZeroDivisionError:
            self.show("Ділення на 0")
        except Exception:
            self.show("Помилка")

    def show(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()