from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///projectthree.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
# User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
#              picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
# session.add(User1)
# session.commit()

# Menu for UrbanBurger
category1 = Category( name="Shows")

session.add(category1)
session.commit()

item2 = Item( name="Teen Titans Go!", description="2010 version of Teen titans. Group of super teens that love to joke around.", category=category1)

session.add(item2)
session.commit()


item1 = Item( name="Young Justice", description="Teen version of Justice League, made in the 2010s.", category=category1)

session.add(item1)
session.commit()



category2 = Category( name="Artists")

session.add(category1)
session.commit()

item2 = Item( name="Bruno Mars", description="Super star musician, that's what I like.", category=category2)
session.add(item2)
session.commit()

item3 = Item( name="Drake", description="second best rapper in the game", category=category2)

session.add(item3)
session.commit()

item4 = Item( name="Kendrick Lamar", description="Best rapper in the game", category=category1)

session.add(item4)
session.commit()
