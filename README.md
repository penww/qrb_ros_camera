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

The QRB ROS Camera is a ROS package to publish the images from Qualcomm CSI cameras. It provides:

- Concurrent multiple streams output support
- Composable ROS node support
- Zero-Copy transport powered by [QRB ROS Transport](https://github.com/qualcomm-qrb-ros/qrb_ros_transport)

Check out the [CHANGELOG](CHANGELOG.md) for detailed updates and fixes.

---

## ✨ Installation

Add Qualcomm IOT PPA for Ubuntu:

```bash
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

### Parameters

#### Avaliable Parameters:

- **camera_id**:
  - The camera device ID
  - Can be set to *0*, *1*, *2*
  - Default value: `0`
 
- **log_level**
  - Log level for ROS node
  - Can be set to *DEBUG*
  - Default value: `DEBUG`

## 🎯 Supported Targets

Here is the list of all supported targets based on [Qualcomm Ubuntu](https://ubuntu.com/download/qualcomm-iot). 

<table>
  <tr>
    <th>RB3 Gen2</td>
    <th>RB8</td>
    <th>RB4</td>
  </tr>
  <tr>
    <td><a href="https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit">
      <img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_600,h_338/https://assets.ubuntu.com/v1/346869e6-QCS6490-bg-solid.png" width="200"/>
    </a></td>
    <td><a><img></a></td>
    <td><a><img></a></td>
  </tr>
</table>

For Qualcomm Linux, check out [Qualcomm Intelligent Robotics Product SDK](https://docs.qualcomm.com/bundle/publicresource/topics/80-70018-265/introduction_1.html?vproduct=1601111740013072&version=1.4&facet=Qualcomm%20Intelligent%20Robotics%20Product%20(QIRP)%20SDK) documents.

---

## 👨‍💻 Build from Source

Install dependencies

```bash
sudo apt install ros-jazzy-qrb-ros-transport-image-type
```

Download source code and build with colcon
```bash
git clone https://github.com/qualcomm-qrb-ros/qrb_ros_camera.git
colcon build
```

Run and debug

```bash
source install/setup.bash
ros2 launch qrb_ros_camera qrb_ros_camera_launch.py
```

## 💪 Contributing

We love community contributions! Get started by reading our [CONTRIBUTING.md](CONTRIBUTING.md).

## ♥️ Contributors

Thanks to all our contributors who have helped make this project better!

<table>
  <tr>
    <td align="center"><a href="https://github.com/dingtian777"><img src="https://avatars.githubusercontent.com/u/154509668?v=4" width="100" height="100" alt="dingtian777"/><br /><sub><b>dingtian777</b></sub></a></td>
    <td align="center"><a href="https://github.com/quic-zhanlin"><img src="https://avatars.githubusercontent.com/u/88314584?v=4" width="100" height="100" alt="quic-zhanlin"/><br /><sub><b>quic-zhanlin</b></sub></a></td>
  </tr>
</table>

## 📃 License

Project is licensed under the [BSD-3-Clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE](./LICENSE) for the full license text.

