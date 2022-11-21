
from PySide6 import QtWidgets
from wgpu.gui.qt import WgpuWidget
import wgpu.backends.rs  # noqa: F401, Select Rust backend

from triangle import main

class WgpuBottomLeftView(QtWidgets.QWidget):
    def __init__(self, annotation_page = None):
        super().__init__(annotation_page)
        layout = QtWidgets.QHBoxLayout()
        self.wgpu_bottom_left_view = WgpuWidget()

        layout.addWidget(self.wgpu_bottom_left_view)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        
        main(self.wgpu_bottom_left_view)