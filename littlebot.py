#!/usr/bin/env python



import rospy
from std_msgs.msg import String
from sound_play.libsoundplay import SoundClient
import sys
import os

class LittleBot:
    def __init__(self, script_path):
        rospy.init_node('littlebot')

        rospy.on_shutdown(self.cleanup)
        
        self.wavepath = rospy.get_param("~wavepath", script_path + "/../sounds")
        
        self.soundhandle = SoundClient(blocking=True)
        
        rospy.sleep(1)
        
        self.soundhandle.stopAll()
        
        self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
       
        rospy.loginfo("Ready, waiting for commands...")
	self.soundhandle.say('Hello. Nice to meet you.')
	
        rospy.Subscriber('/lm_data', String, self.talkback)


    def talkback(self, msg):
       
        rospy.loginfo(msg.data)

	if msg.data.find('WHO-ARE-YOU')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        
		self.soundhandle.say("I am LittleBot. I will be your friend.")
		 
	elif msg.data.find('WHERE-ARE-YOU-FROM')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	
		self.soundhandle.say("I heard you ask about my hometown. I am from Tianjin.")
        	
	elif msg.data.find('WHAT-CAN-YOU-DO')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	
		self.soundhandle.say("I am a baby now, so I can just do little things. But I will learn.")
		
	elif msg.data.find('DO-YOU-KNOW-ME')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	
		self.soundhandle.say("Of course. I am clever than you.")
		
        elif msg.data.find('DO-YOU-LIKE-DOING-HOMEWORK')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	
		self.soundhandle.say("Well, I do not have homework.")
		
        elif msg.data.find('GOODBYE')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	
		self.soundhandle.say("goodbye")
		

    def cleanup(self):
        self.soundhandle.stopAll()
        rospy.loginfo("Shutting down littlebot node...")

if __name__=="__main__":
    try:
        LittleBot(sys.path[0])
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("littlebot node terminated.")
