<div align="center">
  <h1>QRB ROS Camera</h1>
  <p align="center">
   <img src="https://s7d1.scene7.com/is/image/dmqualcommprod/rb3gen2-dev-kits-hero-7" alt="Qualcomm QRB ROS" title="Qualcomm QRB ROS" />
      
  </p>
  <p>ROS Packages for Cameras on Qualcomm Robotics Platforms</p>
  
  <a href="https://ubuntu.com/download/qualcomm-iot" target="_blank"><img src="https://img.shields.io/badge/Qualcomm%20Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Qualcomm Ubuntu"></a>
  <a href="https://docs.ros.org/en/jazzy/" target="_blank"><img src="https://img.shields.io/badge/ROS%20Jazzy-1c428a?style=for-the-badge&logo=ros&logoColor=white" alt="Jazzy"></a>
  
</div>

---

## 👋 Overview

The [QRB ROS Camera](https://github.com/qualcomm-qrb-ros/qrb_ros_camera) is a ROS package to publish the images from Qualcomm CSI and GMSL cameras. It provides:

- Concurrent multiple streams output support
- Composable ROS node support
- Zero-Copy transport powered by [QRB ROS Transport](https://github.com/qualcomm-qrb-ros/qrb_ros_transport)
- Output NV12 format

#### Supported Targets

<table >
  <col width="120" />
  <col width="120" />
  <col width="200" />
  <tr>
    <th>RB3 Gen2</td>
    <th>RB8</td>
    <th>RB4</td>
  </tr>
  <tr>
    <td><a href="https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit"><img src="https://s7d1.scene7.com/is/image/dmqualcommprod/rb3-gen2-carousel?fmt=webp-alpha&qlt=85" width="160"/></a></td>
    <td><a href="https://www.qualcomm.com/products/internet-of-things/industrial-processors/iq9-series/iq-9075"><img src="https://s7d1.scene7.com/is/image/dmqualcommprod/dragonwing-IQ-9075-EVK?$QC_Responsive$&fmt=png-alpha" width="160"></a></td>
    <td>&nbsp;&nbsp;&nbsp;<a href="https://www.qualcomm.com/dragonwing"><img src="https://s7d1.scene7.com/is/image/dmqualcommprod/iterim-glass-chip?$QC_Responsive$&fmt=png-alpha" width="120"></a>&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <th>which camera in this platform? GMSL/CSI</td>
    <th>RB8</td>
    <th>RB4</td>
  </tr>
</table>

> [!NOTE]
> This project developed and tested based on [Qualcomm® Ubuntu](https://ubuntu.com/download/qualcomm-iot) and [ROS Jazzy](https://docs.ros.org/en/jazzy/index.html). <br>
> For Qualcomm Linux, please to check out [Qualcomm Intelligent Robotics Product SDK](https://docs.qualcomm.com/bundle/publicresource/topics/80-70018-265/introduction_1.html?vproduct=1601111740013072&version=1.4&facet=Qualcomm%20Intelligent%20Robotics%20Product%20(QIRP)%20SDK) documents.

#### Architecture Diagrams



#### Add introduction for all modules, such as qrb_camera

---

## ✨ Installation

Add Qualcomm IOT PPA for Ubuntu:

```bash
sudo add-apt-repository ppa:ubuntu-qcom-iot/qcom-noble-ppa
sudo add-apt-repository ppa:ubuntu-qcom-iot/qirp
sudo apt update
```

Install Debian package:

```bash
sudo apt install ros-jazzy-qrb-ros-camera
```

## 🚀 Usage

### Start the camera node

```bash
source /opt/ros/jazzy/setup.bash
ros2 launch qrb_ros_camera qrb_ros_camera_launch.py
```

What does it do in this commands? open camera 0 , with which resolution? how to configure resolution ?

### Example for how to enable multiple streams

### ROS interfaces

<table>
  <tr>
    <th>Interface</th>
    <th>Name</th>
    <th>Type</th>
    <td>Description</td>
  </tr>
  <tr>
    <td>Publisher</td>
    <td>/cam${camera_id}_${stream_name}</td>
    <td>sensor_msgs/msg/Image</td>
    <td>output image</td>
  </tr>
  <tr>
    <td></td>
    <td>/cam${camera_id}_camera_info</td>
    <td>sensor_msgs/msg/CameraInfo</td>
    <td>camera information</td>
  </tr>
</table>

### ROS parameters

<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Description</td>
    <th>Default Value</td>
  </tr>
  <tr>
    <td>camera_id</td>
    <td>int64</td>
    <td>The camera device ID</td>
    <td>0</td>
  </tr>
  <tr>
    <td>stream_size</td>
    <td>uint64</td>
    <td>Count of camera stream</td>
    <td>1</td>
  </tr>
  <tr>
    <td>stream_name</td>
    <td>string[]</td>
    <td>camera stream names</td>
    <td>stream${camera_id}</td>
  </tr>
  <tr>
    <td>camera_info_path</td>
    <td>string</td>
    <td>Camera metadata file path</td>
    <td>config/camera_info_imx577.yaml</td>
  </tr>
  <tr>
    <td>log_level</td>
    <td>string</td>
    <td>The log level</td>
    <td>DEBUG</td>
  </tr>
</table>

---

## 👨‍💻 Build from Source (Only for Ubuntu)

Install dependencies

```bash
sudo apt install ros-jazzy-qrb-ros-transport-image-type
```

Download source code and build with colcon
```bash
source /opt/ros/jazzy/setup.bash
git clone https://github.com/qualcomm-qrb-ros/qrb_ros_camera.git
colcon build
```

Run and debug

```bash
source install/setup.bash
ros2 launch qrb_ros_camera qrb_ros_camera_launch.py
```

## 🤝 Contributing

We love community contributions! Get started by reading our [CONTRIBUTING.md](CONTRIBUTING.md).<br>
Feel free to create issue for bug report, feature request or any discussion💡.

## ❤️ Contributors

Thanks to all our contributors who have helped make this project better!

<table>
  <tr>
    <td align="center"><a href="https://github.com/dingtian777"><img src="https://avatars.githubusercontent.com/u/154509668?v=4" width="100" height="100" alt="dingtian777"/><br /><sub><b>dingtian777</b></sub></a></td>
    <td align="center"><a href="https://github.com/quic-zhanlin"><img src="https://avatars.githubusercontent.com/u/88314584?v=4" width="100" height="100" alt="quic-zhanlin"/><br /><sub><b>quic-zhanlin</b></sub></a></td>
  </tr>
</table>

## 📜 License

Project is licensed under the [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) License. See [LICENSE](./LICENSE) for the full license text.

