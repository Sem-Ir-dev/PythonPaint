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
        brush_size = 3
        color = 'black'
        frame_col = '#F8F8F8'
        frame_col2 = '#E0E0E0'

        up_frame = Frame(self.root, bg=frame_col, height=20)
        up_frame.place(relwidth=1)

        brush_frame = Frame(up_frame, bg=frame_col2, width=90, height=20)
        brush_frame.place(x=0, y=0)

        right_frame = Frame(self.root, bg=frame_col)
        right_frame.place(relheight=.925, relwidth=.16, relx=.83, rely=.06)

        def paint(event):
            nonlocal brush_size, color
            x1 = event.x - brush_size
            x2 = event.x + brush_size
            y1 = event.y - brush_size
            y2 = event.y + brush_size
            canvas_area.create_oval(x1, y1, x2, y2, fill=color, outline=color)

        def brush_size_change(event):
            if event.char == '\r':
                nonlocal brush_size
                new_size = size_entry.get()
                brush_size = int(new_size)

        def bg_color_change():
            nonlocal color
            canvas_area['bg'] = color

        def color_accept():
            new_color = hex_e.get()
            nonlocal bt_color, color
            bt_color['bg'] = new_color
            color = new_color

        def color_window():
            window1 = Toplevel()
            window1.geometry('250x100+300+200')

            lb_desc = Label(window1, text='Enter Hex Colors, or name\n of colors(Example: #ff1489, white)',
                            font='Arial 11')
            lb_desc.place(x=5, y=5)

            global hex_e
            hex_e = Entry(window1, width=8)
            hex_e.place(x=70, y=50)
            Button(window1, text='Accept', command=color_accept, font='Arial 12').place(x=150, y=40)

        def btn_erase():
            nonlocal color
            color = 'white'

        def canvas_size_change():
            new_width = wid.get()
            new_height = hei.get()
            canvas_area['width'] = new_width
            canvas_area['height'] = new_height

        # ============================ Верхняя боковая панель инструментов =====================================

        size_lb = Label(brush_frame, text='Brush size:', font='Arial 10', bg=frame_col2)
        size_lb.place(x=0, y=0)

        size_entry = Entry(brush_frame, width=3, bd=0, bg=frame_col2)
        size_entry.place(x=75, y=3)
        size_entry.insert(0, 3)
        size_entry.bind('<Key>', brush_size_change)

        # ============================ Правая боковая панель инструментов ======================================
        bg_btn = Button(right_frame, text='Background fill', width=14, command=lambda: bg_color_change())
        bg_btn.place(relx=.05, rely=.1)

        clear_btn = Button(right_frame, text='Clear', width=14, command=lambda: canvas_area.delete('all'))
        clear_btn.place(relx=.05, rely=.16)

        erase_btn = Button(right_frame, text='Eraser', width=14, command=btn_erase)
        erase_btn.place(relx=.05, rely=.22)

        lb_canvas = Label(right_frame, text='Canvas', width=14, bg=frame_col)
        lb_canvas.place(relx=.17, rely=.28)

        wid = Entry(right_frame, width=6)
        wid.place(relx=.05, rely=.35)

        lb_width = Label(right_frame, text='Width', width=8)
        lb_width.place(relx=.4, rely=.35)

        hei = Entry(right_frame, width=6)
        hei.place(relx=.05, rely=.40)

        lb_height = Label(right_frame, text='Height', width=8)
        lb_height.place(relx=.4, rely=.40)

        hw_accept = Button(right_frame, text='Accept', width=14, command=canvas_size_change)
        hw_accept.place(relx=.16, rely=.48)

        pallete_lb = Label(right_frame, text='Color:', font='Arial 10', bg=frame_col)
        pallete_lb.place(relx=.01, rely=0.02)

        bt_color = Button(right_frame, width=3, height=1, bg=color, command=color_window)
        bt_color.place(relx=.3, rely=.02)

        # ====================================== Холст ===================================================

        canvas_area = Canvas(self.root, width=800, height=530, bg='white')
        canvas_area.bind('<B1-Motion>', paint)
        canvas_area.place(x=10, y=35)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    window = Window(1000, 580, 200, 90, 'PythonPaint')
    window.draw_widget()
    window.run()
