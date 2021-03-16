import cv2
import numpy as np


def sift_detector(new_image, image_template):
    # Function that compares input image to template
    # It then returns the number of SIFT matches between them
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    image2 = image_template

    # Create SIFT detector object
    # sift = cv2.SIFT()
    sift = cv2.xfeatures2d.SIFT_create()
    # Obtain the keypoints and descriptors using SIFT
    keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

    # Define parameters for our Flann Matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=3)
    search_params = dict(checks=100)

    # Create the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Obtain matches using K-Nearest Neighbor Method
    # the result 'matches' is the number of similar matches found in both images
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Store good matches using Lowe's ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
    return len(good_matches)


# Load our image template, this is our reference image
image_template = [cv2.imread('Face_Testing.jpg', 0)]


def live_feed():
    cap = cv2.VideoCapture(0)
    while True:
        # Get webcam images
        ret, frame3 = cap.read()

        # Get height and width of webcam frame
        height, width = frame3.shape[:2]

        # Define ROI Box Dimensions
        top_left_x = int(width / 3)
        top_left_y = int((height / 2) + (height / 4))
        bottom_right_x = int((width / 3) * 2)
        bottom_right_y = int((height / 2) - (height / 4))

        # Draw rectangular window for our region of interest
        cv2.rectangle(frame3, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), 255, 3)

        # Crop window of observation we defined above
        cropped = frame3[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        # Flip frame orientation horizontally
        frame = cv2.flip(frame3, 1)

        # Get number of SIFT matches
        # for i in range(len(image_template)):
        matches = sift_detector(cropped, image_template[0])

        # Display status string showing the current no. of matches
        cv2.putText(frame3, str(matches), (450, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 1)

        # Our threshold to indicate object detection
        # We use 10 since the SIFT detector returns little false positives
        threshold = 10

        # If matches exceed our threshold then object has been detected
        if matches > threshold:
            cv2.rectangle(frame3, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame3, 'Object Found', (100, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        cv2.imshow('Live Feed', frame3)
        if cv2.waitKey(1) == 27:  # 27 is the Esc Key
            break

    cap.release()
    cv2.destroyAllWindows()
