# 双色球数据爬取工具

这是一个使用 Python 编写的双色球彩票数据爬取工具，基于 `playwright` 库从指定网站抓取彩票开奖数据，并将其保存为 Excel 和 CSV 文件。

## 功能

- 爬取指定年份和期数的双色球开奖数据。
- 提取每期数据的6个红球号码和1个蓝球号码。
- 将数据保存为 Excel (`.xlsx`) 和 CSV (`.csv`) 格式。

## 依赖库

- `playwright`：用于模拟浏览器操作和网页数据抓取。
- `pandas`：用于数据处理和保存。
- `time`：用于控制请求间隔，避免被网站限制。

安装依赖：
```bash
pip install playwright pandas
playwright install  # 安装浏览器驱动
