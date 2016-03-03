#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pypot.robot
from pypot.primitive.move import MoveRecorder, Move, MovePlayer


class CommentTuTeSens(pypot.primitive.Primitive):
    def __init__(self, robot):
            pypot.primitive.Primitive.__init__(self, robot)
            self._robot = robot
        

    def start(self):
            
            pypot.primitive.Primitive.start(self)

    def run(self):
     
                move = '/home/poppy/cherry/resources/optional/move/commentTuTeSens.move'
        
                with open(move) as f:
                    m = Move.load(f)
                    
                self._robot.compliant = False
                
                speak.start("Et comment tu te sens quand tu parles à un robot ?" ) 
                
                move_player = MovePlayer(self._robot, m)
                time.sleep(1.5)
                move_player.start()
