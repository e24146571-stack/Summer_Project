import streamlit as st
from logic import get_all_attributes, get_recent_records, add_record, get_activity_by_name

# 主頁 (角色狀態)
st.title("Summer Project")
st.header("角色狀態")
attributes = get_all_attributes()
for attr in attributes:
    progress = attr["current_exp"] / attr["exp_needed"]
    st.write(f"**{attr['display_name']}** ({attr['name']}) - Lv.{attr['level']}")
    st.progress(progress)
    st.write(f"{attr['current_exp']:.1f} / {attr['exp_needed']:.1f} exp")

# 活動新增
st.header("新增紀錄")
activity_names = ["工程數學", "電子學", "電路學", "計算機組織", "機率與統計", "材料科學導論", "健身", 
                  "有氧運動", "情緒調適", "英文精進", "英文精進", "日文50音", "社團活動", "專案開發"]
selected_activity = st.selectbox("選擇活動", activity_names)
selected_activity_obj = get_activity_by_name(selected_activity)
unit_label = selected_activity_obj.unit
amount = st.number_input(f"{unit_label}", min_value=0.0, max_value=24.0, value=1.0, step=0.5)

# 效率選擇
efficiency_options = {"很差": 0.25,
                      "不佳": 0.5,
                      "普通": 0.75,
                      "不錯": 1.0,
                      "全神貫注": 1.25}
selected_efficiency_label = st.selectbox("效率如何?", list(efficiency_options.keys()))
efficiency = efficiency_options[selected_efficiency_label]

# 送出按鈕
if st.button("送出"):
    exp_gained = add_record(selected_activity, amount, efficiency)
    st.success(f"成功紀錄!獲得 {exp_gained:.1f} 經驗值")
    st.rerun()