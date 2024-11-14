import cv2
import numpy as np
import time

# Define tracker types
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'CSRT']
trackers = []

# Open video file
videoPath = "soccer-ball.mp4"
cap = cv2.VideoCapture(videoPath)

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Error: Failed to read video")
    exit()

# Select the ROI (bounding box) manually using cv2.selectROI
bbox = cv2.selectROI(frame, False)  # Select the football in the first frame

# Initialize the trackers for each type
for tracker_type in tracker_types:
    if tracker_type == 'BOOSTING':
        tracker = cv2.legacy.TrackerBoosting_create()
    elif tracker_type == 'MIL':
        tracker = cv2.legacy.TrackerMIL_create()
    elif tracker_type == 'KCF':
        tracker = cv2.legacy.TrackerKCF_create()
    elif tracker_type == 'TLD':
        tracker = cv2.legacy.TrackerTLD_create()
    elif tracker_type == 'CSRT':
        tracker = cv2.TrackerCSRT_create()
    trackers.append(tracker)

# Initialize the trackers with the first frame and bounding box
for tracker in trackers:
    tracker.init(frame, bbox)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object to save the output video
out = cv2.VideoWriter('football_tracking_all_algorithms.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width * 2, frame_height * 2))

# Start time to calculate FPS
start_time = time.time()
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    elapsed_time = time.time() - start_time
    current_fps = frame_count / elapsed_time if elapsed_time > 0 else 0
    
    # Create a blank canvas for the 4 quadrant video
    combined_frame = np.zeros((frame_height * 2, frame_width * 2, 3), dtype=np.uint8)
    
    # Update each tracker and draw its bounding box in the appropriate quadrant
    for i, (tracker, tracker_type) in enumerate(zip(trackers, tracker_types)):
        ok, bbox = tracker.update(frame)
        color = (0, 255, 0) if ok else (0, 0, 255)  # Green for tracking success, Red for failure
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        
        # Define position for placing the tracker result in each quadrant
        if i == 0:  # Top-left
            frame_segment = frame.copy()
            if ok:
                cv2.rectangle(frame_segment, p1, p2, color, 2)
            else:
                cv2.putText(frame_segment, "Tracking failure", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            combined_frame[0:frame_height, 0:frame_width] = frame_segment
            # Add tracker name and FPS
            cv2.putText(combined_frame, f"{tracker_type} - FPS: {current_fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        elif i == 1:  # Top-right
            frame_segment = frame.copy()
            if ok:
                cv2.rectangle(frame_segment, p1, p2, color, 2)
            else:
                cv2.putText(frame_segment, "Tracking failure", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            combined_frame[0:frame_height, frame_width:frame_width * 2] = frame_segment
            # Add tracker name and FPS
            cv2.putText(combined_frame, f"{tracker_type} - FPS: {current_fps:.2f}", (frame_width + 10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        elif i == 2:  # Bottom-left
            frame_segment = frame.copy()
            if ok:
                cv2.rectangle(frame_segment, p1, p2, color, 2)
            else:
                cv2.putText(frame_segment, "Tracking failure", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            combined_frame[frame_height:frame_height * 2, 0:frame_width] = frame_segment
            # Add tracker name and FPS
            cv2.putText(combined_frame, f"{tracker_type} - FPS: {current_fps:.2f}", (10, frame_height + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        elif i == 3:  # Bottom-right
            frame_segment = frame.copy()
            if ok:
                cv2.rectangle(frame_segment, p1, p2, color, 2)
            else:
                cv2.putText(frame_segment, "Tracking failure", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            combined_frame[frame_height:frame_height * 2, frame_width:frame_width * 2] = frame_segment
            # Add tracker name and FPS
            cv2.putText(combined_frame, f"{tracker_type} - FPS: {current_fps:.2f}", (frame_width + 10, frame_height + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    
    # Write the combined frame to the output video
    out.write(combined_frame)

    # Display the frame with the tracking results in the 4 quadrants
    cv2.imshow("Tracking Algorithms Comparison", combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
