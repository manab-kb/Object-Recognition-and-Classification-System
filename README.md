# Object Recognition System
An Object Recognition and classification system has been built here. The code is mainly divided into two parts :

1. *Object Recognition in still/non movable images* 
2. *Object Detection in live images*

### Start screen / Home Page of the application :

<p align="center">
<img width="448" alt="Start_Page" src="https://user-images.githubusercontent.com/77844663/111804240-e4af7080-88f5-11eb-8afc-4cd43003aae2.PNG" >
</p>

### 1. Object Recognition
The user is given a choice to select local files from the file dialogue of their own device and upload it into the GUI, which passes it on to the *Convolutional Neural Network (CNN)* for processing and returns the *Class Name* of the image with a specific level of accuracy. 

#### *NOTE: Only '.png' files are recognizable by the CNN created. Providing any other file type will trigger an error and not let the application proceed further*

### File Dialogue : Selection of Files
<p align="center">
<img width="902" alt="Page_1" src="https://user-images.githubusercontent.com/77844663/111804265-ec6f1500-88f5-11eb-8b32-da1feac15714.PNG" align="center">
</p>

### Publication of Results from the CNN :
<p align="center">
<img width="449" alt="Page_2" src="https://user-images.githubusercontent.com/77844663/111804277-f133c900-88f5-11eb-90ff-5057459d1afc.PNG" align="Center">
</p>
As seen in the image above, the result displayed by the CNN on the GUI consists of the *Image class name* and the *Accuracy percentage* associated with the image.

### 2. Image Detection
The user turns on their deivce's inbuilt camera via the GUI using the *Live Feed* button, which detects if an object is present in front of the camera by comparing it with a referrence image, provided previously to the backend of the code.

#### *NOTE: The camera has not been displayed for security purposes. The black window is the camera module opened up on the screen*

<p align="center">
<img width="903" alt="Page_3" src="https://user-images.githubusercontent.com/77844663/111804313-f8f36d80-88f5-11eb-81d9-f4e44951c658.PNG" align="center">
</p>
