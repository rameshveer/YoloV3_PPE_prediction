# YOLO v3 PPE(Personal Protection Equipments) Object Detection:

Below PPE objects can be detected from the required video/image

1. hard hat
2. vest
3. mask
4. boots


PPE object detection after Yolo training with custom dataset:
	
![image](https://github.com/rameshveer/School_of_AI-EVA_5/blob/master/S13/Yolo%20Open%20CV/Annotated_Yolo_Images/Unknown.jpg)
	

### Dataset Preparation:
  	Custom Dataset was prepared to extract images with PPE objects from Google. 
  
  	Code link - https://github.com/rameshveer/YoloV3_PPE_prediction/blob/master/image_scrapper.ipynb
  
  
### Annotation:
	Bounding Boxes(BBox) for the objects in extracted images were manually done using below tool. 
	
	This tool will automatically calculate the x,y co-ordinates of the BBox and put it in yolov3 format via text file.

### Training:
	After collecting and annotating around 3500 PPE images, they were cleaned and fed to the yolov3 model.
	
	Model was trained using Google Colab(Tesla T4 GPU) for 50 epochs only in 5 hrs. More epochs would fetch far more accurate results.


### Youtube link for PPE object detecion with custom Yolo training:
	
https://www.youtube.com/watch?v=U8lIk9Qhy94
	
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/U8lIk9Qhy94/0.jpg)](http://www.youtube.com/watch?v=U8lIk9Qhy94)


### Yolo V3 architecture can be applied for object detection on various sectors and applications.

