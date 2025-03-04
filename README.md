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
使用方法
准备环境

确保已安装 Python 3.x，并通过上述命令安装依赖库。

修改参数

在代码的 if __name__ == "__main__": 部分，设置以下变量：

year：目标年份（如 2025）。
start_issue：起始期数（如 1）。
end_issue：结束期数（如 22）。
运行程序

在终端执行：

bash
python lotto.py
程序将自动抓取数据并保存为 ssq_{year}.xlsx 和 ssq_{year}.csv 文件。


注意事项
网络延迟：程序在每次请求后会暂停 1 秒（time.sleep(1)），避免触发网站的反爬机制。
错误处理：如果某期数据抓取失败，会打印错误信息并跳过该期。
数据验证：确保页面加载正确（红球不少于6个，蓝球存在），否则跳过。
输出文件
ssq_{year}.xlsx：Excel 格式的彩票数据。
ssq_{year}.csv：CSV 格式的彩票数据。
每行数据格式：

Red1, Red2, Red3, Red4, Red5, Red6, Blue
示例
运行以下配置：

python
year = 2025
start_issue = 1
end_issue = 3
程序将抓取 2025 年第 001 期至 003 期的数据，并生成 ssq_2025.xlsx 和 ssq_2025.csv。

法律声明
本工具仅用于学习和研究目的，请遵守相关法律法规及目标网站的robots.txt协议。用户需自行承担使用本工具所带来的法律责任。

问题反馈
如遇到问题，请检查网络连接、依赖安装，或联系开发者WX：scriptalert1script。
