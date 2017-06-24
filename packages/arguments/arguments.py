class arguments:
    """This class handles the command lines arguments.
    
    It has been designed like this for a simpler and better tests. 
    """
    
    __singleton = None
    
    def __init__(self,):
        """Creation of the singleton and initialization if required.
        """
    
    def getSingleton(self,):
        if (arguments.__singleton):
            return arguments.__singleton
        arguments.__singleton = arguments()
        return arguments.__singleton
