from ctoybox import Toybox, Input
import toybox.interventions.amidar as amidar
from toybox.interventions.amidar import AmidarIntervention, Amidar

possible_options = [(25, 217)]

class FillOption:
    def __init__(self):
        self.tb = Toybox('amidar')
        self.start = -1 
        self.destination = -1
    
    def initiate(self):
        """
        To start the option,
        * Agent must be on a certain unpainted tile (self.start). 
        * Destination must be unpainted.
        * All enemies must be 7+ tiles away. 
        """
        with AmidarIntervention(self.tb) as intervention:
            position = intervention.worldpoint_to_tilepoint(intervention.game.player.position)
            for possible in possible_options:
                if possible[0] == position:
                    self.start = possible[0]
                    self.destination = possible[1]
                    return (self.start, self.destination)


    def get_action(self):
        if self.start < self.destination: 
            if self.destination-self.start <= 31:
                return RIGHT
            else:
                return DOWN
        else:
            if self.start-self.destination <= 31:
                return LEFT
            else:
                return UP

    def terminate(self):
        """
        Terminate if 
        * Destination is reached.
        * An enemy comes within 7 tiles.
        """
        position = intervention.worldpoint_to_tilepoint(intervention.game.player.position)
        if position == self.destination:
            return True
        return False
    