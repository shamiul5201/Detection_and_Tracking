# Football Tracker

<video width="600" controls>
  <source src=".//football_tracking_all_algorithms.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


https://github.com/user-attachments/assets/c19cb502-29cb-44ac-9b8b-e66100c254a2

This Python script compares the performance of five OpenCV tracking algorithms (BOOSTING, MIL, KCF, TLD, CSRT) by tracking a selected object in a video. It displays the tracking results in a four-quadrant view and saves the output as a video file. This demonstration is useful for evaluating the suitability of different tracking algorithms for various use cases.

## Purpose and Use Cases
The script serves multiple purposes:

- **Algorithm Comparison**: Helps evaluate tracking algorithms for specific tasks.
- **Visualization**: Offers an interactive view of tracking performance.
- **Research and Development**: Provides a foundation for experimenting with tracking techniques in computer vision.

## Code Walkthrough
### 1. Defining Tracker Types
The script defines five tracker types:
```python
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'CSRT']
trackers = []
```
Each tracker offers different performance trade-offs, such as speed, accuracy, and robustness.

### 2. Loading and Initializing the Video
The script loads a video and reads the first frame:
```python
videoPath = "soccer-ball.mp4"
cap = cv2.VideoCapture(videoPath)

ret, frame = cap.read()
if not ret:
    print("Error: Failed to read video")
    exit()

```
`cv2.VideoCapture`: Handles video input.
**Error Handling**: Stops execution if the video cannot be loaded.

### 3. Region of Interest (ROI) Selection
Select the object to track using cv2.selectROI:

```python
bbox = cv2.selectROI(frame, False)  # Select the football in the first frame
```
This allows the user to manually define the bounding box around the object in the first frame.

### 4. Tracker Initialization
For each tracker type, a corresponding tracker is created and initialized:
```python
for tracker_type in tracker_types:
    if tracker_type == 'BOOSTING':
        tracker = cv2.legacy.TrackerBoosting_create()
    ...
    trackers.append(tracker)

for tracker in trackers:
    tracker.init(frame, bbox)

```
* `cv2.legacy.TrackerX_create()`: Initializes the selected tracker.
* `tracker.init()`: Binds the tracker to the initial frame and bounding box.

### 5. Creating the Output Video
Define the output video properties:
```python
out = cv2.VideoWriter(
    'football_tracking_all_algorithms.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width * 2, frame_height * 2)
)
```
* Multiplication by 2: Accounts for the four-quadrant display layout.

### 6. Processing Video Frames
The main loop processes frames:
```python
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

```
Each frame is processed until the video ends or a termination condition is met.

### 7. Updating Trackers and Displaying Results
For each tracker:
* Update the tracker with the current frame.
* Draw the bounding box if tracking succeeds; display an error otherwise.
* Place the result in one of the quadrants.

### Example Use Cases
* Sports Analytics: Track the motion of a soccer ball during a game.
* Object Tracking: Evaluate object-tracking algorithms for surveillance systems.
* Machine Learning: Use as a baseline to develop advanced tracking models.

### Contribution and Feedback
Suggestions or feedback are always appreciated to refine this project further. 
gmail: shamiulislamnoyon@gmail.com
