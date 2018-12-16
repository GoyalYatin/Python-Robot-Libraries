*** Settings ***
Documentation
Library    ../../src/fetch_webservice.py
Library    ../../src/get_file_lib.py
Library    ../../src/subset_selection.py
Library    OperatingSystem
Library   Collections
Library   RequestsLibrary
Resource   ../../src/globalVariables.robot

*** Variables ***
${expected_file}   ${CURDIR}\\output\\expected_output_subset.json
${expected_file_full_json}   ${CURDIR}\\output\\expected_output_full_json.json
${expected_file_statuscode}   ${CURDIR}\\output\\expected_output_statusCode.json
${carrier}  MH
${number}  1338
${departure_date}  2018-03-22

*** Keywords ***
Initialize Template
    Set File In Folder   ${expected_file}
    Set File In Folder   ${expected_file_full_json}
    Set File In Folder   ${expected_file_statuscode}

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

    ${actual}=  request wbs  ${GETFLIGHT_ENDPOINT}carrierCode=${carrier}&flightNumber=${number}&flightDate=${departure_date}
    ${actual1}=  To Json   ${actual}

    ${expected}=  get file from path   ${expected_file}
    ${expected1}=  To Json   ${expected}

    ${expected_full_json}=  get file from path   ${expected_file_full_json}
    ${expected_full_json1}=  To Json   ${expected_full_json}

    ${expected_statusCode}=  get file from path   ${expected_file_statuscode}
    ${expected_statusCode1}=  To Json   ${expected_statusCode}

    Should Be Equal   ${actual1["statusCode"]}   200
    Should Be Equal   ${actual1["data"]["legs"][0]["boardpoint"]}   KUL
    Should Be Equal   ${actual1}   ${expected_full_json1}
    is subset    ${actual1}   ${expected_full_json1}
    is subset    ${expected1}   ${actual1}
    is subset    ${expected_statusCode1}   ${actual1}

