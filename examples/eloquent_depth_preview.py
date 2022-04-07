from eloquent_depthai import DepthCamera
from eloquent_depthai.preview import DepthPreview


if __name__ == '__main__':
    camera = DepthCamera()
    preview = DepthPreview(camera)

    preview.liveStream()