# Eloquent DepthAI

An wrapper around [depthai](https://docs.luxonis.com/en/latest/) Python package focused on ease of use.


## Example code

To preview a realtime stream of the disparity camera:

```python
from eloquent_depthai import DepthCamera
from eloquent_depthai.preview import DepthPreview


if __name__ == '__main__':
    camera = DepthCamera()
    preview = DepthPreview(camera)

    preview.liveStream()
```