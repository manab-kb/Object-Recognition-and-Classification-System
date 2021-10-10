# Object Recognition System
An Object Recognition and classification system has been built here. The code is mainly divided into two parts :

1. *Object Recognition in still/non-movable images* 
2. *Object Detection in live images*

### Start screen / Home Page of the application :

<p align="center">
<img width="448" alt="Start_Page" src="https://user-images.githubusercontent.com/77844663/111804240-e4af7080-88f5-11eb-8afc-4cd43003aae2.PNG" >
</p>

### 1. Object Recognition
The user is given a choice to select local files from the file dialogue of their own device and upload it into the GUI, which passes it on to the *Convolutional Neural Network (CNN)* for processing and returns the *Class Name* of the image with a specific level of accuracy. 

#### *NOTE: Only '.png' files are recognizable by the CNN created. Providing any other file type will trigger an error and not allow the application to proceed further.*

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

#### *NOTE: The camera has not been displayed for security purposes. The black window open on the screen is the camera module.*

<p align="center">
<img width="903" alt="Page_3" src="https://user-images.githubusercontent.com/77844663/111804313-f8f36d80-88f5-11eb-81d9-f4e44951c658.PNG" align="center">
</p>

# Contributing to Object Recognition and Classification System
Hello and welcome! We are so glad that you are interested in contributing to the Object Recognition and Classification System!
We only have a couple of rules and we hope you enjoy the process :)

## Contributing Rules
1. Don't move or delete any files. Only modify them.
2. Put all CNN Model related codes in the CNN.py file, found under the 'Code (Modules)' folder. This also requires you to follow Rule 6 below in the list.
3. Put all GUI related codes in the GUI.py file, found under the 'Code (Modules)' folder.
4. Put all Live Object Detection related codes in the 'Image Detection.py' file, found under the 'Code (Modules)' folder.
5. Put all New model related codes in the 'Code (Modules)' folder.
6. Upload the entire model file ('.h5' extension) in the CNN_Model folder.

## Contributing Process
1. Fork the repository
2. Clone your forked repository to your computer
3. Head to the issues tab and look for an issue that you like.
4. Once you have decided what issue to work on, give it a shot!
5. Once done, push the code to your forked repository.
6. Head to the Pull Requests tab and click on "Create New Pull Request"
7. On the left of the arrow should be this repo and on the right should be yours.
8. Add a small description to the Pull Request describing what you've done.
9. Mention what Issue you have worked on. If the issue number is #3, you can mention "Closes #3" in the Pull Request description.
10. Submit Pull Request

It's that easy! We hope you enjoy contributing to our repository. Don't hesitate to contact any of the maintainers or ACM team about any problems!
