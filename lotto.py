from playwright.sync_api import sync_playwright
import pandas as pd
import time


def fetch_lottery_data(year, start_issue, end_issue):
    base_url = "https://www.zhcw.com/kjxx/ssq/kjxq/?kjData={}"
    data = []

    # 使用 Playwright 初始化浏览器
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # 无头模式运行
        page = browser.new_page()

        for issue in range(start_issue, end_issue + 1):
            issue_str = f"{year}{issue:03d}"  # 构建期数，如 2025001
            url = base_url.format(issue_str)
            print(f"Fetching data for issue: {issue_str} from URL: {url}")

            try:
                # 访问页面，自动等待网络空闲状态
                page.goto(url, wait_until="networkidle")

                # 查找红球和蓝球元素
                red_balls = page.query_selector_all("div.kjqQq span")
                blue_ball = page.query_selector("div.kjqHq span")

                # 检查数据是否正确加载
                if len(red_balls) < 6 or not blue_ball:
                    print(f"Failed to parse data for issue {issue_str}")
                    continue

                # 提取红球和蓝球号码
                red_numbers = [ball.inner_text() for ball in red_balls]
                blue_number = blue_ball.inner_text()

                # 将数据存入列表
                data.append({
                    'Red1': red_numbers[0],
                    'Red2': red_numbers[1],
                    'Red3': red_numbers[2],
                    'Red4': red_numbers[3],
                    'Red5': red_numbers[4],
                    'Red6': red_numbers[5],
                    'Blue': blue_number
                })

                # 延时避免被封禁
                time.sleep(1)

            except Exception as err:
                print(f"Error occurred for issue {issue_str}: {err}")

        browser.close()  # 关闭浏览器
    return data


if __name__ == "__main__":
    year = 2025
    start_issue = 1
    end_issue = 22
    lottery_data = fetch_lottery_data(year, start_issue, end_issue)

    if lottery_data:
        df = pd.DataFrame(lottery_data)
        df.to_excel(f'ssq_{year}.xlsx', index=False)  # 保存到 Excel 文件
        df.to_csv(f'ssq_{year}.csv', index=False)  # 保存到 CSV 文件
        print("Lottery data has been saved successfully.")
    else:
        print("No lottery data found.")
