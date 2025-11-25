from .view_base import ViewBase
import numpy as np
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PIL import Image
import numpy as np
from pathlib import Path

class ImageView(ViewBase):
    _supported_backend = ['qt']
    _settings = [
        ]
    _need_compute = False

    def __init__(self, controller=None, parent=None, backend="qt"):
        ViewBase.__init__(self, controller=controller, parent=parent,  backend=backend)
        self._block_auto_refresh_and_notify = False
    
    def _qt_make_layout(self):
        from .myqt import QT
        import pyqtgraph as pg

        self.layout = QT.QVBoxLayout()

        #data = np.random.random(size=(100,100))
        self.plot = pg.ImageItem()#viewBox=None)
        self.graphicsscene = QGraphicsScene()
        self.graphicsview = QGraphicsView()
        self.graphicsview.setScene(self.graphicsscene)
        self.graphicsscene.addItem(self.plot)
        self.layout.addWidget(self.graphicsview)

    def _qt_refresh(self):
        import pyqtgraph as pg

        first_visible_unit_id = self.controller.get_visible_unit_ids()[0]

        imagepath = Path(f'/home/nolanlab/Work/Developing/fromgit/wolf_play/M3_D6_rate_maps/M3D6_C{first_visible_unit_id}.png')
        if imagepath.is_file():
            image = Image.open(imagepath)
            data = np.transpose(np.asarray(image), axes=[1,0,2])

#        print(f"{data=}")

            self.plot.clear()
            self.plot.setImage(data)

        else:
            data = np.random.random(size=(100,100))
            self.plot.clear()
            self.plot.setImage(data)

        
ImageView._gui_help_txt = """
# SpikeRateView View

This view shows firing rate for spikes per `bin_s`.
"""
