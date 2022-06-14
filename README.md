# Jarvis
## **Description**
### it is a cloud/container based tool for information gathering and reconnaissance purpose , it is a combination of python automation, cronjobs, docker, apache2 and aws cloud services,it consume little amount of data for single target, it is easy to launch , it will notify you via email about the Attack Status. run on aws ( EC2 , s3 bucket , etc) , it will also push all data to S3 Bucket

### Attack can be triger by using web portal of Jarvis

## What it will do 
- subdomain enumeration via many different tools like amass, subfinder, github-subdomain, sublist3r and assetfinder. so you won't miss any subdomain.
- directory brute force for 403 , and 404. check 404 for subdomain takeover.
- give a table for all alive subdomains along with their Status Code and title
- it will give set of urls for open redirect , SSRF , idor , sqli , rce. it uses gau and waybackurls for collecting all urls.
- it will give you a list of url possibly vulnerble for XSS, it also check for the parameter reflection.
- list out all aws s3 bucket linked to the target or used by target for importing any data via GET request , and do check for misconfigured buckets.
- list out all web pages which are using WordPress and also do a check for enabled xmlrpc api.
- collect all s3 buckets which are disclosed in any html/js file of the domain.

# **Note**
### Currently the email notification is not working, since google has recently disabled access to inbox from less secure application. we are looking for alternative and will update here soon.

## Installation guide 



> https://drive.google.com/file/d/1nT7cITiK-e9SzxnPhW86oqsfNo3Su-DZ/view


![jarvis](https://user-images.githubusercontent.com/60743167/132139203-5cb535ce-baeb-408e-9ca6-8819df75eb15.png)

