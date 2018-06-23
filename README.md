# Simple steps to deploy app in Google Cloud 

Please follow the following instructions to create and deploy your first google cloud application. 

## Account and other basic Steps
1. Please log in to google via your <a href="https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin">google account, </a> or if you dont have an google account create one <a href="https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp">here</a> 

2. Go to <a href="https://cloud.google.com">google cloud's website</a>
3. Go to ![Console](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/1.PNG)
4. Accept the license 

  
![aggreement](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/2.PNG)  
5. Select project ![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/3.PNG)    <br/
  
  
6. Select New Project    

  
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/4.PNG)  

7. Select a project name  


![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/5.PNG)  


8. Select the project you just created    

![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/18.PNG)    


## Final steps

9. Now you should have the dashboard. From there select the terminal (highlighted with a red circle) and and select "start cloud shell"   


![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/6.PNG)

10. use the fllowing code the clone the demo codes from github.
 #### git clone https://github.com/farshidrayhanuiu/cloud_computing.git
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/27.PNG)

11. go to that directory 
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/8.PNG)

12. Now we need to install the prerequisites. To do that type the following codes  
#### pip install -t lib -r requirements.txt
13. Then we need to initialize the enviourment with 
#### gcloud init  





14. Follow these instructions 

  
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/14.PNG)
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/15.PNG)
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/16.PNG)


15. Finally now we are going to deploy the app using the command
#### gcloud app deploy

16. and we are going to follow these instructions


![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/9.PNG)  

![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/10.PNG)
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/11.PNG)
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/12.PNG)



17. And we are done ! run the last command to deploy the app via a weblink
#### gcloud app browse

18. Clink on the link to see the webpage 
  
  
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/17.PNG)

19. Output  

  
  
  
![a](https://raw.githubusercontent.com/farshidrayhanuiu/cloud_computing/master/misc/19.PNG)




  



