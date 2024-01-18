"""
Flight Leg:

IND -> US

2 segments (IND -> DUB, DUB -> US)

"""
from typing import List

class Segment:
    def __init__(self,departure,destination):
        self.departure = departure
        self.destination = destination
        
        
class Flight:
    def __init__(self,segments: List[Segment]):
        self.segments = segments
    
    def __repr__(self):
        """
        return : string in the format of IND -> DUB -> US
        """
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)
            
        return ' -> '.join(stops)
    
    @property
    def departure_point(self) -> str:
        return self.segments[0].departure
    
    @departure_point.setter
    def departure_point(self,val):
        # self.segments[0].departure = val
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val,destination=dest)
        

        
        
flight = Flight([Segment('IND','US')])
print(flight)
flight.departure_point = 'EDI'
print(flight)
