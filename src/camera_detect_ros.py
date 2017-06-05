# coding:utf-8
#!/usr/bin/env python

# /zed/left/image_rect_color から流れてくる

import sys, rospy, cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cascade_path = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

color = (255,255,255)

class image_converter:
    def __init__(self):
        # 送るノード
        self.image_pub = rospy.Publisher("/detect_face", Image, queue_size=10)

        # 受け取るノード
        self.image_sub = rospy.Subscriber("/zed/left/image_rect_color", Image, self.callback)

        self.bridge = CvBridge()


    def callback(self, data):
        try:
            # ROSのメッセージをcv2に変換
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print e
        # 3次元変換 
        (rows, cols, channels) = cv_image.shape
        
        face_detect = cascade.detectMultiScale(cv_image, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))


        if cols > 60 and rows > 60:


        #face_detect = cascade.detectMultiScale(rows, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))
            for rect in face_detect:
            # □　でくくる
                cv2.rectangle(cv_image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)


        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
        except CvBridgeError as e:
            print e

def main(args):
    ic = image_converter()

    # 
    rospy.init_node('image_converter', anonymous=True)

    try:
        rospy.spin()
    except:
        print "Shutting Down"

#if __name__ == '__main__':
print "Start"
main(sys.argv)    











