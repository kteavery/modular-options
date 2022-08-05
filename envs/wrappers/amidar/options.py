from ctoybox import Toybox, Input
import toybox.interventions.amidar as amidar
from toybox.interventions.amidar import AmidarIntervention, Amidar


class FillOption:
    def __init__(self, start, destination):
        self.start = start 
        self.destination = destination
    
    def conditions():
        """
        To start the option,
        * Agent must be on a certain unpainted tile (self.start). 
        * Destination must be unpainted.
        * All enemies must be 7+ tiles away. 
        """
        pass

    def local_policy():
        pass

    def terminate():
        """
        Terminate if 
        * Destination is reached.
        * An enemy comes within 7 tiles.
        """
        pass
    