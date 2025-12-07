# PyQt5模块详解

## 模块概述

PyQt5是Qt5应用框架的Python绑定，是一个功能强大的跨平台GUI开发库。它提供了丰富的GUI组件和工具，支持多种操作系统（Windows、macOS、Linux），并允许开发者创建现代化、交互式的桌面应用程序。PyQt5由Riverbank Computing开发，基于C++编写的Qt5库，提供了与Qt5几乎完全一致的API。

## 安装方法

PyQt5是第三方库，需要使用pip进行安装：

```bash
pip install PyQt5
```

如果需要开发工具（如Qt Designer），可以安装PyQt5-tools：

```bash
pip install PyQt5-tools
```

## 基本概念

### 应用程序（Application）

`QApplication`是PyQt5应用程序的核心，负责管理应用程序的事件循环和资源。每个PyQt5应用程序必须有且只有一个`QApplication`实例。

### 窗口（Window）

`QMainWindow`是PyQt5应用程序的主窗口，提供了菜单栏、工具栏、状态栏和中央部件等基本结构。

### 组件（Widget）

组件是PyQt5应用程序中的基本元素，如按钮、标签、文本框等。所有组件都继承自`QWidget`类。

### 布局（Layout）

布局管理器用于管理组件在窗口中的位置和大小，如`QVBoxLayout`、`QHBoxLayout`、`QGridLayout`等。

### 信号与槽（Signals and Slots）

信号与槽是PyQt5的核心机制，用于组件之间的通信。当组件发生特定事件时，会发射一个信号，槽是接收并处理信号的函数。

## 基本用法

### 创建窗口

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 400, 300)  # (x, y, width, height)
        
        # 创建标签
        self.label = QLabel("Hello, PyQt5!", self)
        self.label.move(150, 100)  # 设置标签位置

if __name__ == "__main__":
    # 创建应用程序实例
    app = QApplication(sys.argv)
    
    # 创建窗口实例
    window = MyWindow()
    
    # 显示窗口
    window.show()
    
    # 运行应用程序的事件循环
    sys.exit(app.exec_())
```

### 布局管理

PyQt5提供了多种布局管理器，用于管理组件在窗口中的位置和大小。

#### 垂直布局（QVBoxLayout）

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Vertical Layout Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout(central_widget)
        
        # 添加组件
        layout.addWidget(QLabel("Label 1", self))
        layout.addWidget(QPushButton("Button 1", self))
        layout.addWidget(QLabel("Label 2", self))
        layout.addWidget(QPushButton("Button 2", self))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

#### 水平布局（QHBoxLayout）

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Horizontal Layout Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建水平布局
        layout = QHBoxLayout(central_widget)
        
        # 添加组件
        layout.addWidget(QLabel("Label 1", self))
        layout.addWidget(QPushButton("Button 1", self))
        layout.addWidget(QLabel("Label 2", self))
        layout.addWidget(QPushButton("Button 2", self))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

#### 网格布局（QGridLayout）

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Grid Layout Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建网格布局
        layout = QGridLayout(central_widget)
        
        # 添加组件
        layout.addWidget(QLabel("Name:", self), 0, 0)  # 第0行第0列
        layout.addWidget(QLineEdit(self), 0, 1)  # 第0行第1列
        layout.addWidget(QLabel("Email:", self), 1, 0)  # 第1行第0列
        layout.addWidget(QLineEdit(self), 1, 1)  # 第1行第1列
        layout.addWidget(QPushButton("Submit", self), 2, 0, 1, 2)  # 第2行，跨两列

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

### 信号与槽

信号与槽是PyQt5的核心机制，用于组件之间的通信。

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Signals and Slots Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout(central_widget)
        
        # 创建标签和按钮
        self.label = QLabel("Hello, PyQt5!", self)
        layout.addWidget(self.label)
        
        self.button = QPushButton("Click Me", self)
        layout.addWidget(self.button)
        
        # 连接信号与槽
        self.button.clicked.connect(self.on_button_clicked)
    
    def on_button_clicked(self):
        """按钮点击事件处理函数"""
        self.label.setText("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

### 菜单栏、工具栏和状态栏

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Menu, Toolbar and Statusbar Example")
        self.setGeometry(100, 100, 600, 400)
        
        # 创建菜单栏
        menubar = self.menuBar()
        
        # 创建文件菜单
        file_menu = menubar.addMenu("File")
        
        # 创建打开动作
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Open a file")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        # 创建保存动作
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.setStatusTip("Save a file")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        # 创建退出动作
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 创建编辑菜单
        edit_menu = menubar.addMenu("Edit")
        
        # 创建撤销动作
        undo_action = QAction("Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.setStatusTip("Undo last action")
        edit_menu.addAction(undo_action)
        
        # 创建工具栏
        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        toolbar.addAction(exit_action)
        
        # 创建状态栏
        self.statusBar().showMessage("Ready")
    
    def open_file(self):
        """打开文件"""
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        if file_name:
            self.statusBar().showMessage(f"Opened: {file_name}")
    
    def save_file(self):
        """保存文件"""
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)")
        if file_name:
            self.statusBar().showMessage(f"Saved: {file_name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

## 高级用法

### 对话框

PyQt5提供了多种对话框，用于与用户进行交互。

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox, QFileDialog

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Dialog Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout(central_widget)
        
        # 创建按钮
        button1 = QPushButton("Show Information Dialog", self)
        button1.clicked.connect(self.show_info_dialog)
        layout.addWidget(button1)
        
        button2 = QPushButton("Show Warning Dialog", self)
        button2.clicked.connect(self.show_warning_dialog)
        layout.addWidget(button2)
        
        button3 = QPushButton("Show Error Dialog", self)
        button3.clicked.connect(self.show_error_dialog)
        layout.addWidget(button3)
        
        button4 = QPushButton("Show Question Dialog", self)
        button4.clicked.connect(self.show_question_dialog)
        layout.addWidget(button4)
        
        button5 = QPushButton("Show File Dialog", self)
        button5.clicked.connect(self.show_file_dialog)
        layout.addWidget(button5)
    
    def show_info_dialog(self):
        """显示信息对话框"""
        QMessageBox.information(self, "Information", "This is an information message.")
    
    def show_warning_dialog(self):
        """显示警告对话框"""
        QMessageBox.warning(self, "Warning", "This is a warning message.")
    
    def show_error_dialog(self):
        """显示错误对话框"""
        QMessageBox.critical(self, "Error", "This is an error message.")
    
    def show_question_dialog(self):
        """显示问题对话框"""
        reply = QMessageBox.question(self, "Question", "Do you want to continue?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("Yes clicked")
        else:
            print("No clicked")
    
    def show_file_dialog(self):
        """显示文件对话框"""
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        if file_name:
            print(f"Selected file: {file_name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

### 自定义组件

PyQt5允许开发者创建自定义组件，继承自现有的组件类。

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import QRect, Qt

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 100)
        self.count = 0
    
    def paintEvent(self, event):
        """绘制事件处理函数"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制背景
        painter.setBrush(QColor(200, 200, 200))
        painter.drawRect(self.rect())
        
        # 绘制文本
        painter.setPen(QColor(0, 0, 255))
        painter.setFont(QFont("Arial", 16))
        painter.drawText(self.rect(), Qt.AlignCenter, f"Count: {self.count}")
    
    def increment_count(self):
        """增加计数"""
        self.count += 1
        self.update()  # 触发重绘

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Custom Widget Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout(central_widget)
        
        # 创建自定义组件
        self.custom_widget = CustomWidget(self)
        layout.addWidget(self.custom_widget)
        
        # 创建按钮
        button = QPushButton("Increment Count", self)
        button.clicked.connect(self.custom_widget.increment_count)
        layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

### 多线程

PyQt5中的GUI操作必须在主线程中进行，对于耗时操作，应该使用多线程。

```python
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QProgressBar, QLabel
from PyQt5.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    """工作线程"""
    progress_changed = pyqtSignal(int)  # 进度信号
    finished = pyqtSignal()  # 完成信号
    
    def run(self):
        """线程运行函数"""
        for i in range(101):
            time.sleep(0.05)
            self.progress_changed.emit(i)  # 发射进度信号
        self.finished.emit()  # 发射完成信号

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Multi-threading Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout(central_widget)
        
        # 创建进度条
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)
        
        # 创建标签
        self.status_label = QLabel("Ready", self)
        layout.addWidget(self.status_label)
        
        # 创建按钮
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_task)
        layout.addWidget(self.start_button)
    
    def start_task(self):
        """开始任务"""
        self.start_button.setEnabled(False)
        self.status_label.setText("Running...")
        
        # 创建工作线程
        self.worker_thread = WorkerThread()
        
        # 连接信号与槽
        self.worker_thread.progress_changed.connect(self.update_progress)
        self.worker_thread.finished.connect(self.task_finished)
        
        # 启动线程
        self.worker_thread.start()
    
    def update_progress(self, progress):
        """更新进度条"""
        self.progress_bar.setValue(progress)
    
    def task_finished(self):
        """任务完成"""
        self.status_label.setText("Finished")
        self.start_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

## 实际应用示例

### 1. 简单的文本编辑器

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Simple Text Editor")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建文本编辑区
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        
        # 创建菜单栏
        menubar = self.menuBar()
        
        # 创建文件菜单
        file_menu = menubar.addMenu("File")
        
        # 创建打开动作
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        # 创建保存动作
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        # 创建另存为动作
        save_as_action = QAction("Save As", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)
        
        # 创建退出动作
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 当前文件路径
        self.current_file = None
    
    def open_file(self):
        """打开文件"""
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                with open(file_name, "r") as f:
                    content = f.read()
                self.text_edit.setPlainText(content)
                self.current_file = file_name
                self.setWindowTitle(f"Simple Text Editor - {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")
    
    def save_file(self):
        """保存文件"""
        if self.current_file:
            try:
                content = self.text_edit.toPlainText()
                with open(self.current_file, "w") as f:
                    f.write(content)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
        else:
            self.save_file_as()
    
    def save_file_as(self):
        """另存为文件"""
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            try:
                content = self.text_edit.toPlainText()
                with open(file_name, "w") as f:
                    f.write(content)
                self.current_file = file_name
                self.setWindowTitle(f"Simple Text Editor - {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
    
    def closeEvent(self, event):
        """关闭窗口事件处理函数"""
        if self.text_edit.document().isModified():
            reply = QMessageBox.question(self, "Save Changes", "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.save_file()
            elif reply == QMessageBox.Cancel:
                event.ignore()
                return
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
```

### 2. 简单的计算器

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建网格布局
        layout = QGridLayout(central_widget)
        
        # 创建显示框
        self.display = QLineEdit(self)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.display, 0, 0, 1, 4)  # 第0行，跨4列
        
        # 创建按钮
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("CE", 5, 1), ("DEL", 5, 2), ("", 5, 3)
        ]
        
        for button_text, row, col in buttons:
            if button_text:
                button = QPushButton(button_text, self)
                button.setFixedSize(70, 50)
                button.setStyleSheet("font-size: 16px;")
                button.clicked.connect(lambda checked, text=button_text: self.on_button_click(text))
                layout.addWidget(button, row, col)
    
    def on_button_click(self, button_text):
        """按钮点击事件处理函数"""
        current_text = self.display.text()
        
        if button_text == "C":  # 清除所有
            self.display.clear()
        elif button_text == "CE":  # 清除当前输入
            self.display.clear()
        elif button_text == "DEL":  # 删除最后一个字符
            self.display.setText(current_text[:-1])
        elif button_text == "=":  # 计算结果
            try:
                # 替换除法运算符
                expression = current_text.replace("/", "//")
                result = eval(expression)
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        else:  # 数字和运算符
            self.display.setText(current_text + button_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
```

### 3. 简单的待办事项应用

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Todo List")
        self.setGeometry(100, 100, 500, 400)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout(central_widget)
        
        # 创建输入区域
        input_layout = QHBoxLayout()
        
        self.todo_input = QLineEdit(self)
        self.todo_input.setPlaceholderText("Enter a new todo item")
        self.todo_input.returnPressed.connect(self.add_todo)
        input_layout.addWidget(self.todo_input)
        
        add_button = QPushButton("Add", self)
        add_button.clicked.connect(self.add_todo)
        input_layout.addWidget(add_button)
        
        layout.addLayout(input_layout)
        
        # 创建待办事项列表
        self.todo_list = QListWidget(self)
        self.todo_list.itemDoubleClicked.connect(self.toggle_todo)
        layout.addWidget(self.todo_list)
        
        # 创建操作按钮
        button_layout = QHBoxLayout()
        
        delete_button = QPushButton("Delete Selected", self)
        delete_button.clicked.connect(self.delete_todo)
        button_layout.addWidget(delete_button)
        
        clear_button = QPushButton("Clear All", self)
        clear_button.clicked.connect(self.clear_todos)
        button_layout.addWidget(clear_button)
        
        layout.addLayout(button_layout)
    
    def add_todo(self):
        """添加待办事项"""
        todo_text = self.todo_input.text().strip()
        if todo_text:
            item = QListWidgetItem(todo_text)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.todo_list.addItem(item)
            self.todo_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a todo item.")
    
    def toggle_todo(self, item):
        """切换待办事项状态"""
        current_text = item.text()
        if current_text.startswith("✓ "):
            new_text = current_text[2:]
            item.setText(new_text)
            font = item.font()
            font.setStrikeOut(False)
            item.setFont(font)
        else:
            new_text = f"✓ {current_text}"
            item.setText(new_text)
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)
    
    def delete_todo(self):
        """删除选中的待办事项"""
        selected_items = self.todo_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select a todo item to delete.")
            return
        
        for item in selected_items:
            self.todo_list.takeItem(self.todo_list.row(item))
    
    def clear_todos(self):
        """清除所有待办事项"""
        if self.todo_list.count() == 0:
            QMessageBox.information(self, "Information", "No todo items to clear.")
            return
        
        reply = QMessageBox.question(self, "Confirmation", "Are you sure you want to clear all todo items?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.todo_list.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())
```

## 最佳实践

### 1. 使用面向对象编程

PyQt5应用程序应该使用面向对象编程，将界面和逻辑分离，提高代码的可维护性和可扩展性。

### 2. 使用信号与槽

信号与槽是PyQt5的核心机制，应该充分利用它来处理组件之间的通信，避免直接操作组件。

### 3. 使用布局管理器

应该使用布局管理器来管理组件的位置和大小，而不是使用绝对定位，这样可以使界面在不同大小的窗口中都能正常显示。

### 4. 使用多线程处理耗时操作

GUI操作必须在主线程中进行，对于耗时操作，应该使用多线程，避免GUI冻结。

### 5. 处理异常

应该妥善处理可能出现的异常，避免应用程序崩溃，提供友好的错误提示。

### 6. 使用Qt Designer

Qt Designer是PyQt5的可视化设计工具，可以快速创建界面，提高开发效率。

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 加载UI文件
        loadUi("main_window.ui", self)
        
        # 连接信号与槽
        self.pushButton.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        """按钮点击事件处理函数"""
        self.label.setText("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

## 与其他模块的关系

### PyQt5与PyQt4的区别

PyQt5是PyQt4的升级版，主要区别包括：
- PyQt5基于Qt5，而PyQt4基于Qt4
- PyQt5提供了更现代化的UI组件和API
- PyQt5支持Python 3，而PyQt4支持Python 2和Python 3
- PyQt5的模块结构发生了变化，一些模块被拆分或重组

### PyQt5与PySide2的区别

PySide2是Qt官方提供的Python绑定，与PyQt5的主要区别包括：
- PySide2使用LGPL许可证，而PyQt5使用GPL或商业许可证
- PySide2的API与PyQt5基本兼容，但有一些细微的差别
- PySide2是Qt官方维护的，而PyQt5是第三方维护的

## 总结

PyQt5是一个功能强大的跨平台GUI开发库，基于Qt5应用框架，提供了丰富的GUI组件和工具。通过学习PyQt5，可以创建现代化、交互式的桌面应用程序。

PyQt5的主要特点包括：
- 支持多种操作系统（Windows、macOS、Linux）
- 提供了丰富的GUI组件和布局管理器
- 采用信号与槽机制进行组件通信
- 支持多线程处理耗时操作
- 提供了Qt Designer可视化设计工具
- 适合开发复杂的GUI应用程序

对于需要开发复杂GUI应用程序的用户，PyQt5是一个不错的选择。通过结合面向对象编程和信号与槽机制，可以创建出结构清晰、易于维护的GUI应用程序。
