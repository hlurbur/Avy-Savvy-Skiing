
class user:
    """
    A user of the program. Each user has an associated name, region they wish to ski in,
    and email.
    """

    def __init__(self, userName, skiRegion, email):
        """
        create a new user object
        """

        self._userName = userName
        self._skiRegion = skiRegion
        self._email = email

    def __str__(self) -> str:
        """
        return the string representation of a user
        """
        return "Name of user: " + self._userName + " Region to ski: " + self._skiRegion + " Email: " + self._email 

    def get_userName(self):
        """
        return a string of the name of the user
        """
        return self._userName
    
    def get_skiRegion(self):
        """
        return the string of the region the user wants to ski in
        """
        return self._skiRegion

    def get_email(self):
        """
        return the string of the email of the user
        """
        return self._email 
