class Player:
    """## Attributes for Player:
      \nteamID 
      \nplayerGamertag 
      \nfullname 
      \nphoneNumber 
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
        """Creates a string seperated by commas"""
        ret_string: str = f'{self.teamID},{self.playerGamertag},"{self.fullname}",{self.phoneNumber},{self.emailAddress},{self.address},{self.link},{self.dateOfBirth}'
        return ret_string
    def createCSVDict(self):
        """Creates a dict to store in a csv file"""
        ret_dic: dict = {'teamID':self.teamID,'playerGamertag':self.playerGamertag,'fullname':self.fullname,'phoneNumber':self.phoneNumber,'emailAddress':self.emailAddress,'address':self.address,'link':self.link,'dateOfBirth':self.dateOfBirth}
        return ret_dic
    def __str__(self):
        return f"""
Handle: {self.playerGamertag}
Name: {self.fullname}
Date of birth(YYYY-MM-DD): {self.dateOfBirth}
Address: {self.address}
Phone number: {self.phoneNumber}
E-mail: {self.emailAddress}
Link: {self.link}
        """