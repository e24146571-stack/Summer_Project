from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Attribute

engine = create_engine("sqlite:///rpg.db")
Session = sessionmaker(bind=engine)
session = Session()

attributes = [Attribute(name="INT", display_name="智力"),
              Attribute(name="STR", display_name="力量"),
              Attribute(name="SAN", display_name="精神力"),
              Attribute(name="WIS", display_name="智慧"),
              Attribute(name="CHA", display_name="魅力")]

session.add_all(attributes)
session.commit()

print("屬性資料新增完成")