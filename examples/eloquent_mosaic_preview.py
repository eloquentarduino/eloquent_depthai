import cv2
import numpy as np
from eloquent_depthai import DepthCamera
from eloquent_depthai.composite import Mosaic


if __name__ == '__main__':
    camera = DepthCamera()
    mosaic = Mosaic(camera, rows=2, cols=3, delay_ms=100)

    mosaic_frame = mosaic.get()
    mosaic_frame = (mosaic_frame * (255 / camera.getMaxDisparity())).astype(np.uint8)
    jet = cv2.applyColorMap(mosaic_frame, cv2.COLORMAP_JET)
    cv2.imwrite("examples/mosaic.png", jet)
