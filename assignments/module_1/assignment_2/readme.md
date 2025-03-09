## Log Screenshots
### Test 1
![test1](https://github.com/1byte-yoda/growdataskills-aws-de-bootcamp/blob/master/assignments/module_1/assignment_2/screenshots/test1.png)
### Test 2
![test2](https://github.com/1byte-yoda/growdataskills-aws-de-bootcamp/blob/master/assignments/module_1/assignment_2/screenshots/test2.png)
### Test 3
![test3](https://github.com/1byte-yoda/growdataskills-aws-de-bootcamp/blob/master/assignments/module_1/assignment_2/screenshots/test3.png)


## Architecture
- This assignment demonstrates how to utilize Lambda Layers to modularize our code and make some functionality reusable across different Lambda Functions. The demo code uses the matrix_utils.py file as the Lambda Layer. 
This Layer has the function transpose_matrix which accepts a 2D array of integer and transposes it.

## Creation and Deployment Steps
1. I created a matrix_utils.py file with the transpose_matrix() function, and I saved it under the `python` folder so Lambda Layers can parse it. 
2. I then zipped the `python` folder, and name it as matrix_utils.zip
3. After that I created a new Layer in Lambda and called it `matrix-transpose-layer`, then upload the matrix_utils.zip file
4. Next, I created a new Lambda function and attached the `matrix-transpose-layer` in the lambda configuration
5. I then imported the transpose_matrix function into my lambda handler script, logging both the input array and transposed array for debugging purposes.
6. Lastly, I deployed and tested the lambda function with various input arrays.
 