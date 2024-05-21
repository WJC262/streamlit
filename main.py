# import streamlit as st
# import pandas as pd
#
# st.write("""
# # My First App
# Hello world!""")

import streamlit as st
import pandas as pd

# 读取Excel文件
# excel_file = '2024-05-20T08-18_export.csv'
# sheet_name = 'Sheet1'  # 根据你的实际情况更改
#
# # 使用Pandas读取Excel文件
# df = pd.read_csv(excel_file)
#
# # Streamlit应用
# st.title("Excel表格展示")
#
# # 显示表头
# st.header("表头")
# st.write(df.columns.tolist())
#
# # 选择要显示的行
# row_number = st.number_input("选择要显示的行号", min_value=0, max_value=len(df)-1, value=0, step=1)
#
# # 显示所选行的数据
# st.header(f"第{row_number}行的数据")
# st.write(df.iloc[row_number])

import streamlit as st
import pandas as pd


# 读取CSV文件
csv_file = '2024-05-20T08-18_export.csv'

# 使用Pandas读取CSV文件
df = pd.read_csv(csv_file)

st.title("Export table display")

# 选择要显示的行
row_number = st.number_input("Select the line numbers to display", min_value=0, max_value=len(df)-1, value=0, step=1)

# 获取所选行的数据并转置
row_data = pd.DataFrame(df.iloc[row_number]).reset_index()
row_data.columns = ["Column", "Value"]

# 显示所选行的数据
st.header(f"Data in line {row_number}")
st.table(row_data)


