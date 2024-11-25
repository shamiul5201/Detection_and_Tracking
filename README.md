# Object Detection and Tracking

https://github.com/user-attachments/assets/c19cb502-29cb-44ac-9b8b-e66100c254a2

This project focuses on detecting and tracking a football in a 39-second video using four OpenCV tracking algorithms. It serves as an exploration of object detection and tracking techniques and an evaluation of tracker performance.

### Objective
The primary objective was to track a football in a video clip using the following OpenCV trackers:
- **BOOSTING**
- **MIL**
- **KCF**
- **TLD**

### Methodology
- **Initial Selection**:
The football was manually selected in the first frame of the video using the cv2.selectROI function:
```python
bbox = cv2.selectROI(frame, False)
```

- **Set Up Trackers**:
Four trackers were implemented, each processing the tracking task independently.

- **Output Visualizations**:
The output was presented as a video split into four sections, with each section showcasing the performance of a tracker alongside its name and the calculated FPS (frames per second).


### Results
The final video output, football_tracking_all_algorithms.mp4, demonstrates the following observations:

1. The TLD tracker exhibited the most robust performance, maintaining track of the football even during rapid movements.
2. The other trackers occasionally lost track or misidentified the football during the sequence.


### Contribution and Feedback
Suggestions or feedback are always appreciated to refine this project further. 
gmail: shamiulislamnoyon@gmail.com
