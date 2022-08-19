from ctoybox import Toybox, Input
import toybox.interventions.amidar as amidar
from toybox.interventions.amidar import AmidarIntervention, Amidar

from abc import ABC, abstractmethod

possible_options = [(25, 217), (217, 25), (447, 639), (639, 447), (447, 255), (255, 447)]

def tilepoint_to_junctionpoint(x, y):
    return (31-y)*32 + x

def json_to_tilepoint(x, y):
    SCALE = 16
    TILE_SIZE = (4,5)
    return x/(TILE_SIZE[0]*16), y/(TILE_SIZE[1]*16)


class FillOption:
    def __init__(self):
        self.start = -1 
        self.destination = -1
    
    def initiate(self, env):
        """
        To start the option,
        * Agent must be on a certain unpainted (TODO) tile (self.start). 
        * TODO Destination must be unpainted.
        * TODO All enemies must be 7+ tiles away. 
        """
        state = env.toybox.state_to_json()
        json_position = state["player"]["position"]
        x, y = json_to_tilepoint(json_position["x"], json_position["y"])
        position_junction = tilepoint_to_junctionpoint(x, y)
        
        # print("Position:")
        # print(position_junction)
        for possible in possible_options:
            if possible[0] == position_junction:
                self.start = possible[0]
                self.destination = possible[1]
                print("Starting option: ")
                print(self.start)
                print(self.destination)
                return (self.start, self.destination)
        return None

    def get_action(self):
        if self.start < self.destination: 
            if self.destination-self.start <= 31:
                print("action: 3")
                return 3 # RIGHT
            else:
                print("action: 5")
                return 5 # DOWN
        else:
            if self.start-self.destination <= 31:
                print("action: 4")
                return 4 # LEFT
            else:
                print("action: 2")
                return 2 # UP

    def terminate(self, env):
        """
        Terminate if 
        * Destination is reached.
        * TODO An enemy comes within 7 tiles.
        """
        state = env.toybox.state_to_json()
        json_position = state["player"]["position"]
        x, y = json_to_tilepoint(json_position["x"], json_position["y"])
        position_junction = tilepoint_to_junctionpoint(x, y)
        
        if position_junction == self.destination:
            print("destination reached")
            return True
        return False
