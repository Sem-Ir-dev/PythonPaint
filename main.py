from tkinter import *


class Window:
    def __init__(self, width, height, x, y, title, resizable=(True, True), icon=None):
        self.root = Tk()
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.iconbitmap(icon)
        self.root['bg'] = '#C0C0C0'

    def draw_widget(self):
        canvas_width = 870
        canvas_height = 565
        brush_size = 3
        color = 'black'

        def paint(event):
            nonlocal brush_size, color
            x1 = event.x - brush_size
            x2 = event.x + brush_size
            y1 = event.y - brush_size
            y2 = event.y + brush_size
            canvas_area.create_oval(x1, y1, x2, y2, fill=color, outline=color)

        # TODO
        def brush_size_change(new_size):
            nonlocal brush_size
            brush_size = new_size

        def color_change(new_color):
            nonlocal color
            color = new_color

        def bg_color_change():
            nonlocal color
            canvas_area['bg'] = color

        red_btn = Button(self.root, text='Red', width=14, command=lambda: color_change('red'))
        red_btn.grid(row=0, column=1)

        blue_btn = Button(self.root, text='Blue', width=14, command=lambda: color_change('blue'))
        blue_btn.grid(row=1, column=1)

        black_btn = Button(self.root, text='Black', width=14, command=lambda: color_change('black'))
        black_btn.grid(row=2, column=1)

        white_btn = Button(self.root, text='White', width=14, command=lambda: color_change('white'))
        white_btn.grid(row=3, column=1)

        clear_btn = Button(self.root, text='Clear', width=14, command=lambda: canvas_area.delete('all'))
        clear_btn.grid(row=4, column=1)

        bg_btn = Button(self.root, text='Background fill', width=14, command=lambda: bg_color_change())
        bg_btn.grid(row=5, column=1)

        canvas_area = Canvas(self.root, width=canvas_width, height=canvas_height, bg='white')
        canvas_area.bind('<B1-Motion>', paint)
        canvas_area.grid(row=0, column=0, rowspan=7, padx=5, pady=5, sticky=E + W + S + N)
        canvas_area.columnconfigure(6, weight=1)
        canvas_area.rowconfigure(2, weight=1)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    window = Window(1000, 580, 220, 90, 'Paint')
    window.draw_widget()
    window.run()
