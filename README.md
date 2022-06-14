# Jarvis
![jarvis first look](jarvis.png)
## **Description**
### it is a cloud/container based tool for information gathering and reconnaissance purpose , it is a combination of python automation, cronjobs, docker, apache2 and aws cloud services,it consume little amount of data for single target, it is easy to launch , it will notify you via email about the Attack Status. run on aws ( EC2 , s3 bucket , etc) , it will also push all data to S3 Bucket
![Jarvis image](jarvis2.png)

### Attack can be triger by using web portal of Jarvis

## What it will do 
- subdomain enumeration via many different tools like amass, subfinder, github-subdomain, sublist3r and assetfinder. so you won't miss any subdomain.
- directory brute force for 403 , and 404. check 404 for subdomain takeover.
- give a table for all alive subdomains along with their Status Code and title
- it will give set of urls for open redirect , SSRF , idor , sqli , rce. it uses gau and waybackurls for collecting all urls.
- it will give you a list of url possibly vulnerble for XSS, it also check for the parameter reflection.
- list out all aws s3 bucket linked to the target or used by target for importing any data via GET request , and do check for misconfigured buckets.
- check for s3 buckets for each subdomain, and also list out all the s3bucket names collected from the JS/HTML files.
- list out all web pages which are using WordPress and also do a check for enabled xmlrpc api.
- all the attack data will be stored in an s3 bucket so you can download it whenever you want.

# **Note**
### Currently the email notification is not working, since google has recently disabled access to inbox from less secure application. we are looking for alternative and will update here soon.

## Installation guide 
check this medium blog for the installation guide 
> https://hackpeas.medium.com/jarvis-automated-bug-hunting-tool-reconnaissance-tool-b8071d88ecc5

## How to use
Jarvis uses web portal to handle new attack, to provide current status, and to launch new attack, and to configure/reconfigure credentials
after the setup is done
you need to run start.sh script in the ec2 instance
> $ bash start.sh

![image](https://user-images.githubusercontent.com/60743167/173586053-618bfe6c-6b05-43fe-8713-ee1e50289cbf.png)

and the web page will look like this

![image](https://user-images.githubusercontent.com/60743167/173586811-6472b65a-52ce-4bbc-a18b-c9dad1820a87.png)

From now onwards, everything will be handled on web portal only

#admin tab


