# convert_excel_to_udid_list
批量处理excel统计的udid生成苹果设备列表

### 使用步骤 (Usage)
##### 1. 使用文件UDID.xlsx统计UDID，设备类型不含mac可统一填写ios(可通过pgyer等三方工具获取设备的UDID)，按照文档格式，请勿修改文件名和表单名。
##### 2. 确保已经安装了 pandas 和 openpyxl 库， 用于处理excel表格。可以使用以下命令进行安装(``已安装可跳过本步骤``):
```
pip install pandas openpyxl
```
##### 3. 确保excel和脚本在同一目录下，执行以下命令:
```
python excel_to_udid_list.py
```
成功后可看到 ，``multiple-device-upload.txt`` 文件就是可以上传
```
➜  convert_excel_to_udid_list git:(main) ✗ python excel_to_udid_list.py
成功将 Excel 文件 'UDID.xlsx' 转换为 TXT 文件 'multiple-device-upload.txt'
```
##### 4.  上传 multiple-device-upload.txt 文件即可大功告成!
![image.png](https://upload-images.jianshu.io/upload_images/3474734-6de93e30166ca650.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### Enjoy your day! 🤪
