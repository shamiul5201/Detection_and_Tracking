# Object Detection and Tracking
#### click the video to see the result
Each tracker had its own method to follow the ball, and I wanted to compare how they worked.

https://github.com/user-attachments/assets/c19cb502-29cb-44ac-9b8b-e66100c254a2

This project is about detecting and tracking a football in a 39-second video. I worked on it to learn how object detection and tracking work. I also wanted to see which tracker algorithm performs best.

### Goal
The goal was to track a football from a video clip using four different trackers from OpenCV:
- **BOOSTING**
- **MIL**
- **KCF**
- **TLD**

### How I Did It
- **Select the Ball**:
At the start of the video, I manually selected the football in the first frame. This line does the job
```python
bbox = cv2.selectROI(frame, False)
```

- **Set Up Trackers**:
I used all four trackers, and each one tracked the ball in its own way.

- **Make a Video with Four Frames**:
I split the output into four sections, showing how each tracker worked side by side. The video also displayed the tracker names and FPS (frames per second).

### Final Output
The output video, football_tracking_all_algorithms.mp4, shows the results. The trackers worked okay, but not all of them were perfect:

1. The TLD tracker did the best job. It kept tracking the football even when the ball moved fast.
2. Other trackers sometimes lost the ball or got confused.

### Problems I Faced
The hardest part was combining all the tracker outputs into one video. Making four frames in a single video was tricky for me, but after some tries, I made it work. The rest of the code was straightforward and worked fine.

### Why This Project is Useful
This project helped me understand how object tracking works. Now, I know the strengths and weaknesses of different trackers. This can be useful for more complex projects in the future.

### Feedback
I’m still learning, so any suggestions or feedback would be great! 😊
