from app import db, Hero, Power, HeroPower

# Create some heroes and add them to the database
heroes = [
    Hero(name='Kamala Khan', super_name='Ms. Marvel'),
    Hero(name='Doreen Green', super_name='Squirrel Girl'),
    Hero(name='Gwen Stacy', super_name='Spider-Gwen'),
    Hero(name='Janet Van Dyne', super_name='The Wasp'),
    Hero(name='Wanda Maximoff', super_name='Scarlet Witch'),
    Hero(name='Carol Danvers', super_name='Captain Marvel'),
    Hero(name='Jean Grey', super_name='Dark Phoenix')
]

# Add heroes to the database session
for hero in heroes:
    db.session.add(hero)

# Commit the changes to the database
db.session.commit()
