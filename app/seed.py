from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Attribute, QuestLine

engine = create_engine("sqlite:///rpg.db")
Session = sessionmaker(bind=engine)
session = Session()

session.query(Attribute).delete()
session.query(QuestLine).delete()
session.commit()

attributes = [Attribute(name="INT", display_name="智力"),
              Attribute(name="STR", display_name="力量"),
              Attribute(name="SAN", display_name="精神力"),
              Attribute(name="WIS", display_name="智慧"),
              Attribute(name="CHA", display_name="魅力")]

session.add_all(attributes)
session.commit()
print("屬性資料新增完成")

quest_lines = [QuestLine(name="學業系統", type="主線"),
               QuestLine(name="健康系統", type="主線"),
               QuestLine(name="自我拓展", type="主線"),
               QuestLine(name="社團", type="副線"),
               QuestLine(name="專案開發", type="副線")]

session.add_all(quest_lines)
session.commit()
print("QuestLine 資料新增完成")

