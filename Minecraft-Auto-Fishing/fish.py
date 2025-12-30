def select_region():
    root = tk.Tk()
    root.overrideredirect(True)  # 隐藏标题栏和边框
    root.attributes('-alpha', 0.3)  # 半透明

    # 获取屏幕宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置窗口大小为200x100，并定位到右下角
    window_width = 200
    window_height = 100
    x = screen_width - window_width
    y = screen_height - window_height
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 添加提示文字
    label = tk.Label(root, text="请调整窗口覆盖字幕\n点击窗口内任意位置\n即可确定范围", font=("Arial", 10))
    label.pack(expand=True)

    # 存储选中的区域
    region = None

    def on_click(event):
        nonlocal region
        region = (event.x_root, event.y_root, event.x_root + window_width, event.y_root + window_height)
        root.destroy()

    root.bind("<Button-1>", on_click)
    root.mainloop()
    return region