# PySide2模块详解

## 模块概述

PySide2是Python的跨平台GUI开发库，基于Qt 5，由Qt公司官方维护。PySide2允许开发者使用Python创建现代、美观的桌面应用程序，支持Windows、macOS和Linux等操作系统。PySide2提供了丰富的GUI组件和工具，适合开发各种复杂程度的桌面应用程序。

## 安装方法

PySide2可以使用pip进行安装：

```bash
pip install PySide2
```

## 基本概念

### 应用程序（QApplication）

`QApplication`是PySide2应用程序的核心，负责管理应用程序的事件循环和资源。每个PySide2应用程序必须有且只有一个`QApplication`实例。

### 窗口（QMainWindow、QWidget、QDialog）

PySide2提供了三种主要的窗口类：
- `QMainWindow`：提供了菜单栏、工具栏、状态栏和中央部件等基本结构，适合作为应用程序的主窗口。
- `QWidget`：是所有用户界面元素的基类，可以作为独立窗口或容器使用。
- `QDialog`：用于创建对话框窗口，提供了标准的对话框布局和按钮。

### 布局管理器（Layout）

布局管理器用于管理部件在容器中的位置和大小，如`QVBoxLayout`、`QHBoxLayout`、`QGridLayout`和`QFormLayout`等。

### 信号与槽（Signal & Slot）

信号与槽是PySide2的核心机制，用于在对象之间进行通信。当一个对象的状态发生变化时，它会发出一个信号，而其他对象可以通过连接到该信号的槽来响应这个变化。

### 部件（Widget）

部件是PySide2应用程序中的基本元素，如按钮、标签、文本框等。PySide2提供了丰富的部件类，如`QPushButton`、`QLabel`、`QLineEdit`、`QTextEdit`等。

## 基本用法

### 创建窗口

#### 使用QMainWindow

```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("My First PySide2 App")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建中央部件
        self.central_widget = QLabel("Hello, PySide2!")
        self.central_widget.setStyleSheet("font-size: 24px; font-weight: bold; color: blue;")
        self.setCentralWidget(self.central_widget)

if __name__ == "__main__":
    # 创建应用程序实例
    app = QApplication(sys.argv)
    
    # 创建窗口实例
    window = MainWindow()
    
    # 显示窗口
    window.show()
    
    # 运行应用程序的事件循环
    sys.exit(app.exec_())
```

#### 使用QWidget

```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("QWidget Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建标签
        self.label = QLabel("Hello, PySide2!", self)
        self.label.setGeometry(50, 50, 300, 200)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold; color: blue;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

### 布局管理

#### 垂直布局（QVBoxLayout）

```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("QVBoxLayout Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        
        # 添加部件
        self.label1 = QLabel("Label 1")
        layout.addWidget(self.label1)
        
        self.button1 = QPushButton("Button 1")
        layout.addWidget(self.button1)
        
        self.label2 = QLabel("Label 2")
        layout.addWidget(self.label2)
        
        self.button2 = QPushButton("Button 2")
        layout.addWidget(self.button2)
        
        # 设置布局
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

#### 水平布局（QHBoxLayout）

```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("QHBoxLayout Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建水平布局
        layout = QHBoxLayout()
        
        # 添加部件
        self.label1 = QLabel("Label 1")
        layout.addWidget(self.label1)
        
        self.button1 = QPushButton("Button 1")
        layout.addWidget(self.button1)
        
        self.label2 = QLabel("Label 2")
        layout.addWidget(self.label2)
        
        self.button2 = QPushButton("Button 2")
        layout.addWidget(self.button2)
        
        # 设置布局
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

#### 网格布局（QGridLayout）

```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("QGridLayout Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建网格布局
        layout = QGridLayout()
        
        # 添加部件
        self.name_label = QLabel("Name:")
        layout.addWidget(self.name_label, 0, 0)
        
        self.name_edit = QLineEdit()
        layout.addWidget(self.name_edit, 0, 1)
        
        self.email_label = QLabel("Email:")
        layout.addWidget(self.email_label, 1, 0)
        
        self.email_edit = QLineEdit()
        layout.addWidget(self.email_edit, 1, 1)
        
        self.submit_button = QPushButton("Submit")
        layout.addWidget(self.submit_button, 2, 0, 1, 2)  # 跨2列
        
        # 设置布局
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

#### 表单布局（QFormLayout）

```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("QFormLayout Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建表单布局
        layout = QFormLayout()
        
        # 添加部件
        self.name_edit = QLineEdit()
        layout.addRow("Name:", self.name_edit)
        
        self.email_edit = QLineEdit()
        layout.addRow("Email:", self.email_edit)
        
        self.age_edit = QLineEdit()
        layout.addRow("Age:", self.age_edit)
        
        self.submit_button = QPushButton("Submit")
        layout.addRow(self.submit_button)
        
        # 设置布局
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

### 信号与槽

```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("Signal & Slot Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        
        # 创建部件
        self.label = QLabel("Hello, PySide2!")
        layout.addWidget(self.label)
        
        self.button = QPushButton("Click Me")
        layout.addWidget(self.button)
        
        # 连接信号与槽
        self.button.clicked.connect(self.on_button_clicked)
        
        # 设置布局
        self.setLayout(layout)
    
    def on_button_clicked(self):
        """按钮点击事件处理函数"""
        self.label.setText("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

### 菜单栏、工具栏和状态栏

```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog, QMessageBox
from PySide2.QtGui import QIcon, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("Menu, Toolbar and Statusbar Example")
        self.setGeometry(100, 100, 600, 400)
        
        # 创建中央部件
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建工具栏
        self.create_tool_bar()
        
        # 创建状态栏
        self.statusBar().showMessage("Ready")
        
        # 当前文件路径
        self.current_file = None
    
    def create_menu_bar(self):
        """创建菜单栏"""
        menu_bar = self.menuBar()
        
        # 创建文件菜单
        file_menu = menu_bar.addMenu("&File")
        
        # 创建打开菜单项
        open_action = QAction("&Open", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.setStatusTip("Open a file")
        open_action.triggered.connect(self.on_open)
        file_menu.addAction(open_action)
        
        # 创建保存菜单项
        save_action = QAction("&Save", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.setStatusTip("Save a file")
        save_action.triggered.connect(self.on_save)
        file_menu.addAction(save_action)
        
        # 创建另存为菜单项
        save_as_action = QAction("Save &As", self)
        save_as_action.setShortcut(QKeySequence.SaveAs)
        save_as_action.setStatusTip("Save file as")
        save_as_action.triggered.connect(self.on_save_as)
        file_menu.addAction(save_as_action)
        
        # 创建分隔线
        file_menu.addSeparator()
        
        # 创建退出菜单项
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.on_exit)
        file_menu.addAction(exit_action)
        
        # 创建编辑菜单
        edit_menu = menu_bar.addMenu("&Edit")
        
        # 创建撤销菜单项
        undo_action = QAction("&Undo", self)
        undo_action.setShortcut(QKeySequence.Undo)
        undo_action.setStatusTip("Undo last action")
        undo_action.triggered.connect(self.text_edit.undo)
        edit_menu.addAction(undo_action)
        
        # 创建重做菜单项
        redo_action = QAction("&Redo", self)
        redo_action.setShortcut(QKeySequence.Redo)
        redo_action.setStatusTip("Redo last action")
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)
    
    def create_tool_bar(self):
        """创建工具栏"""
        tool_bar = self.addToolBar("Main Toolbar")
        
        # 创建打开工具按钮
        open_action = QAction("Open", self)
        open_action.setStatusTip("Open a file")
        open_action.triggered.connect(self.on_open)
        tool_bar.addAction(open_action)
        
        # 创建保存工具按钮
        save_action = QAction("Save", self)
        save_action.setStatusTip("Save a file")
        save_action.triggered.connect(self.on_save)
        tool_bar.addAction(save_action)
    
    def on_open(self):
        """打开文件"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*.*)")
        if file_path:
            try:
                with open(file_path, "r") as f:
                    content = f.read()
                self.text_edit.setPlainText(content)
                self.current_file = file_path
                self.setWindowTitle(f"Menu, Toolbar and Statusbar Example - {file_path}")
                self.statusBar().showMessage(f"Opened: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")
    
    def on_save(self):
        """保存文件"""
        if self.current_file:
            try:
                content = self.text_edit.toPlainText()
                with open(self.current_file, "w") as f:
                    f.write(content)
                self.statusBar().showMessage(f"Saved: {self.current_file}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
        else:
            self.on_save_as()
    
    def on_save_as(self):
        """另存为文件"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*.*)")
        if file_path:
            try:
                content = self.text_edit.toPlainText()
                with open(file_path, "w") as f:
                    f.write(content)
                self.current_file = file_path
                self.setWindowTitle(f"Menu, Toolbar and Statusbar Example - {file_path}")
                self.statusBar().showMessage(f"Saved: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
    
    def on_exit(self):
        """退出应用程序"""
        self.close()
    
    def closeEvent(self, event):
        """关闭窗口事件处理函数"""
        if self.text_edit.document().isModified():
            result = QMessageBox.question(self, "Save Changes", "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if result == QMessageBox.Yes:
                self.on_save()
                event.accept()
            elif result == QMessageBox.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

## 高级用法

### 对话框

PySide2提供了多种对话框，用于与用户进行交互。

```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QFileDialog, QInputDialog

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("Dialog Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        
        # 创建按钮
        self.info_button = QPushButton("Show Information Dialog")
        layout.addWidget(self.info_button)
        self.info_button.clicked.connect(self.on_info_button_clicked)
        
        self.warning_button = QPushButton("Show Warning Dialog")
        layout.addWidget(self.warning_button)
        self.warning_button.clicked.connect(self.on_warning_button_clicked)
        
        self.error_button = QPushButton("Show Error Dialog")
        layout.addWidget(self.error_button)
        self.error_button.clicked.connect(self.on_error_button_clicked)
        
        self.question_button = QPushButton("Show Question Dialog")
        layout.addWidget(self.question_button)
        self.question_button.clicked.connect(self.on_question_button_clicked)
        
        self.input_button = QPushButton("Show Input Dialog")
        layout.addWidget(self.input_button)
        self.input_button.clicked.connect(self.on_input_button_clicked)
        
        self.file_button = QPushButton("Show File Dialog")
        layout.addWidget(self.file_button)
        self.file_button.clicked.connect(self.on_file_button_clicked)
        
        # 设置布局
        self.setLayout(layout)
    
    def on_info_button_clicked(self):
        """显示信息对话框"""
        QMessageBox.information(self, "Information", "This is an information message.")
    
    def on_warning_button_clicked(self):
        """显示警告对话框"""
        QMessageBox.warning(self, "Warning", "This is a warning message.")
    
    def on_error_button_clicked(self):
        """显示错误对话框"""
        QMessageBox.critical(self, "Error", "This is an error message.")
    
    def on_question_button_clicked(self):
        """显示问题对话框"""
        result = QMessageBox.question(self, "Question", "Do you want to continue?",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if result == QMessageBox.Yes:
            print("Yes clicked")
        elif result == QMessageBox.No:
            print("No clicked")
        else:
            print("Cancel clicked")
    
    def on_input_button_clicked(self):
        """显示输入对话框"""
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok:
            print(f"Name: {text}")
    
    def on_file_button_clicked(self):
        """显示文件对话框"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*.*)")
        if file_path:
            print(f"Selected file: {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

### 自定义部件

PySide2允许开发者创建自定义部件，继承自现有的部件类。

```python
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide2.QtGui import QPainter, QColor, QFont
from PySide2.QtCore import Qt

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置部件的大小
        self.setFixedSize(200, 100)
        
        # 初始化计数
        self.count = 0
    
    def paintEvent(self, event):
        """绘制事件处理函数"""
        painter = QPainter(self)
        
        # 设置背景颜色
        painter.fillRect(self.rect(), QColor(200, 200, 200))
        
        # 设置文本颜色和字体
        painter.setPen(QColor(0, 0, 255))
        painter.setFont(QFont("Arial", 16, QFont.Bold))
        
        # 绘制文本
        text = f"Count: {self.count}"
        text_rect = painter.boundingRect(self.rect(), Qt.AlignCenter, text)
        painter.drawText(text_rect, Qt.AlignCenter, text)
    
    def increment_count(self):
        """增加计数"""
        self.count += 1
        self.update()  # 触发重绘

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("Custom Widget Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        
        # 创建自定义部件
        self.custom_widget = CustomWidget()
        layout.addWidget(self.custom_widget, alignment=Qt.AlignCenter)
        
        # 创建按钮
        self.button = QPushButton("Increment Count")
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        
        # 连接信号与槽
        self.button.clicked.connect(self.custom_widget.increment_count)
        
        # 设置布局
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

### 多线程

PySide2中的GUI操作必须在主线程中进行，对于耗时操作，应该使用多线程。可以使用`QThread`或Python的`threading`模块。

```python
import sys
import time
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton, QLabel
from PySide2.QtCore import QThread, Signal

class WorkerThread(QThread):
    """工作线程"""
    progress_updated = Signal(int)  # 进度更新信号
    finished = Signal()  # 完成信号
    
    def run(self):
        """线程运行函数"""
        for i in range(101):
            time.sleep(0.05)
            self.progress_updated.emit(i)
        self.finished.emit()

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("Multi-threading Example")
        self.setGeometry(100, 100, 400, 300)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        
        # 创建进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        layout.addWidget(self.progress_bar)
        
        # 创建状态标签
        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
        
        # 创建按钮
        self.start_button = QPushButton("Start")
        layout.addWidget(self.start_button)
        
        # 连接信号与槽
        self.start_button.clicked.connect(self.on_start_button_clicked)
        
        # 设置布局
        self.setLayout(layout)
        
        # 创建工作线程
        self.worker_thread = WorkerThread()
        self.worker_thread.progress_updated.connect(self.update_progress)
        self.worker_thread.finished.connect(self.on_task_finished)
    
    def on_start_button_clicked(self):
        """开始按钮点击事件处理函数"""
        if not self.worker_thread.isRunning():
            # 禁用按钮
            self.start_button.setEnabled(False)
            self.status_label.setText("Running...")
            
            # 启动工作线程
            self.worker_thread.start()
    
    def update_progress(self, progress):
        """更新进度条"""
        self.progress_bar.setValue(progress)
    
    def on_task_finished(self):
        """任务完成处理函数"""
        self.status_label.setText("Finished")
        # 启用按钮
        self.start_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
```

## 实际应用示例

### 1. 简单的文本编辑器

```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog, QMessageBox
from PySide2.QtGui import QKeySequence

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("Simple Text Editor")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建中央部件
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建状态栏
        self.statusBar().showMessage("Ready")
        
        # 当前文件路径
        self.current_file = None
    
    def create_menu_bar(self):
        """创建菜单栏"""
        menu_bar = self.menuBar()
        
        # 创建文件菜单
        file_menu = menu_bar.addMenu("&File")
        
        # 创建打开菜单项
        open_action = QAction("&Open", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.setStatusTip("Open a file")
        open_action.triggered.connect(self.on_open)
        file_menu.addAction(open_action)
        
        # 创建保存菜单项
        save_action = QAction("&Save", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.setStatusTip("Save a file")
        save_action.triggered.connect(self.on_save)
        file_menu.addAction(save_action)
        
        # 创建另存为菜单项
        save_as_action = QAction("Save &As", self)
        save_as_action.setShortcut(QKeySequence.SaveAs)
        save_as_action.setStatusTip("Save file as")
        save_as_action.triggered.connect(self.on_save_as)
        file_menu.addAction(save_as_action)
        
        # 创建分隔线
        file_menu.addSeparator()
        
        # 创建退出菜单项
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.on_exit)
        file_menu.addAction(exit_action)
    
    def on_open(self):
        """打开文件"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*.*)")
        if file_path:
            try:
                with open(file_path, "r") as f:
                    content = f.read()
                self.text_edit.setPlainText(content)
                self.current_file = file_path
                self.setWindowTitle(f"Simple Text Editor - {file_path}")
                self.statusBar().showMessage(f"Opened: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")
    
    def on_save(self):
        """保存文件"""
        if self.current_file:
            try:
                content = self.text_edit.toPlainText()
                with open(self.current_file, "w") as f:
                    f.write(content)
                self.statusBar().showMessage(f"Saved: {self.current_file}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
        else:
            self.on_save_as()
    
    def on_save_as(self):
        """另存为文件"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*.*)")
        if file_path:
            try:
                content = self.text_edit.toPlainText()
                with open(file_path, "w") as f:
                    f.write(content)
                self.current_file = file_path
                self.setWindowTitle(f"Simple Text Editor - {file_path}")
                self.statusBar().showMessage(f"Saved: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
    
    def on_exit(self):
        """退出应用程序"""
        self.close()
    
    def closeEvent(self, event):
        """关闭窗口事件处理函数"""
        if self.text_edit.document().isModified():
            result = QMessageBox.question(self, "Save Changes", "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if result == QMessageBox.Yes:
                self.on_save()
                event.accept()
            elif result == QMessageBox.No:
                event.accept()
            else:
                event.ignore()
        else:
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
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PySide2.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        
        # 创建网格布局
        layout = QGridLayout()
        
        # 创建显示文本框
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.display, 0, 0, 1, 4)
        
        # 创建按钮网格
        button_grid = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "CE", "DEL", ""]
        ]
        
        # 添加按钮
        for row, button_row in enumerate(button_grid, 1):
            for col, button_text in enumerate(button_row):
                if button_text:
                    button = QPushButton(button_text)
                    button.setStyleSheet("font-size: 16px;")
                    button.clicked.connect(lambda checked, text=button_text: self.on_button_clicked(text))
                    layout.addWidget(button, row, col)
        
        # 设置布局
        self.setLayout(layout)
    
    def on_button_clicked(self, button_text):
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
                result = eval(current_text)
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
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox
from PySide2.QtGui import QKeySequence
from PySide2.QtCore import Qt

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.setWindowTitle("Todo List")
        self.setGeometry(100, 100, 500, 400)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout(central_widget)
        
        # 创建输入区域
        input_layout = QHBoxLayout()
        
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Enter a new todo item")
        input_layout.addWidget(self.todo_input, 1)
        
        self.add_button = QPushButton("Add")
        input_layout.addWidget(self.add_button)
        
        layout.addLayout(input_layout)
        
        # 创建待办事项列表
        self.todo_list = QListWidget()
        layout.addWidget(self.todo_list, 1)
        
        # 创建操作按钮区域
        button_layout = QHBoxLayout()
        
        self.delete_button = QPushButton("Delete Selected")
        button_layout.addWidget(self.delete_button)
        
        self.clear_button = QPushButton("Clear All")
        button_layout.addWidget(self.clear_button)
        
        layout.addLayout(button_layout)
        
        # 连接信号与槽
        self.add_button.clicked.connect(self.on_add_button_clicked)
        self.todo_input.returnPressed.connect(self.on_add_button_clicked)
        self.delete_button.clicked.connect(self.on_delete_button_clicked)
        self.clear_button.clicked.connect(self.on_clear_button_clicked)

    def on_add_button_clicked(self):
        """添加待办事项"""
        todo_text = self.todo_input.text().strip()
        if todo_text:
            self.todo_list.addItem(todo_text)
            self.todo_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a todo item.")

    def on_delete_button_clicked(self):
        """删除选中的待办事项"""
        selected_items = self.todo_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "Please select a todo item to delete.")
            return
        
        for item in selected_items:
            self.todo_list.takeItem(self.todo_list.row(item))

    def on_clear_button_clicked(self):
        """清除所有待办事项"""
        if self.todo_list.count() == 0:
            QMessageBox.information(self, "Information", "No todo items to clear.")
            return
        
        result = QMessageBox.question(self, "Confirmation", "Are you sure you want to clear all todo items?",
                                     QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.todo_list.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())
```

## 最佳实践

### 1. 使用面向对象编程

对于复杂的GUI应用程序，建议使用面向对象编程，将界面和逻辑分离，提高代码的可维护性和可扩展性。

### 2. 使用布局管理器

应该使用布局管理器来管理部件的位置和大小，而不是使用绝对定位，这样可以使界面在不同大小的窗口中都能正常显示。

### 3. 避免在主线程中执行耗时操作

GUI操作必须在主线程中进行，对于耗时操作，应该使用多线程，避免GUI冻结。可以使用`QThread`或Python的`threading`模块，并使用信号与槽在主线程中更新UI。

### 4. 使用信号与槽进行通信

信号与槽是PySide2的核心机制，用于在对象之间进行通信，应该充分利用这一机制，避免直接调用对象的方法。

### 5. 处理异常

妥善处理可能出现的异常，避免应用程序崩溃，提供友好的错误提示。

### 6. 保持界面简洁

设计简洁、直观的界面，避免过多的组件和复杂的布局，提高用户体验。

### 7. 使用样式表

可以使用样式表（Style Sheet）来美化界面，样式表的语法类似于CSS。

```python
# 示例：设置按钮样式
button.setStyleSheet(""".QPushButton {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    border-radius: 4px;
}

.QPushButton:hover {
    background-color: #45a049;
}

.QPushButton:pressed {
    background-color: #3e8e41;
}
""")
```

## 与其他模块的关系

### PySide2与PyQt5的区别

PySide2和PyQt5都是基于Qt的Python GUI开发库，主要区别包括：
- 许可证：PySide2使用LGPL许可证，而PyQt5使用GPL或商业许可证
- 维护者：PySide2由Qt公司官方维护，而PyQt5由Riverbank Computing维护
- API：两者的API非常相似，但存在一些细微差别

### PySide2与wxPython的区别

PySide2和wxPython都是流行的Python GUI开发库，主要区别包括：
- 底层库：PySide2基于Qt，而wxPython基于wxWidgets
- 外观：PySide2提供了更现代化的UI组件，而wxPython提供了更原生的外观和感觉
- 学习曲线：PySide2的学习曲线较陡，而wxPython的学习曲线相对平缓
- 功能：PySide2提供了更多的现代化功能，如Qt Quick、Qt WebEngine等

## 总结

PySide2是一个功能强大的跨平台GUI开发库，基于Qt，由Qt公司官方维护。通过学习PySide2，可以创建现代、美观的桌面应用程序。

PySide2的主要特点包括：
- 支持多种操作系统（Windows、macOS、Linux）
- 提供了丰富的GUI组件和布局管理器
- 采用信号与槽机制进行对象间通信
- 支持多线程处理耗时操作
- 提供了现代化的UI组件和功能
- 使用LGPL许可证，适合商业和非商业项目

对于需要开发现代、复杂GUI应用程序的用户，PySide2是一个不错的选择。通过结合面向对象编程和信号与槽机制，可以创建出结构清晰、易于维护的GUI应用程序。
