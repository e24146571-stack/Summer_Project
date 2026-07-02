from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# 屬性: INT, STR, SAN, WIS, CHA
class Attribute(Base):
    __tablename__ = "attributes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) # ex: INT
    display_name = Column(String, nullable=False)
    current_exp = Column(Integer, default=0)
    level = Column(Integer, default=1)

# 主線/副線
class QuestLine(Base):
    __tablename__ = "quest_lines"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) # ex: 學業系統
    type = Column(String, nullable=False) # 主/副線

# 具體活動
class ActivityType(Base):
    __tablename__ = "activity_types"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) # ex: 工數
    unit = Column(String, nullable=False) # ex: hr
    base_exp_per_unit = Column(Float, nullable=False) # 每單位基礎經驗值

    quest_line_id = Column(Integer, ForeignKey("quest_lines.id"))
    attribute_id = Column(Integer, ForeignKey("attributes.id"))

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    activity_type_id = Column(Integer, ForeignKey("activity_types.id"))
    amount = Column(Float, nullable=False) # 時數or次數
    efficiency = Column(Float, default=1.0) # 0.25~1.25
    note = Column(String, nullable=True) # 備註，可留空

if __name__ == "__main__":
    engine = create_engine("sqlite:///rpg.db")
    Base.metadata.create_all(engine)
    print("資料庫建立成功")