
# My weather report chatbot
by Charles Chen
# FSM Diagram 
![](https://i.imgur.com/3f6Sscl.png)

# Bonus Feature
## 1. Web crawing
Import beautiful4 extention to crawing [中央氣象局](https://www.cwb.gov.tw/V7/forecast/) website, and get temperature and raining probability of each city.

##### reference
[爬蟲新手](https://pala.tw/python-web-crawler/)
https://cuiqingcai.com/1319.html
http://blog.castman.net/%E6%95%99%E5%AD%B8/2016/12/22/python-data-science-tutorial-3.html

## 2. web driver
Use chrome driver to get elements which can't directly parse by beautifulsoup4. Since those elements are triggered by javascript.

## 3. deploy on heroku
Depoly on heroku to not just run on local

## 4. more messenger functionalities
### a) quick reply message
![](https://i.imgur.com/OTrILMz.png)

### b) button message
![](https://i.imgur.com/EHmKAnP.png)

### c) image message
![](https://i.imgur.com/LwoM8jM.png)

### 5. creative design
sweet reminds and cute picture(長輩圖)
![](https://i.imgur.com/LwoM8jM.png)


# How to run and interact which my chatbot
### 1. input "hi" ot "hello" to call my chatbot, it will ask which region are you in.
![](https://i.imgur.com/9phNH6O.png)


### 2. choose your region(by quick reply), then chatbot will ask which city are you in.
![](https://i.imgur.com/p30Yh1X.png)

### 3 after type in your city, chatbot will ask if you want to know the data of temperature or raining probability.
![](https://i.imgur.com/WeCX2et.png)


### 4.1 after choosing temperature, chatbot will reply today's temperature and sweet reminds.
![](https://i.imgur.com/IkUymcQ.png)


### 4.2 after choosing raining probability, chatbot will reply today's raining probability and sweet reminds.
![](https://i.imgur.com/9foOWn1.png)

### 5 after getting imformation, user have three options
#### 1) continue to search another climate information(go back to step 4)
#### 2) search climate information of another city(go back to state 2)
#### 3) leave chat bot(go to step 6)
![](https://i.imgur.com/uhCaV3Q.png)

### 6 leave chatbot, byebye!
![](https://i.imgur.com/nbIK4FM.png)
