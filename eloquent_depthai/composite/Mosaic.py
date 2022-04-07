import numpy as np
from time import sleep, time


class Mosaic:
    """
    Generate a mosaic of images from camera
    """
    def __init__(self, camera, cols, rows=1, delay_ms=100):
        """

        :param camera:
        :param cols:
        :param rows:
        :param delay_ms:
        """
        assert cols > 1, 'cols must be >= 1'
        assert rows > 1, 'rows must be >= 1'

        self.camera = camera
        self.cols = int(cols)
        self.rows = int(rows)
        self.delay = int(delay_ms) / 1000

    @property
    def num_frames(self):
        """
        Get total number of frames
        :return: int
        """
        return self.rows * self.cols

    def get(self):
        """
        Get mosaic
        :return:
        """
        mosaic = None
        last_tick = 0

        for i in range(self.num_frames):
            # blocking
            while time() - last_tick < self.delay:
                sleep(0.01)

            frame = self.camera.getFrame()
            height, width, depth = (list(frame.shape[:3]) + [1])[:3]
            last_tick = time()

            if mosaic is None:
                mosaic = np.zeros((height * self.rows, width * self.cols, depth))

            x = i % self.cols
            y = i // self.cols

            if len(frame.shape) == 2:
                frame = frame.reshape((height, width, 1))

            # mirror vertically on even rows
            if y % 2 == 1:
                x = self.cols - x - 1
                frame = frame[::-1, :, :]

            mosaic[y * height:(y + 1) * height, x * width:(x + 1) * width, :] = frame

        return mosaic
