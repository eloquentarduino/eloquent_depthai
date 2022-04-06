import cv2
import numpy as np


class DepthPreview:
    """
    Preview depth frames
    """
    def __init__(self, camera):
        """

        :param camera: DepthCamera
        """
        self.camera = camera

    def liveStream(self, escape_key='q', colormap=cv2.COLORMAP_JET):
        """
        Show live stream of frames
        :param colormap:
        :param escape_key:
        :return:
        """
        while True:
            frame = self.camera.getFrame()
            # Normalization for better visualization
            frame = (frame * (255 / self.camera.getMaxDisparity())).astype(np.uint8)

            # Available color maps: https://docs.opencv.org/3.4/d3/d50/group__imgproc__colormap.html
            frame = cv2.applyColorMap(frame, colormap)
            cv2.imshow("disparity", frame)

            if cv2.waitKey(1) == ord(escape_key):
                break

    def close(self):
        """
        Close stream
        :return:
        """
        self.camera.close()