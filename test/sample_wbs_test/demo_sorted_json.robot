*** Settings ***
Documentation
Library    ../../src/fetch_webservice.py
Library    ../../src/json_lib.py
Library    ../../src/get_file_lib.py
Library    OperatingSystem
Resource   ../../src/globalVariables.robot

*** Variables ***
${expected_file}   ${CURDIR}\\output\\expected_output_full_json.json
${carrier}  MH
${number}  1338
${departure_date}  2018-03-22

*** Keywords ***
Initialize Template
    Set File In Folder   ${expected_file}

*** Test Cases ***
| Get Flight Test case 1
| | [Documentation]
| | ... | = Test Condition =
| | ... | Provide some test condition
| | ... | = Test data =
| | ... | Test data
| | ... | = Test step number =
| | ... | == Step 1 ==
| | ... | Test steps
| | ... | == Step 2 ==
| | ... | ....
| | ... | == Expected Result ==
| | ... | Verify

    [Timeout]   200

    ${actual}=  request wbs sorted json  ${GETFLIGHT_ENDPOINT}carrierCode=${carrier}&flightNumber=${number}&flightDate=${departure_date}

    ${expected}=  get file sorted json   ${expected_file}
    Should Be Equal   ${actual}   ${expected}
