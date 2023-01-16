

class skiRoute:

   

    def __init__(self, region, belowTreeline, nearTreeline, aboveTreeline, avyTerrain, avyAvoidable, funOften, riskOften):
        """
        Create a new skiRoute object. 
        """
        
        self.region = region
        self._belowTreeline = belowTreeline
        self._nearTreeline = nearTreeline
        self._aboveTreeline = aboveTreeline
        self._avyTerrain = avyTerrain
        self._avyAvoidable = avyAvoidable
        self._funOften = funOften
        self._riskOften = riskOften

    def get_region(self):
        """
        get the region that a route is in
        """
        return self._region

    def get_belowTreeline(self):
        """
        """
        return self._belowTreeline

    def get_nearTreeline(self):
        """
        """
        return self._nearTreeline
    
    def get_aboveTreeline(self):
        """
        """
        return self._aboveTreeline
    
    def get_avyTerrain(self):
        """
        """
        return self._avyTerrain

    def get_avyAvoidable(self):
        """
        """
        return self._avyAvoidable
    
    def get_funOften(self):
        """
        """
        return self._funOften

    def get_riskOften(self):
        """
        """
        return self._riskOften
