from selenium import webdriver

def print_company_info(driver):
    # 企業情報を取得してプリントする
    company_name_list = driver.find_elements_by_css_selector('.blog-item > div.post-metax > h3 > a')

    for company in company_name_list:
        name = company.text
        num = company_name_list.index(company)
        url = company.get_attribute('href')

        print(name + ',' + url)

def main():
    ## Seleniumでnoteからデータを取得する処理
    driver = webdriver.Chrome()

    # 一覧画面に遷移
    driver.get("http://maizuru-kigyou-job.net/guide/")

    print_company_info(driver)

    driver.quit()

if __name__  == '__main__':
    main()
