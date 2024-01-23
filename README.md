# OpenCV-Color-Detector
Detecting the desired color object via webcam using openCV in python

This repository contains a simple Python script that uses OpenCV to perform object tracking based on color. The script captures video from the default camera (usually the webcam) and tracks objects of a specified color (in this case, red) in real-time.

## Prerequisites
- Python 3.x
- OpenCV
- Pillow (PIL)

Install the required dependencies using the following command:

```bash
pip install opencv-python Pillow
```

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/opencv-color-object-tracking.git
```

2. Navigate to the project directory:

3. Run the script:

4. To exit the application, press the 'q' key.

## Description

The script captures video frames from the camera, converts them to the HSV color space, and applies a color mask to isolate the specified color (red). It then identifies the bounding box of the tracked object and draws a rectangle around it in the original frame. The tracking is done in real-time until the user presses the 'q' key to exit.

## Customization

You can customize the script by modifying the following:

- **Color:** Change the `red` variable to the desired BGR color code for tracking.

```python
red = [0, 0, 255]  # BGR color code for red
```

- **Adjustment of color range:** If needed, modify the `get_limits` function in the `utils.py` file to set the lower and upper limits for the color range.

Feel free to explore and customize the code according to your specific requirements.

## Acknowledgments

- The script uses the OpenCV library for computer vision tasks. More information about OpenCV can be found [here](https://opencv.org/).
