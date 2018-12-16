*** Settings ***
Documentation
Library    ../../src/random_generators.py

*** Variables ***
${rloc}=  generate_random_record_locator
${id}=  generate_random_id
${ticket_number}=   generate_random_ticket_number

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

    Log   ${rloc}
    Log   ${id}
    Log   ${ticket_number}
