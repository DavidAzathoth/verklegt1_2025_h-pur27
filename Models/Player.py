class Player:
    """## Attributes for Player:
      \nteamID 
      \nplayerGamertag 
      \nfullname phonenumber 
      \nemailAddress 
      \naddress 
      \nlink 
      \ndateOfBirth"""
    def __init__(self, teamID: str, playerGamertag: str, fullname: str, phoneNumber: str, emailAddress: str, address: str, link: str, dateOfBirth: str):
        self.teamID = teamID
        self.playerGamertag = playerGamertag
        self.fullname = fullname
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address
        self.link = link
        self.dateOfBirth = dateOfBirth
    def createCSVString(self):
        """Creates a row to store in a csv file"""
        ret_string: str = f'{self.teamID},{self.playerGamertag},"{self.fullname}",{self.phoneNumber},{self.emailAddress},{self.address},{self.link},{self.dateOfBirth}'
        return ret_string