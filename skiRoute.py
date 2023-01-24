

class skiRoute:

   

    def __init__(self, name, region, belowTreeline, nearTreeline, aboveTreeline, avyTerrain, avyAvoidable, funOften, riskOften):
        """
        Create a new skiRoute object. 
        """
        self._name = name
        self._region = region
        self._belowTreeline = belowTreeline
        self._nearTreeline = nearTreeline
        self._aboveTreeline = aboveTreeline
        self._avyTerrain = avyTerrain
        self._avyAvoidable = avyAvoidable
        self._funOften = funOften
        self._riskOften = riskOften

    def __str__(self) -> str:
        """
        return the string representation of a Ski Route
        """
        routeStr = "Name:" + self._name + ", Region:" + self._region + ", BelowTL:" + str(self._belowTreeline) + ", Near TL:" + str(self._nearTreeline) + ", AboveTL:" + str(self._aboveTreeline) + ", AvyTrr:" + str(self._avyTerrain) + ", Avoidable:" +  str(self._avyAvoidable) + ", Fun/10:" + str(self._funOften) + ", Risk/10:" + str(self._riskOften)
        return routeStr

    def get_name(self):
        """
        get the name of the route
        """
        return self._name

    def get_region(self):
        """
        get the region that a route is in
        """
        return self._region

    def get_belowTreeline(self):
        """
        return T or F is the route crosses enters bwlow treeline elevation
        """
        #return the boolean of the true false string
        return self._belowTreeline

    def get_nearTreeline(self):
        """
        return T or F if the route croses near treeline elevation
        """
        #return the boolean of the true false string
        return eval(self._nearTreeline)
    
    def get_aboveTreeline(self):
        """
        return T of F if the route crosses above treeline elevation
        """
        #return the boolean of the string
        return eval(self._aboveTreeline)
    
    def get_avyTerrain(self):
        """
        return T of F if the route enters avalanche terrain
        """
        #return the boolean of the true false string
        return eval(self._avyTerrain)

    def get_avyAvoidable(self):
        """
        return T or F if it is possible to complete the route while avoiding avalanche terrain
        """
        #return the boolean of the true false string
        return eval(self._avyAvoidable)
    
    def get_funOften(self):
        """
        Return the route's fun score ranked out of 10
        """
        #return the integer of the string value
        return self._funOften

    def get_risk(self):
        """
        return the route's general risk score out of 10
        """
        return self._riskOften
