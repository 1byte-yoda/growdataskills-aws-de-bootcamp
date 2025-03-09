## Screenshots
### Lambda Permissions
![permissions](https://github.com/1byte-yoda/growdataskills-aws-de-bootcamp/blob/master/assignments/module_1/screenshots/lambda_permissions.png)
### Lambda Role Attached
![role](https://github.com/1byte-yoda/growdataskills-aws-de-bootcamp/blob/master/assignments/module_1/screenshots/lambda_role_attached.png)
### Lambda Trigger Configuration
![role](https://github.com/1byte-yoda/growdataskills-aws-de-bootcamp/blob/master/assignments/module_1/screenshots/lambda_s3_trigger.png)
### CloudWatch Logs for file larger than 100mb
![role](https://github.com/1byte-yoda/growdataskills-aws-de-bootcamp/blob/master/assignments/module_1/screenshots/gt_100mb.png)
### CloudWatch Logs for file smaller than 100mb
![role](https://github.com/1byte-yoda/growdataskills-aws-de-bootcamp/blob/master/assignments/module_1/screenshots/less_100mb.png)

## Architecture
- This assignment involves the usage of AWS S3 to trigger a lambda function. The main goal is to parse the file size from the S3 object creation event and pass it as
an argument to the lambda function, and log a message to AWS CloudWatch if the object's file size is greater than 100mb.

## Execution Steps
1. Upload a file to S3 bucket with more than 100MB file size
2. S3 Bucket Will perform a POST request and the response will be sent to the Lambda Function
3. Lambda Function will then receive the POST response as a JSON of events
4. To access the file name and file size, it will navigate the JSON object like so: `events["Records"]["s3"]["object"]["key"] / events["Records"]["s3"]["object"]["size"]`
5. Then it will compare the S3 Object's file size to 10**8, if larger, then log a message.
6. Logs can be found in AWS CloudWatch

## Challenges Faced
- The default logging module for python does not work with the default configurations. By reading the [lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html#python-logging-lib), the logger level must be set to INFO for it to work. 