# Jarvis
## **Description**
### it is a cloud based tool for information gathering and reccon purpose , it is a Combination of Python Automation,cronjobs and aws cloud services,it consume little amount of data for single target, it is Easy to Launch , it will notify you via email about the Attack Status. Run on aws (VPC , EC2 , s3 bucket , s3 glacier ...) , it will also push all data to S3 Bucket

### Attack can be triger just by sending an email to Jarvis mail id or by using Jarvis tool

## what it will do 
- subdomain enumeration
- directory brute force for 403 , and 404. check 404 for subdomain takeover.
- give a table for all alive subdomains along with their Status Code and title
- it will give set of urls for open redirect , SSRF , idor , sqli , rce .
- list out all aws s3 bucket linked to the target or used by target for importing any data via GET request , and do check for misconfigured buckets
- list out all web pages which are using WordPress and also do a check for enabled xmlrpc api.

# **Note**
### Currently the source code is not public yet , we are working on it , but you can look at below preview video 

https://drive.google.com/file/d/1nT7cITiK-e9SzxnPhW86oqsfNo3Su-DZ/view

![jarvis](https://user-images.githubusercontent.com/60743167/132139203-5cb535ce-baeb-408e-9ca6-8819df75eb15.png)

