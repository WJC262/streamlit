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

# import streamlit as st
# import pandas as pd


# # 读取CSV文件
# csv_file = '2024-05-20T08-18_export.csv'

# # 使用Pandas读取CSV文件
# df = pd.read_csv(csv_file)

# st.title("Export table display")

# # 选择要显示的行
# row_number = st.number_input("Select the line numbers to display", min_value=0, max_value=len(df)-1, value=0, step=1)

# # 获取所选行的数据并转置
# row_data = pd.DataFrame(df.iloc[row_number]).reset_index()
# row_data.columns = ["Column", "Value"]

# # 显示所选行的数据
# st.header(f"Data in line {row_number}")
# st.table(row_data)


# import streamlit as st
# import pandas as pd

# # 读取xlsx文件
# xlsx_file = 'classified_pcr.xlsx'

# # 使用Pandas读取xlsx文件
# df = pd.read_excel(xlsx_file)

# # 删除'Number'列
# if 'Number' in df.columns:
#     df = df.drop(columns=['Number'])

# # 显示原始表格文件
# st.title("PCR Table Display")
# st.header("Complete Table")
# st.dataframe(df)

# # 将PCR Number设置为索引
# df.set_index('PCR Number', inplace=True)

# # 搜索PCR Number并显示对应的那一行表单
# st.header("Search by PCR Number")
# pcr_number = st.text_input("Search PCR Number", value=df.index[0])

# if pcr_number in df.index:
#     row_data = pd.DataFrame(df.loc[pcr_number]).reset_index()
#     row_data.columns = ["Column", "Value"]

#     # 显示所选行的数据
#     st.header(f"Data for PCR Number {pcr_number}")
#     st.table(row_data)
    
#     # “开始评估”按钮
#     if st.button("开始评估"):
#         classification = df.loc[pcr_number, "Classification"]
        
#         if classification == "ssd":
#             A = [
#                 ["ke ding", "dingke@lenovo.com", "PM", 1],
#                 ["xiaotong yang", "yangxt4@lenovo.com", "ODT", 2],
#                 ["xiaojuan kang", "kangxj@lenovo.com", "TPM", 3],
#                 ["Yinyi Ling", "linyy@lenovo.com", "CPU owner", 4]
#             ]
#             st.header("评估结果")
#             st.write("显示 A 列表:")
#             for item in A:
#                 st.write(item)

#         elif classification == "keyboard":
#             B = [
#                 ["knn ding", "dingke@lenovo.com", "PM", 1],
#                 ["xiaotong yang", "yangxt4@lenovo.com", "ODT", 2],
#                 ["xiaojuan kang", "kangxj@lenovo.com", "TPM", 3],
#                 ["Yinyi Ling", "linyy@lenovo.com", "CPU owner", 4]
#             ]
#             st.header("评估结果")
#             st.write("显示 B 列表:")
#             for item in B:
#                 st.write(item)
# else:
#     st.write("PCR Number not found.")


import streamlit as st
import pandas as pd

# 读取xlsx文件
xlsx_file = 'classified_pcr.xlsx'

# 使用Pandas读取xlsx文件
df = pd.read_excel(xlsx_file)

# 显示原始表格文件
st.title("PCR Table Display")
st.header("Complete Table")
st.dataframe(df)

# 设置'Number'列为索引
df.set_index('Number', inplace=True)

# 搜索Number并显示对应的那一行表单
st.header("Search by Number")
number = st.text_input("Search Number", value=str(df.index[0]))

if number.isdigit() and int(number) in df.index:
    number = int(number)
    row_data = pd.DataFrame(df.loc[number]).reset_index()
    row_data.columns = ["Column", "Value"]

    # 显示所选行的数据
    st.header(f"Data for Number {number}")
    st.table(row_data)
    
    # “开始评估”按钮
    if st.button("开始评估"):
        classification = df.loc[number, "Classification"]
        
        if classification == "ssd":
            SSD = [
                ["yuyuan9", "yuyuan9@lenovo.com", "ODT/Planner", 1],
                ["yanghd3", "yanghd@lenovo.com", "TPM", 2],
                ["huagj1", "kangxj@lenovo.com", "BBO", 3],
                ["wuyang10", "wuyang10@lenovo.com", "thermal", 4],
                ["duanlp1", "duanlp1@lenovo.com", "PA", 5],
                ["yanghd3", "yanghd3@lenovo.com", "TPM", 6],
                ["luomz1", "luomz1@lenovo.com", "OPS", 7],
                ["jiajy", "jiajy@lenovo.com", "MFG", 7],
                ["yanghd3", "yanghd3@lenovo.com", "TPM", 8],
                ["yuyuan9", "yuyuan9@lenovo.com", "ODT/Planner", 9]
            ]
            st.header("Evaluation Results")
            st.write("SSD PCR process:")
            for item in SSD:
                st.write(item)

        elif classification == "keyboard":
            keyboard = [
                ["liqi8", "liqi8@lenovo.com", "ODT/Planner", 1],
                ["yanghd3", "yanghd@lenovo.com", "TPM", 2],
                ["dinglm2", "dinglm2@lenovo.com", "BBO", 3],
                ["chenrou1", "chenrou1@lenovo.com", "Preload", 4],
                ["shaoyh", "shaoyh@lenovo.com", "package", 4],
                ["duanlp1", "duanlp1@lenovo.com", "PA", 5],
                ["yanghd3", "luomz1@lenovo.com", "TPM", 6],
                ["jiajy", "jiajy@lenovo.com", "MFG", 7],
                ["luomz1", "luomz1@lenovo.com", "OPS", 7],
                ["yanghd3", "yanghd3@lenovo.com", "TPM", 8],
                ["yuyuan9", "yuyuan9@lenovo.com", "ODT/Planner", 9]
            ]
            st.header("Evaluation Results")
            st.write("keyboard PCR process:")
            for item in keyboard:
                st.write(item)
else:
    st.write("Number not found or invalid.")

