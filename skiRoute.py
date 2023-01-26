

class skiRoute:
    """
    A class for a ski route. Each ski route passes through different elevation levels and
    either does or doesn't enter avalanche terrain. Additionally, some routes can be still be completed with minor
    changes to avoid avalanche terrain while other must enter avalanche terrain to complete. Routes are also given a fun
    rating and a risk rating which captures how exposed and generally risky a route feels while skiing.
    """

   

    def __init__(self, name, region, belowTreeline, nearTreeline, aboveTreeline, avyTerrain, avyAvoidable, funOften, riskOften):
        """
        Create a new skiRoute object. 
        Args:
        name (string)- the name of the route
        region (string)- the name of the region in the Cascades that the route is in
        belowTreeline (bool)- True if the route enters the below treeline elevation band
        nearTreeline (bool)- True if the route enters the near treeline elevation band
        aboveTreeline (bool)- True if the route enters the above treeline elevation band
        avyTerrain (bool)- True if the route enters avalanche terrain (slope angle above 30 degrees)
        avyAvoidable (bool)- True if the route can be tweaked to avoid avalanche terrain
        funOften (int)- how fun the route is on a scale of 10
        riskOften (int) - how "risky" the route is on a scale of 10. This captures how exposed, remote, or scary the
        route is in terms of avalanche danger. (sometime certain skis are just scarier haha)
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
        routeStr =  self._name.upper() + " Region: " + self._region + ", BelowTL: " + str(self._belowTreeline) + ", Near TL: " + str(self._nearTreeline) + ", AboveTL: " + str(self._aboveTreeline) + ", AvyTrr: " + str(self._avyTerrain) + ", Avoidable: " +  str(self._avyAvoidable) + ", Fun/10: " + str(self._funOften) + ", Risk/10: " + str(self._riskOften)
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
        return T or F is the route crosses enters below treeline elevation
        """
        #return the boolean of the true false string
        return self._belowTreeline

    def get_nearTreeline(self):
        """
        return T or F if the route crosses near treeline elevation
        """
        #return the boolean of the true false string
        return self._nearTreeline
    
    def get_aboveTreeline(self):
        """
        return T of F if the route crosses above treeline elevation
        """
        #return the boolean of the string
        return self._aboveTreeline
    
    def get_avyTerrain(self):
        """
        return T of F if the route enters avalanche terrain
        """
        #return the boolean of the true false string
        return self._avyTerrain

    def get_avyAvoidable(self):
        """
        return T or F if it is possible to complete the route while avoiding avalanche terrain
        """
        #return the boolean of the true false string
        return self._avyAvoidable
    
    def get_funOften(self):
        """
        Return the route's fun score ranked out of 10
        """
        
        return self._funOften

    def get_risk(self):
        """
        return the route's general risk score out of 10
        """
        return self._riskOften
