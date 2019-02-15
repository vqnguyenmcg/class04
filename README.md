# class04
Class 04

Questions 1&3:
A) Build Docker:
docker build -t vqn_image ./

B) Showing Images:
docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
nvq_image           latest              4cfb487bc162        5 minutes ago       581MB
ubuntu              16.04               7e87e2b3bf7a        3 weeks ago         117MB

C) Runing Dockerfile:
docker run -ti nvq_image

Question 2:
Continuous Integration is an idea in software development where people who are sharing a common repository can integrate and test new or changed code frequently. Each time one person itegrate his/her code is called one integration. Each integration will then be validated by an automated build to detect errors and give feedbacks.

An example of continuous integration platform that can be used with GitHub is Abstruse CI
https://abstruse.bleenco.io

Questions 4&5: 
I used the data set on breast cancer and prepared the script "python_script.py".
To run the code in the terminal: python python_script.py "path_to_data" and in my example, it is in the current folder and hence, python python_script.py breast-cancer-wisconsin.data.txt


