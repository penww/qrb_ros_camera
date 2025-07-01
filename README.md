<div align="center">
  <h1>QRB ROS Camera</h1>
  <p align="center">
   <img src="https://s7d1.scene7.com/is/image/dmqualcommprod/rb3gen2-dev-kits-hero-7" alt="Qualcomm QRB ROS" title="Qualcomm QRB ROS" />
      
  </p>
  <p>ROS wrapper for camera on Qualcomm robotics platforms.</p>
  
  <a href="https://ubuntu.com/download/qualcomm-iot" target="_blank"><img src="https://img.shields.io/badge/Qualcomm%20Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Qualcomm Ubuntu"></a>
  <a href="https://docs.ros.org/en/jazzy/" target="_blank"><img src="https://img.shields.io/badge/ROS%20Jazzy-1c428a?style=for-the-badge&logo=ros&logoColor=white" alt="Jazzy"></a>
  
</div>
<br>

<div align="center">

<a href="https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit" target="_blank"><img src="https://img.shields.io/badge/RB3%20gen%202%20Vision%20Kit-2a2aea?style=for-the-badge&logo=qualcomm&logoColor=white" alt="RB3 Gen2 Vision Kit"></a>
<a href="https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit" target="_blank"><img src="https://img.shields.io/badge/RB3%20gen%202%20Lite%20Vision%20Kit-2a2aea?style=for-the-badge&logo=qualcomm&logoColor=white" alt="RB3 Gen2 Vision Lite Kit"></a>


</div>

**QRB ROS Camera** is a ROS package to publish the camera data from Qualcomm camera sensors. It provides:
- Concurrent multiple streams output support
- Composable node support
- Zero copy data transport powered by **QRB ROS Transport**

Check out the [CHANGELOG](CHANGELOG.md) for detailed updates and fixes.

---


## Installation

Add Qualcomm IOT PPA for ubuntu:

```bash
sudo add-apt-repository ppa:ubuntu-qcom-iot/qirp
sudo apt update
```

Install Debian package:

```bash
sudo apt install ros-jazzy-qrb-ros-camera
```

## Usage

### Start the camera node

```bash
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

---

## Build from Source

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

---



## Supported Platforms

This package is designed and tested to be compatible with ROS 2 Humble running on Qualcomm RB3 gen2.

| Hardware                                                     | Software          |
| ------------------------------------------------------------ | ----------------- |
| [Qualcomm RB3 gen2](https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit) | `LE.QCROBOTICS.1.0`, `Canonical Ubuntu Image for RB3 gen2` |

## Contributing

We would love to have you as a part of the QRB ROS community. Whether you are helping us fix bugs, proposing new features, improving our documentation, or spreading the word, please refer to our [contribution guidelines](./CONTRIBUTING.md) and [code of conduct](./CODE_OF_CONDUCT.md).

- Bug report: If you see an error message or encounter failures, please create a [bug report](../../issues)
- Feature Request: If you have an idea or if there is a capability that is missing and would make development easier and more robust, please submit a [feature request](../../issues)

## Authors

* **Tian Ding** - *Initial work* - [dingtian777](https://github.com/dingtian777)
* **Zhanye Lin** - *Second version work* - [zhanlin](https://github.com/quic-zhanlin)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

Project is licensed under the [BSD-3-clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE](./LICENSE) for the full license text.

