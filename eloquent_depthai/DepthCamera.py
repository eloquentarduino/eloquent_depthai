import depthai


class DepthCamera:
    """
    Get depth images from OAK
    """
    def __init__(self):
        # Create pipeline
        pipeline = depthai.Pipeline()

        # Define sources and outputs
        left = pipeline.create(depthai.node.MonoCamera)
        right = pipeline.create(depthai.node.MonoCamera)
        depth = pipeline.create(depthai.node.StereoDepth)
        xout = pipeline.create(depthai.node.XLinkOut)

        xout.setStreamName("disparity")

        # Properties
        left.setResolution(depthai.MonoCameraProperties.SensorResolution.THE_400_P)
        left.setBoardSocket(depthai.CameraBoardSocket.LEFT)
        right.setResolution(depthai.MonoCameraProperties.SensorResolution.THE_400_P)
        right.setBoardSocket(depthai.CameraBoardSocket.RIGHT)

        self.pipeline = pipeline
        self.left = left
        self.right = right
        self.depth = depth
        self.xout = xout
        self.device = None
        self.queue = None
        self.is_opened = False
        self.is_linked = False
        
    def open(self):
        """
        Open stream
        :return:
        """
        # Linking
        if not self.is_linked:
            self.left.out.link(self.depth.left)
            self.right.out.link(self.depth.right)
            self.depth.disparity.link(self.xout.input)
            self.is_linked = True

        self.device = depthai.Device(self.pipeline)
        self.queue = self.device.getOutputQueue(name="disparity", maxSize=4, blocking=True)
        self.is_opened = True

    def close(self):
        """
        Close stream
        :return:
        """
        self.device.__exit__(None, None, None)
        self.is_opened = False

    def getFrame(self):
        """
        Get frame
        :return:
        """
        if not self.is_opened:
            self.open()

        if self.queue is None:
            return None

        disparity = self.queue.get()

        if disparity is None:
            return None

        return disparity.getFrame()

    def getMaxDisparity(self):
        """

        :return:
        """
        return self.depth.initialConfig.getMaxDisparity()
