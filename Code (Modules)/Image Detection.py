import cv2
import numpy as np

#Function to match live image and image template
#Returns the keypoint matches in both the images
def sift_detector(new_image, image_template):
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    image2 = image_template

    # Create SIFT detector object
    sift = cv2.xfeatures2d.SIFT_create()
    
    # Obtain the keypoints and descriptors using the SIFT function
    keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

    # Define parameters for the Flann Based Matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=3)
    search_params = dict(checks=100)

    # Creating the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    #Computing number of similiar matches found in both the objects
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Store the good matches using Lowe's ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
    return len(good_matches)


#Creating a list of refference images
image_template = [cv2.imread('Face_Testing.jpg', 0)]


def live_feed():
    cap = cv2.VideoCapture(0)
    while True:
        
        # Obtain webcam images
        ret, frame3 = cap.read()

        # Obtaining height and width of webcam frame
        height, width = frame3.shape[:2]

        # Defining ROI Box Dimensions
        top_left_x = int(width / 3)
        top_left_y = int((height / 2) + (height / 4))
        bottom_right_x = int((width / 3) * 2)
        bottom_right_y = int((height / 2) - (height / 4))

        # Drawing a rectangular window for the region of interest
        cv2.rectangle(frame3, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), 255, 3)

        # Cropping window of observation we defined above
        cropped = frame3[bottom_right_y:top_left_y, top_left_x:bottom_right_x]

        # Flipping the frame orientation horizontally
        frame = cv2.flip(frame3, 1)

        # Getting the number of SIFT matches
        
        #A for loop has been created to integrate an option of multiple referrence images later on
        # for i in range(len(image_template)):
        matches = sift_detector(cropped, image_template[0])

        # Displaying status string showing the current no. of matches
        cv2.putText(frame3, str(matches), (450, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 1)
        
        threshold = 10
        if matches > threshold:
            cv2.rectangle(frame3, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 3)
            cv2.putText(frame3, 'Object Found', (100, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        cv2.imshow('Live Feed', frame3)
        if cv2.waitKey(1) == 27:  #27 is the Esc Key
            break

    cap.release()
    cv2.destroyAllWindows()
