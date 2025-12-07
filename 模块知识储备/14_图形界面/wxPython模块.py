# wxPython模块详解

## 模块概述

wxPython是Python的跨平台GUI开发库，基于wxWidgets（一个用C++编写的跨平台GUI库）。wxPython允许开发者使用Python创建原生外观的桌面应用程序，支持Windows、macOS和Linux等操作系统。wxPython提供了丰富的GUI组件和工具，适合开发各种复杂程度的桌面应用程序。

## 安装方法

wxPython可以使用pip进行安装：

```bash
pip install wxPython
```

注意：wxPython的安装可能因操作系统和Python版本而异。在某些平台上，可能需要安装额外的依赖库。

## 基本概念

### 应用程序（App）

`wx.App`是wxPython应用程序的核心，负责管理应用程序的事件循环和资源。每个wxPython应用程序必须有且只有一个`wx.App`实例。

### 框架（Frame）

`wx.Frame`是wxPython应用程序的主窗口，提供了菜单栏、工具栏、状态栏和客户区等基本结构。

### 面板（Panel）

`wx.Panel`是一个容器组件，用于组织其他组件。面板通常作为框架的客户区，提供了基本的背景和事件处理功能。

### 组件（Widget）

组件是wxPython应用程序中的基本元素，如按钮、标签、文本框等。wxPython提供了多种组件，每种组件都有特定的功能和外观。

### 布局管理器（Sizer）

布局管理器用于管理组件在容器中的位置和大小，如`wx.BoxSizer`、`wx.GridSizer`、`wx.FlexGridSizer`等。

### 事件（Event）

事件是用户与GUI应用程序交互的动作，如点击按钮、键盘输入等。wxPython使用事件驱动编程模式，通过绑定事件处理函数来响应用户操作。

## 基本用法

### 创建窗口

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        # 调用父类构造函数
        super().__init__(None, title="My First wxPython App", size=(400, 300))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建标签
        self.label = wx.StaticText(self.panel, label="Hello, wxPython!", pos=(150, 100))
        
        # 显示窗口
        self.Show()

if __name__ == "__main__":
    # 创建应用程序实例
    app = wx.App()
    
    # 创建窗口实例
    frame = MyFrame()
    
    # 运行应用程序的事件循环
    app.MainLoop()
```

### 布局管理

wxPython提供了多种布局管理器（Sizer），用于管理组件在容器中的位置和大小。

#### 盒子布局（wx.BoxSizer）

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="BoxSizer Example", size=(400, 300))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建垂直盒子布局
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 添加组件
        self.label1 = wx.StaticText(self.panel, label="Label 1")
        self.vbox.Add(self.label1, 0, wx.ALL | wx.CENTER, 10)
        
        self.button1 = wx.Button(self.panel, label="Button 1")
        self.vbox.Add(self.button1, 0, wx.ALL | wx.CENTER, 10)
        
        self.label2 = wx.StaticText(self.panel, label="Label 2")
        self.vbox.Add(self.label2, 0, wx.ALL | wx.CENTER, 10)
        
        self.button2 = wx.Button(self.panel, label="Button 2")
        self.vbox.Add(self.button2, 0, wx.ALL | wx.CENTER, 10)
        
        # 设置面板的布局
        self.panel.SetSizer(self.vbox)
        
        # 显示窗口
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
```

#### 网格布局（wx.GridSizer）

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="GridSizer Example", size=(400, 300))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建网格布局（3行2列）
        self.gridsizer = wx.GridSizer(rows=3, cols=2, hgap=10, vgap=10)
        
        # 添加组件
        self.label1 = wx.StaticText(self.panel, label="Name:")
        self.gridsizer.Add(self.label1, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        
        self.textctrl1 = wx.TextCtrl(self.panel)
        self.gridsizer.Add(self.textctrl1, 0, wx.ALL | wx.EXPAND, 10)
        
        self.label2 = wx.StaticText(self.panel, label="Email:")
        self.gridsizer.Add(self.label2, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        
        self.textctrl2 = wx.TextCtrl(self.panel)
        self.gridsizer.Add(self.textctrl2, 0, wx.ALL | wx.EXPAND, 10)
        
        self.button = wx.Button(self.panel, label="Submit")
        self.gridsizer.Add(self.button, 0, wx.ALL | wx.ALIGN_CENTER, 10)
        
        # 设置面板的布局
        self.panel.SetSizer(self.gridsizer)
        
        # 显示窗口
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
```

#### 弹性网格布局（wx.FlexGridSizer）

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="FlexGridSizer Example", size=(400, 300))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建弹性网格布局（2行2列）
        self.flexgridsizer = wx.FlexGridSizer(rows=2, cols=2, hgap=10, vgap=10)
        self.flexgridsizer.AddGrowableCol(1)  # 第1列可增长
        
        # 添加组件
        self.label1 = wx.StaticText(self.panel, label="Name:")
        self.flexgridsizer.Add(self.label1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        
        self.textctrl1 = wx.TextCtrl(self.panel)
        self.flexgridsizer.Add(self.textctrl1, 0, wx.ALL | wx.EXPAND, 10)
        
        self.label2 = wx.StaticText(self.panel, label="Email:")
        self.flexgridsizer.Add(self.label2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        
        self.textctrl2 = wx.TextCtrl(self.panel)
        self.flexgridsizer.Add(self.textctrl2, 0, wx.ALL | wx.EXPAND, 10)
        
        # 设置面板的布局
        self.panel.SetSizer(self.flexgridsizer)
        
        # 显示窗口
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
```

### 事件处理

事件处理是GUI应用程序的核心，用于响应用户操作。在wxPython中，可以使用`Bind`方法绑定事件处理函数。

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Event Handling Example", size=(400, 300))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建垂直盒子布局
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 创建标签和按钮
        self.label = wx.StaticText(self.panel, label="Hello, wxPython!")
        self.vbox.Add(self.label, 0, wx.ALL | wx.CENTER, 20)
        
        self.button = wx.Button(self.panel, label="Click Me")
        self.vbox.Add(self.button, 0, wx.ALL | wx.CENTER, 10)
        
        # 绑定事件处理函数
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
        
        # 设置面板的布局
        self.panel.SetSizer(self.vbox)
        
        # 显示窗口
        self.Show()
    
    def on_button_click(self, event):
        """按钮点击事件处理函数"""
        self.label.SetLabel("Button clicked!")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
```

### 菜单栏、工具栏和状态栏

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Menu, Toolbar and Statusbar Example", size=(600, 400))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建菜单栏
        menubar = wx.MenuBar()
        
        # 创建文件菜单
        file_menu = wx.Menu()
        
        # 创建打开菜单项
        open_menu_item = file_menu.Append(wx.ID_OPEN, "&Open	Ctrl+O", "Open a file")
        self.Bind(wx.EVT_MENU, self.on_open, open_menu_item)
        
        # 创建保存菜单项
        save_menu_item = file_menu.Append(wx.ID_SAVE, "&Save	Ctrl+S", "Save a file")
        self.Bind(wx.EVT_MENU, self.on_save, save_menu_item)
        
        # 创建分隔线
        file_menu.AppendSeparator()
        
        # 创建退出菜单项
        exit_menu_item = file_menu.Append(wx.ID_EXIT, "&Exit	Ctrl+Q", "Exit application")
        self.Bind(wx.EVT_MENU, self.on_exit, exit_menu_item)
        
        # 将文件菜单添加到菜单栏
        menubar.Append(file_menu, "&File")
        
        # 创建帮助菜单
        help_menu = wx.Menu()
        
        # 创建关于菜单项
        about_menu_item = help_menu.Append(wx.ID_ABOUT, "&About", "About application")
        self.Bind(wx.EVT_MENU, self.on_about, about_menu_item)
        
        # 将帮助菜单添加到菜单栏
        menubar.Append(help_menu, "&Help")
        
        # 设置菜单栏
        self.SetMenuBar(menubar)
        
        # 创建工具栏
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_OPEN, "Open", wx.Bitmap(16, 16), "Open a file")
        toolbar.AddTool(wx.ID_SAVE, "Save", wx.Bitmap(16, 16), "Save a file")
        toolbar.AddSeparator()
        toolbar.AddTool(wx.ID_EXIT, "Exit", wx.Bitmap(16, 16), "Exit application")
        toolbar.Realize()
        
        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("Ready")
        
        # 显示窗口
        self.Show()
    
    def on_open(self, event):
        """打开文件"""
        with wx.FileDialog(self, "Open File", wildcard="All Files (*.*)|*.*|Text Files (*.txt)|*.txt",
                          style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            # 获取选中的文件路径
            pathname = fileDialog.GetPath()
            self.SetStatusText(f"Opened: {pathname}")
    
    def on_save(self, event):
        """保存文件"""
        with wx.FileDialog(self, "Save File", wildcard="All Files (*.*)|*.*|Text Files (*.txt)|*.txt",
                          style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            # 获取选中的文件路径
            pathname = fileDialog.GetPath()
            self.SetStatusText(f"Saved: {pathname}")
    
    def on_exit(self, event):
        """退出应用程序"""
        self.Close(True)
    
    def on_about(self, event):
        """显示关于对话框"""
        wx.MessageBox("This is a wxPython menu example.", "About", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
```

## 高级用法

### 对话框

wxPython提供了多种对话框，用于与用户进行交互。

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Dialog Example", size=(400, 300))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建垂直盒子布局
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 创建按钮
        self.info_button = wx.Button(self.panel, label="Show Information Dialog")
        self.vbox.Add(self.info_button, 0, wx.ALL | wx.CENTER, 10)
        self.info_button.Bind(wx.EVT_BUTTON, self.on_info_button_click)
        
        self.warning_button = wx.Button(self.panel, label="Show Warning Dialog")
        self.vbox.Add(self.warning_button, 0, wx.ALL | wx.CENTER, 10)
        self.warning_button.Bind(wx.EVT_BUTTON, self.on_warning_button_click)
        
        self.error_button = wx.Button(self.panel, label="Show Error Dialog")
        self.vbox.Add(self.error_button, 0, wx.ALL | wx.CENTER, 10)
        self.error_button.Bind(wx.EVT_BUTTON, self.on_error_button_click)
        
        self.question_button = wx.Button(self.panel, label="Show Question Dialog")
        self.vbox.Add(self.question_button, 0, wx.ALL | wx.CENTER, 10)
        self.question_button.Bind(wx.EVT_BUTTON, self.on_question_button_click)
        
        # 设置面板的布局
        self.panel.SetSizer(self.vbox)
        
        # 显示窗口
        self.Show()
    
    def on_info_button_click(self, event):
        """显示信息对话框"""
        wx.MessageBox("This is an information message.", "Information", wx.OK | wx.ICON_INFORMATION)
    
    def on_warning_button_click(self, event):
        """显示警告对话框"""
        wx.MessageBox("This is a warning message.", "Warning", wx.OK | wx.ICON_WARNING)
    
    def on_error_button_click(self, event):
        """显示错误对话框"""
        wx.MessageBox("This is an error message.", "Error", wx.OK | wx.ICON_ERROR)
    
    def on_question_button_click(self, event):
        """显示问题对话框"""
        result = wx.MessageBox("Do you want to continue?", "Question", wx.YES_NO | wx.ICON_QUESTION)
        if result == wx.YES:
            print("Yes clicked")
        else:
            print("No clicked")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
```

### 自定义组件

wxPython允许开发者创建自定义组件，继承自现有的组件类。

```python
import wx

class CustomPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        
        # 设置面板的大小
        self.SetSize((200, 100))
        
        # 初始化计数
        self.count = 0
        
        # 绑定绘制事件
        self.Bind(wx.EVT_PAINT, self.on_paint)
    
    def on_paint(self, event):
        """绘制事件处理函数"""
        dc = wx.PaintDC(self)
        
        # 设置背景颜色
        dc.SetBackground(wx.Brush(wx.Colour(200, 200, 200)))
        dc.Clear()
        
        # 设置文本颜色和字体
        dc.SetTextForeground(wx.Colour(0, 0, 255))
        dc.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        # 绘制文本
        text = f"Count: {self.count}"
        text_width, text_height = dc.GetTextExtent(text)
        x = (self.GetSize().width - text_width) // 2
        y = (self.GetSize().height - text_height) // 2
        dc.DrawText(text, x, y)
    
    def increment_count(self):
        """增加计数"""
        self.count += 1
        self.Refresh()  # 触发重绘

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Custom Component Example", size=(400, 300))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建垂直盒子布局
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 创建自定义组件
        self.custom_panel = CustomPanel(self.panel)
        self.vbox.Add(self.custom_panel, 0, wx.ALL | wx.CENTER, 20)
        
        # 创建按钮
        self.button = wx.Button(self.panel, label="Increment Count")
        self.vbox.Add(self.button, 0, wx.ALL | wx.CENTER, 10)
        
        # 绑定按钮点击事件
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
        
        # 设置面板的布局
        self.panel.SetSizer(self.vbox)
        
        # 显示窗口
        self.Show()
    
    def on_button_click(self, event):
        """按钮点击事件处理函数"""
        self.custom_panel.increment_count()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
```

### 多线程

wxPython中的GUI操作必须在主线程中进行，对于耗时操作，应该使用多线程。

```python
import wx
import time
import threading

class WorkerThread(threading.Thread):
    """工作线程"""
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.daemon = True  # 设置为守护线程
    
    def run(self):
        """线程运行函数"""
        for i in range(101):
            time.sleep(0.05)
            # 使用wx.CallAfter在主线程中更新UI
            wx.CallAfter(self.parent.update_progress, i)
        # 使用wx.CallAfter在主线程中通知任务完成
        wx.CallAfter(self.parent.task_finished)

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Multi-threading Example", size=(400, 300))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建垂直盒子布局
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 创建进度条
        self.progress_bar = wx.Gauge(self.panel, range=100, size=(300, 20))
        self.vbox.Add(self.progress_bar, 0, wx.ALL | wx.CENTER, 20)
        
        # 创建状态标签
        self.status_label = wx.StaticText(self.panel, label="Ready")
        self.vbox.Add(self.status_label, 0, wx.ALL | wx.CENTER, 10)
        
        # 创建按钮
        self.start_button = wx.Button(self.panel, label="Start")
        self.vbox.Add(self.start_button, 0, wx.ALL | wx.CENTER, 10)
        
        # 绑定按钮点击事件
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start_button_click)
        
        # 设置面板的布局
        self.panel.SetSizer(self.vbox)
        
        # 显示窗口
        self.Show()
    
    def on_start_button_click(self, event):
        """开始按钮点击事件处理函数"""
        # 禁用按钮
        self.start_button.Disable()
        self.status_label.SetLabel("Running...")
        
        # 创建并启动工作线程
        self.worker_thread = WorkerThread(self)
        self.worker_thread.start()
    
    def update_progress(self, progress):
        """更新进度条"""
        self.progress_bar.SetValue(progress)
    
    def task_finished(self):
        """任务完成处理函数"""
        self.status_label.SetLabel("Finished")
        # 启用按钮
        self.start_button.Enable()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
```

## 实际应用示例

### 1. 简单的文本编辑器

```python
import wx

class TextEditorFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Simple Text Editor", size=(800, 600))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建文本控件
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_RICH2)
        
        # 创建垂直盒子布局
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.text_ctrl, 1, wx.ALL | wx.EXPAND, 10)
        
        # 设置面板的布局
        self.panel.SetSizer(self.vbox)
        
        # 创建菜单栏
        menubar = wx.MenuBar()
        
        # 创建文件菜单
        file_menu = wx.Menu()
        
        # 创建打开菜单项
        open_menu_item = file_menu.Append(wx.ID_OPEN, "&Open	Ctrl+O", "Open a file")
        self.Bind(wx.EVT_MENU, self.on_open, open_menu_item)
        
        # 创建保存菜单项
        save_menu_item = file_menu.Append(wx.ID_SAVE, "&Save	Ctrl+S", "Save a file")
        self.Bind(wx.EVT_MENU, self.on_save, save_menu_item)
        
        # 创建另存为菜单项
        save_as_menu_item = file_menu.Append(wx.ID_SAVEAS, "&Save As	Ctrl+Shift+S", "Save file as")
        self.Bind(wx.EVT_MENU, self.on_save_as, save_as_menu_item)
        
        # 创建分隔线
        file_menu.AppendSeparator()
        
        # 创建退出菜单项
        exit_menu_item = file_menu.Append(wx.ID_EXIT, "&Exit	Ctrl+Q", "Exit application")
        self.Bind(wx.EVT_MENU, self.on_exit, exit_menu_item)
        
        # 将文件菜单添加到菜单栏
        menubar.Append(file_menu, "&File")
        
        # 设置菜单栏
        self.SetMenuBar(menubar)
        
        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("Ready")
        
        # 当前文件路径
        self.current_file = None
        
        # 显示窗口
        self.Show()
    
    def on_open(self, event):
        """打开文件"""
        with wx.FileDialog(self, "Open File", wildcard="Text Files (*.txt)|*.txt|All Files (*.*)|*.*",
                          style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            # 获取选中的文件路径
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, "r") as f:
                    content = f.read()
                self.text_ctrl.SetValue(content)
                self.current_file = pathname
                self.SetTitle(f"Simple Text Editor - {pathname}")
                self.SetStatusText(f"Opened: {pathname}")
            except Exception as e:
                wx.MessageBox(f"Failed to open file: {e}", "Error", wx.OK | wx.ICON_ERROR)
    
    def on_save(self, event):
        """保存文件"""
        if self.current_file:
            try:
                content = self.text_ctrl.GetValue()
                with open(self.current_file, "w") as f:
                    f.write(content)
                self.SetStatusText(f"Saved: {self.current_file}")
            except Exception as e:
                wx.MessageBox(f"Failed to save file: {e}", "Error", wx.OK | wx.ICON_ERROR)
        else:
            self.on_save_as(event)
    
    def on_save_as(self, event):
        """另存为文件"""
        with wx.FileDialog(self, "Save File As", wildcard="Text Files (*.txt)|*.txt|All Files (*.*)|*.*",
                          style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            # 获取选中的文件路径
            pathname = fileDialog.GetPath()
            try:
                content = self.text_ctrl.GetValue()
                with open(pathname, "w") as f:
                    f.write(content)
                self.current_file = pathname
                self.SetTitle(f"Simple Text Editor - {pathname}")
                self.SetStatusText(f"Saved: {pathname}")
            except Exception as e:
                wx.MessageBox(f"Failed to save file: {e}", "Error", wx.OK | wx.ICON_ERROR)
    
    def on_exit(self, event):
        """退出应用程序"""
        self.Close(True)
    
    def Close(self, force=False):
        """关闭窗口"""
        # 检查是否有未保存的更改
        if not force and self.text_ctrl.IsModified():
            result = wx.MessageBox("Do you want to save changes?", "Save Changes", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
            if result == wx.CANCEL:
                return False
            elif result == wx.YES:
                self.on_save(None)
        
        return super().Close(force)

if __name__ == "__main__":
    app = wx.App()
    frame = TextEditorFrame()
    app.MainLoop()
```

### 2. 简单的计算器

```python
import wx

class CalculatorFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Calculator", size=(300, 400))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建垂直盒子布局
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 创建显示文本控件
        self.display = wx.TextCtrl(self.panel, style=wx.TE_RIGHT | wx.TE_READONLY)
        self.display.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.vbox.Add(self.display, 0, wx.ALL | wx.EXPAND, 10)
        
        # 创建按钮网格
        button_grid = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "CE", "DEL", ""]
        ]
        
        # 创建网格布局
        self.gridsizer = wx.GridSizer(rows=5, cols=4, hgap=5, vgap=5)
        
        # 添加按钮
        for row in button_grid:
            for button_text in row:
                if button_text:
                    button = wx.Button(self.panel, label=button_text)
                    button.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
                    button.Bind(wx.EVT_BUTTON, lambda event, text=button_text: self.on_button_click(event, text))
                    self.gridsizer.Add(button, 0, wx.EXPAND)
        
        self.vbox.Add(self.gridsizer, 1, wx.ALL | wx.EXPAND, 10)
        
        # 设置面板的布局
        self.panel.SetSizer(self.vbox)
        
        # 显示窗口
        self.Show()
    
    def on_button_click(self, event, button_text):
        """按钮点击事件处理函数"""
        current_text = self.display.GetValue()
        
        if button_text == "C":  # 清除所有
            self.display.SetValue("")
        elif button_text == "CE":  # 清除当前输入
            self.display.SetValue("")
        elif button_text == "DEL":  # 删除最后一个字符
            self.display.SetValue(current_text[:-1])
        elif button_text == "=":  # 计算结果
            try:
                result = eval(current_text)
                self.display.SetValue(str(result))
            except Exception:
                self.display.SetValue("Error")
        else:  # 数字和运算符
            self.display.SetValue(current_text + button_text)

if __name__ == "__main__":
    app = wx.App()
    frame = CalculatorFrame()
    app.MainLoop()
```

### 3. 简单的待办事项应用

```python
import wx

class TodoAppFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Todo List", size=(500, 400))
        
        # 创建面板
        self.panel = wx.Panel(self)
        
        # 创建垂直盒子布局
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 创建输入区域
        input_hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.todo_input = wx.TextCtrl(self.panel, placeholder="Enter a new todo item")
        input_hbox.Add(self.todo_input, 1, wx.ALL | wx.EXPAND, 10)
        
        add_button = wx.Button(self.panel, label="Add")
        add_button.Bind(wx.EVT_BUTTON, self.on_add_button_click)
        input_hbox.Add(add_button, 0, wx.ALL, 10)
        
        self.vbox.Add(input_hbox, 0, wx.EXPAND)
        
        # 创建待办事项列表
        self.todo_list = wx.ListBox(self.panel, style=wx.LB_EXTENDED)
        self.vbox.Add(self.todo_list, 1, wx.ALL | wx.EXPAND, 10)
        
        # 创建操作按钮区域
        button_hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        delete_button = wx.Button(self.panel, label="Delete Selected")
        delete_button.Bind(wx.EVT_BUTTON, self.on_delete_button_click)
        button_hbox.Add(delete_button, 0, wx.ALL, 10)
        
        clear_button = wx.Button(self.panel, label="Clear All")
        clear_button.Bind(wx.EVT_BUTTON, self.on_clear_button_click)
        button_hbox.Add(clear_button, 0, wx.ALL, 10)
        
        self.vbox.Add(button_hbox, 0, wx.EXPAND)
        
        # 设置面板的布局
        self.panel.SetSizer(self.vbox)
        
        # 绑定回车键
        self.todo_input.Bind(wx.EVT_TEXT_ENTER, self.on_add_button_click)
        
        # 显示窗口
        self.Show()
    
    def on_add_button_click(self, event):
        """添加待办事项"""
        todo_text = self.todo_input.GetValue().strip()
        if todo_text:
            self.todo_list.Append(todo_text)
            self.todo_input.Clear()
        else:
            wx.MessageBox("Please enter a todo item.", "Warning", wx.OK | wx.ICON_WARNING)
    
    def on_delete_button_click(self, event):
        """删除选中的待办事项"""
        selected_indices = self.todo_list.GetSelections()
        if not selected_indices:
            wx.MessageBox("Please select a todo item to delete.", "Warning", wx.OK | wx.ICON_WARNING)
            return
        
        # 从后往前删除，避免索引变化导致错误
        for index in reversed(selected_indices):
            self.todo_list.Delete(index)
    
    def on_clear_button_click(self, event):
        """清除所有待办事项"""
        if self.todo_list.GetCount() == 0:
            wx.MessageBox("No todo items to clear.", "Information", wx.OK | wx.ICON_INFORMATION)
            return
        
        result = wx.MessageBox("Are you sure you want to clear all todo items?", "Confirmation", wx.YES_NO | wx.ICON_QUESTION)
        if result == wx.YES:
            self.todo_list.Clear()

if __name__ == "__main__":
    app = wx.App()
    frame = TodoAppFrame()
    app.MainLoop()
```

## 最佳实践

### 1. 使用面向对象编程

对于复杂的GUI应用程序，建议使用面向对象编程，将界面和逻辑分离，提高代码的可维护性和可扩展性。

### 2. 使用布局管理器

应该使用布局管理器来管理组件的位置和大小，而不是使用绝对定位，这样可以使界面在不同大小的窗口中都能正常显示。

### 3. 避免在主线程中执行耗时操作

GUI操作必须在主线程中进行，对于耗时操作，应该使用多线程，避免GUI冻结。可以使用`wx.CallAfter`或`wx.PostEvent`在主线程中更新UI。

### 4. 使用事件驱动编程

GUI应用程序采用事件驱动编程模式，需要理解事件循环和回调函数的概念。

### 5. 处理异常

妥善处理可能出现的异常，避免应用程序崩溃，提供友好的错误提示。

### 6. 保持界面简洁

设计简洁、直观的界面，避免过多的组件和复杂的布局，提高用户体验。

## 与其他模块的关系

### wxPython与PyQt5的区别

wxPython和PyQt5都是流行的Python GUI开发库，主要区别包括：
- wxPython基于wxWidgets，而PyQt5基于Qt
- wxPython提供了更原生的外观和感觉，而PyQt5提供了更现代化的UI组件
- wxPython的许可证更宽松（LGPL），而PyQt5使用GPL或商业许可证
- wxPython的API设计更简洁，而PyQt5的API设计更全面

### wxPython与tkinter的区别

wxPython和tkinter都是Python的GUI开发库，主要区别包括：
- wxPython是第三方库，需要额外安装，而tkinter是Python标准库的一部分
- wxPython提供了更丰富的UI组件和功能，而tkinter的功能相对简单
- wxPython的学习曲线较陡，而tkinter的学习曲线较平缓
- wxPython的性能较好，而tkinter的性能相对较差

## 总结

wxPython是一个功能强大的跨平台GUI开发库，基于wxWidgets，提供了丰富的GUI组件和工具。通过学习wxPython，可以创建原生外观的桌面应用程序。

wxPython的主要特点包括：
- 支持多种操作系统（Windows、macOS、Linux）
- 提供了丰富的GUI组件和布局管理器
- 采用事件驱动编程模式
- 支持多线程处理耗时操作
- 适合开发复杂的GUI应用程序

对于需要开发复杂GUI应用程序的用户，wxPython是一个不错的选择。通过结合面向对象编程和事件驱动编程，可以创建出结构清晰、易于维护的GUI应用程序。
