import pandas as pd
from pypinyin import lazy_pinyin

# 定义 Excel 文件路径和工作表名称
excel_file_path = 'UDID.xlsx'
sheet_name = 'UDID'  # 指定要读取的工作表名称

try:
    # 读取 Excel 文件
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    # 交换第一第二两列数据
    df.iloc[:, [0, 1]] = df.iloc[:, [1, 0]].values
    # 将第二列汉字转为拼音
    df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: ''.join(lazy_pinyin(x)))
    # 定义输出 TXT 文件的路径
    txt_file_path = 'multiple-device-upload.txt'

    # 打开 TXT 文件以写入数据
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        # 遍历 DataFrame 的每一行
        line = "Device ID\tDevice Name\tDevice Platform"
        file.write(line + '\n')
        for index, row in df.iterrows():
            if row.isnull().any():
                print(f"第 {index} 行存在空值: {row.values} ")
                continue
            # 将每行数据转换为制表符分隔的字符串
            line = '\t'.join(map(str, row.values))
            # 将处理后的行写入文件，并添加换行符
            file.write(line + '\n')

    print(f"成功将 Excel 文件 '{excel_file_path}' 转换为 TXT 文件 '{txt_file_path}'")

except FileNotFoundError:
    print("文件不存在，请检查路径是否正确。")
except Exception as e:
    print(f"发生错误：{e}")