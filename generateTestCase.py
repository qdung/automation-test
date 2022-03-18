from numpy import number
import pandas

header = pandas.read_excel(
    'Testcase_ZenS.xlsx', sheet_name='Integration test', skiprows=1)
testcaseInfo = pandas.read_excel(
    'Testcase_ZenS.xlsx', sheet_name='Integration test', skiprows=7)

footer = "  driver.close()\n\nexcept Exception as e: print(e)\n" + "#End of file\n"

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
actionId = testcaseInfo.get('Id')

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


def getTestCaseRange(testcaseId: number):
    previousBreakCount = 0
    lastBreakCount = 0

    previousIndex = 0
    lastIndex = 0

    for index, description in enumerate(testcaseDescriptions):
        if(description == '-'):
            if(testcaseId == previousBreakCount + 1):
                previousIndex = index+1
            previousBreakCount += 1

            if(testcaseId == lastBreakCount):
                lastIndex = index+1
            lastBreakCount += 1
    return (previousIndex, lastIndex - 1)


def generateBodyTestCase(_from, _to):
    _try = "try: \n"
    body = ''

    for row in range(_from, _to):
        description = "  # Step {}:\n".format(testcaseDescriptions[row])
        step = "  action{} = ".format(actionId[row]) + \
            str(mapActionToSeleniumCore(
                action[row], xPath[row], testData[row])) + "\n"
        wait = "  driver.implicitly_wait({})\n".format(
            implicitlyWaitTiming)
        body += (description + step + wait)
    return (_try + body)


for index, tcId in enumerate(testcaseID):
    if(str(tcId).isnumeric()):
        (_from, _to) = getTestCaseRange(tcId - 1)
        print('Testcase {} range: {} -> {}'.format(tcId, _from, _to - 1))
        tcName = "\n\n# Testcase name: {}\n\n".format(testcaseName[index])
        body = generateBodyTestCase(_from, _to)

        tcDetail = header + tcName + body + footer
        fileScript = open("./script/testcase_{}.py".format(tcId), "w")
        fileScript.write(tcDetail)
        fileScript.close()
