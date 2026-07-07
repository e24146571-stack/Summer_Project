from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Attribute, QuestLine, ActivityType

engine = create_engine("sqlite:///rpg.db")
Session = sessionmaker(bind=engine)
session = Session()

session.query(Attribute).delete()
session.query(QuestLine).delete()
session.query(ActivityType).delete()
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

# 查詢 Attributes
attr_int = session.query(Attribute).filter_by(name="INT").first()
attr_str = session.query(Attribute).filter_by(name="STR").first()
attr_san = session.query(Attribute).filter_by(name="SAN").first()
attr_wis = session.query(Attribute).filter_by(name="WIS").first()
attr_cha = session.query(Attribute).filter_by(name="CHA").first()

# 查詢 QuestLine
ql_academic = session.query(QuestLine).filter_by(name="學業系統").first()
ql_health = session.query(QuestLine).filter_by(name="健康系統").first()
ql_growth = session.query(QuestLine).filter_by(name="自我拓展").first()
ql_club = session.query(QuestLine).filter_by(name="社團").first()
ql_project = session.query(QuestLine).filter_by(name="專案開發").first()

activity_type = [ActivityType(name="工程數學", unit="小時",base_exp_per_unit=10, quest_line_id=ql_academic.id, attribute_id=attr_int.id),
                 ActivityType(name="電子學", unit="小時",base_exp_per_unit=11, quest_line_id=ql_academic.id, attribute_id=attr_int.id),
                 ActivityType(name="電路學", unit="小時",base_exp_per_unit=11, quest_line_id=ql_academic.id, attribute_id=attr_int.id),
                 ActivityType(name="計算機組織", unit="小時",base_exp_per_unit=9, quest_line_id=ql_academic.id, attribute_id=attr_int.id),
                 ActivityType(name="機率與統計", unit="小時",base_exp_per_unit=8, quest_line_id=ql_academic.id, attribute_id=attr_int.id),
                 ActivityType(name="材料科學導論", unit="小時",base_exp_per_unit=7, quest_line_id=ql_academic.id, attribute_id=attr_int.id),
                 ActivityType(name="健身", unit="小時",base_exp_per_unit=12, quest_line_id=ql_health.id, attribute_id=attr_str.id),
                 ActivityType(name="有氧運動", unit="小時",base_exp_per_unit=15, quest_line_id=ql_health.id, attribute_id=attr_str.id),
                 ActivityType(name="情緒調適", unit="次數",base_exp_per_unit=6, quest_line_id=ql_health.id, attribute_id=attr_san.id),
                 ActivityType(name="英文精進", unit="小時",base_exp_per_unit=6, quest_line_id=ql_growth.id, attribute_id=attr_wis.id),
                 ActivityType(name="日文50音", unit="小時",base_exp_per_unit=5, quest_line_id=ql_growth.id, attribute_id=attr_str.id),
                 ActivityType(name="社團活動", unit="小時",base_exp_per_unit=3, quest_line_id=ql_club.id, attribute_id=attr_cha.id),
                 ActivityType(name="專案開發", unit="小時",base_exp_per_unit=8, quest_line_id=ql_project.id, attribute_id=attr_wis.id)]

session.add_all(activity_type)
session.commit()
print("ActivityType 資料新增完成")