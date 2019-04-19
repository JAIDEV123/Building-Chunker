import sqlalchemy, sys
from sqlalchemy import create_engine

class data:
	
	def __init__(self):
		self.db = create_engine("sqlite:///forum.db")

	def retrievepost(self):
		posts = self.db.engine.execute("SELECT * FROM POSTS")
		return posts

	def createpost(self,new):
		self.db.engine.execute("INSERT INTO POSTS VALUES(:name, :topic, :content)", name=new["name"], topic=new["topic"], content=new["content"])