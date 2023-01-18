
class user:

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
        return "Name of user: " + self._userName + " Region to ski: " + self._region + " Email: " + self._email 

    