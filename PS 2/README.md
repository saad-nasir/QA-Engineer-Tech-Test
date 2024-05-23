# Solution to Problem Statement 2

## Testcases for Incoming and Outgoing Fund Transfers (Happy Path)
### 1. Incoming Transfer (Valid Account Number)

| Steps      | Expected Result |
| ----------- | ----------- |
|Perform a test fund transfer with a valid account number and all other relevant valid data    | The transfer is successful and the amount is credited to the recipient's account      |


### 2. Outgoing Transfer (Valid Account Number)

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer with a valid account number and all other relevant valid data     | The transfer is successful and the amount is debited from the sender's account       |


## Testcases for Incoming and Outgoing Fund Transfers (Sad Path)

### 1. Incoming Transfer (Invalid Account Number)

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer using invalid account details for the recipient     | The transfer is not successful and an error message is shown      |


### 2. Incoming Transfer (Duplicate Transfer)

| Steps      | Expected Result |
| ----------- | ----------- |
| Verify the behavior when a duplicate transfer is attempted     | The duplicate transfer is detected and rejected       |
 

### 3. Outgoing Transfer (Invalid Amount)

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer by using valid details for the recipient but enter an invalid amount, e.g. exceed the limit of the account      | The transfer should not be executed and an error message should be shown      |


### 4. Outgoing Transfer (Invalid Account Number)

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer by entering invalid details for the recipient      | The transfer should not be executed and an error message should be shown       |


### 5. Outgoing Transfer (Inactive Account)

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer to an account that is no longer active      | The transfer should not be executed and an error message should be shown      |


## Edge Cases


### 1. Transfer Max. Allowed Limit

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer by entering the max. allowed amount    | The transfer should be successfully executed      |

### 2. Transfer with Special Characters in Account Details

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer by adding special characters in the recipient's account details      | The transfer should not be executed and an error message should be shown      |

### 3. Transfer Min. Allowed Limit

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer by entering the min. allowed amount      | The transfer should be successfully executed      |

### 4. Transfer during Maintenance Window

| Steps      | Expected Result |
| ----------- | ----------- |
| Perform a test fund transfer when the system is under scheduled maintenance    | The transfer should not be executed and an error message should be shown      |

## Suggestions for Improvement

1. Strict data quality and validity rules to ensure that invalid data is not processed
2. Test how the system handles varying amounts of load during peak traffic times
3. Identify critical parameters and Service Level Indicators to help set up a dashboard for monitoring the different services and performance of the system. This could further be improved by setting up alerts which fire whenever the system needs human intervention
4. Exhaustive automated and regression test coverage

## Integration into Jenkins Pipeline

1. The following piece of code defines a Jenkins pipeline that includes stages for build, deplpoy and test

    ```
    pipeline {
        agent any
        stages {
            stage('Build') {
                steps {
                    echo 'Building...'
                    // Add build steps here
                }
            }
            stage('Deploy') {
                steps {
                    echo 'Deploying...'
                    // Add deployment steps here
                }
            }
            stage('Test') {
                steps {
                    echo 'Testing...'
                    sh 'pytest tests/ --junitxml=reports/results.xml'
                }
            }
        }
        post {
            always {
                junit 'reports/results.xml'
            }
        }
    }
    ```
2. The test suite can be integrated into the Test stage of the pipeline and pytest could be used for running the tests and generating test reports
3. Use fixtures in pytest to set up and tear down test data before and after each test run
4. Ensure that the pipeline is triggered on code changes
