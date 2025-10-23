from spikeinterface_gui import run_mainwindow
import spikeinterface.full as si
from PyQt5.QtCore import QTimer
import time


def save_screenshot(win, file_name):
    pixmap = win.grab()
    pixmap.save(file_name)

# NP2 four shank
sorting_analyzer = si.load_sorting_analyzer('/home/nolanlab/Work/Developing/fromgit/spikeinterface-gui/test_np2')

# test waveform view

layout = {'zone5': ['waveform']}
win = run_mainwindow(sorting_analyzer, mode="desktop", start_app=False, curation=True, layout=layout)

time.sleep(0.1)

save_screenshot(win, "screenshots/NP2_waveform_geometry.png")

# select two

win.views['waveform'].controller._visible_unit_ids = [99,103]
win.views['waveform']._refresh()

time.sleep(0.1)

save_screenshot(win, "screenshots/NP2_waveform_geometry_two.png")

