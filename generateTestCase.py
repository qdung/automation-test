from numpy import number
import pandas

header = pandas.read_excel(
    'Testcase_ZenS.xlsx', sheet_name='Integration test', skiprows=1)
testcaseInfo = pandas.read_excel(
    'Testcase_ZenS.xlsx', sheet_name='Integration test', skiprows=7)

dataHash = testcaseInfo.to_dict()

# Config
implicitlyWaitTiming = 10

# Get header excel
website = str(header.loc[0, 'Website'])
width = str(header.loc[0, 'Width'])
height = str(header.loc[0, 'Height'])

# Get testcase information
testcaseID = testcaseInfo.get('TC ID')
testcaseName = testcaseInfo.get('TC name')
testcaseDescriptions = testcaseInfo.get('TC description')
xPath = testcaseInfo.get('Xpath')
testData = testcaseInfo.get('Test data')
action = testcaseInfo.get('Action')

header = open('./template/header.txt', 'r').read()
header = header.replace('CUSTOM_WIDTH', width).replace('CUSTOM_HEIGHT', height)
header = header.replace('WEBSITE_URL', website)


def mapActionToSeleniumCore(action, xpath, value=None, filePng=None):
    if(str(action) == 'Input'):
        return 'driver.find_element(By.XPATH, "{}").send_keys("{}")'.format(xpath, value)

    elif(str(action) == 'Enter'):
        return 'driver.find_element(By.XPATH, "{}").send_keys(Keys.RETURN)'.format(xpath)

    elif(str(action) == 'Click'):
        return 'driver.find_element(By.XPATH, "{}").click()'.format(xpath)

    elif(str(action) == 'Get'):
        return 'print(driver.find_element(By.XPATH, "{}").get_attribute("textContent"))'.format(xpath)

    elif(str(action) == 'Clear'):
        return 'driver.find_element(By.XPATH, "{}").clear()'.format(xpath)

    elif(str(action) == 'Alert OK'):
        return 'Alert(driver).accept()'

    elif(str(action) == 'Alert cancel'):
        return 'Alert(driver).dismiss()'

    elif(str(action) == 'Alert text'):
        return 'Alert(driver).text'
    elif(str(action) == 'Screenshot'):
        return 'driver.get_screenshot_as_file("{}")'.format(filePng)


def generateBodyTestCase(id: number):
    tcName = "\n\n# Testcase name: {}\n\n".format(testcaseName[id])
    _try = "try: \n"
    body = ''
    count = 0
    for index, tcDescription in enumerate(testcaseDescriptions):
        print('Index row: {}'.format(index))
        if(str(tcDescription) == '-'):
            print('tcId: {}'.format(tcId))
            print('Index of "-": {}'.format(index))
            break

        description = "  # Step {}:\n".format(tcDescription)
        step = "  action{} = ".format(index+1) + \
            str(mapActionToSeleniumCore(
                action[index], xPath[index], testData[index])) + "\n"
        wait = "  driver.implicitly_wait({})\n".format(
            implicitlyWaitTiming)
        body += (description + step + wait)
        print('index: {}'.format(index))
        return (tcName + _try + body)


print(testcaseName[1])

for index, tcId in enumerate(testcaseID):
    if(str(tcId).isnumeric()):
        # print(tcId)
        tcDetail = header + generateBodyTestCase(index) + "  driver.close()\n" + \
            "\nexcept Exception as e: print(e)\n" + "#End of file\n"
        fileScript = open("./script/testcase_{}.py".format(tcId), "w")
        fileScript.write(tcDetail)
        fileScript.close()

# tcDetail = header + generateBodyTestCase() + "  driver.close()\n" + \
#     "\nexcept Exception as e: print(e)\n" + "#End of file\n"

# fileScript = open("./script/tc1.py", "w")
# fileScript.write(tcDetail)
# fileScript.close()
