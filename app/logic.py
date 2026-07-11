from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Attribute, ActivityType, Record
from datetime import datetime

engine = create_engine("sqlite:///rpg.db")
Session = sessionmaker(bind=engine)
session = Session()

# 新增活動紀錄
def add_record(activity_type_name, amount, efficiency, note=None):
    activity = session.query(ActivityType).filter_by(name=activity_type_name).first()
    exp_gained = amount * activity.base_exp_per_unit * efficiency
    attribute = session.query(Attribute).filter_by(id=activity.attribute_id).first()
    attribute.current_exp += exp_gained

    # 升級判斷
    base_exp = 100
    growth_factor = 1.5
    exp_needed = base_exp * (attribute.level ** growth_factor)
    while attribute.current_exp >= exp_needed:
        attribute.level += 1
        attribute.current_exp -= exp_needed
        exp_needed = base_exp * (attribute.level ** growth_factor)
    
    new_record = Record(date=datetime.now().date(),
                        activity_type_id=activity.id,
                        amount=amount,
                        efficiency=efficiency,
                        note=note)
    session.add(new_record)
    session.commit()
    return exp_gained

# 取得所有屬性狀態
def get_all_attributes():
    attributes = session.query(Attribute).all()
    result = []
    for attr in attributes:
        exp_needed = 100 * (attr.level ** 1.5)
        result.append({"name": attr.name,
                       "display_name": attr.display_name,
                       "level": attr.level,
                       "current_exp": attr.current_exp,
                       "exp_needed": exp_needed})
    return result

# 取得近期的活動紀錄
def get_recent_records(limit):
    records = session.query(Record).order_by(Record.date.desc()).limit(limit).all()
    result = []
    for record in records:
        activity = session.query(ActivityType).filter_by(id=record.activity_type_id).first()
        result.append({"date": record.date,
                      "activity_name": activity.name,
                      "amount": record.amount,
                      "efficiency": record.efficiency,
                      "note": record.note})
    return result

# 查詢該活動名稱的資料
def get_activity_by_name(name):
    activity = session.query(ActivityType).filter_by(name=name).first()
    return activity                           

if __name__ == "__main__":
    exp = add_record("工程數學", 2, 1.0)
    print(f"這次獲得 {exp} 經驗值")

    all_attrs = get_all_attributes()
    for attr in all_attrs:
        print(attr)

    print("---")

    recent = get_recent_records(5)
    for r in recent:
        print(r)

