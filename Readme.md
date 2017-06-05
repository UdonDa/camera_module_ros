##How to use camera_detect_ros.py  
1. roscore(76)
2. roslaunch zed_wrapper zed.launch)(233)
3. python camera_detect_ros.py(233)
4. rqt_image_view)(77)



##How to use image_recognition.py
1. roscore
2. rosrun cv_camera cv_camera_node
3. python image_recognition.py image:/cv_camera/image_raw
4. rostopic /tensorflow/publisher
