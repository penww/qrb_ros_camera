## Run RealSense D457

### 1. Camera config file

```yaml
/**:
  ros__parameters:
    camera_id: 4
    isp_usecase: 0

    stream_size: 3
    stream_name:
      - stream0
      - stream1
      - stream2

    # Depth
    stream0:
      width:  1280
      height: 720
      fps:    30
      format: mipi16
      bufferlist_id: 1
      camera_info_path: ""

    # Color
    stream1:
      width:  1280
      height: 720
      fps:    30
      format: nv12
      bufferlist_id: 2
      camera_info_path: ""

    # IR
    stream2:
      width:  1280
      height: 720
      fps:    30
      format: mipi8
      bufferlist_id: 3
      camera_info_path: ""
```

### 2. Build and run

```bash
source /opt/ros/jazzy/setup.bash

colcon build
source install/setup.bash

ros2 run qrb_ros_camera camera_node_exe \
    --ros-args \
    --params-file /path/to/config.yaml
```
