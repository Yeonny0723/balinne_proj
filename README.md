### Links
  * Demo

  [Balinne e-comerce website](https://www.youtube.com/watch?v=DsCSNfDMI24)

### About Service
This responsive E-commerce website was created for Balinne Corp. 
Unique features of this websites involves...:
- Multi-language provision
- Sending direct email through web browser using Google API
- Social login (Kakao talk API, Naver API, Facebook API)
- Auto address updates on every purchase
- Post address search API

I was in charge of building a website from scratch which involves...
- Write functional & non-functional requirements
- Database design
- Website design (+admin page)
- Server-side development 


### Used tools & libraries
[Server]: Django, [DB]: MySQL, [Cloud]: AWS Elastic beanstalk (hosting), S3 (static file storage)

### About Code
This project follows MTV(Model-Tempalte_View) pattern to make debugging process easier and to enhance reusability. I encountered a few problems during development, and those are the way how did I approach them...

1. There was an issue that the shopping kart gets empty every time user gets redirected to the new page. To solve this problem I used a context processor to remove the repeating view rendering process and set the kart as a local variable. 

2. For users to send emails directly through the browser, users are required to do those bothering processes (go to email setting and turn off the mailing security feature, re-authentication etc...). To remove those redundant steps, I set up two email servers (one - sender, the other - receiver) and configured only the sender server to be able to send an email and connected it to a new custom API which will take user-inputted inquiries and program sender server to send email to receiver server. 

3. To streamline the ordering process, I focused on the address field. If there's no address saved on the database, users are allowed to save their address before making the payment. If there is an address, the user can choose to call an address back and if there are any modifications detected, the modal will pop up confirming users if they want to save a new address or not. 


### Project Plan 
| ![balinne_relational_diagram](https://user-images.githubusercontent.com/70524037/201114136-100f942a-3ab8-4426-9484-e14e4f1e5836.png) | 
|:--:| 
| *Relational Diagram* |

| <img width="1440" alt="Screen Shot 2022-11-10 at 11 14 38 PM" src="https://user-images.githubusercontent.com/70524037/201114759-c4ec270d-b90e-401d-b2a0-23c37ea2276f.png"> | 
|:--:| 
| *Website Mockup* |


### Project Demo

| <img width="300" alt="Screen Shot 2022-11-10 at 11 42 01 PM" src="https://user-images.githubusercontent.com/70524037/201122533-ed28f79d-59f2-4fb8-9043-6d2bf1f6ffe0.png"> <img width="300" alt="Screen Shot 2022-11-10 at 11 43 17 PM" src="https://user-images.githubusercontent.com/70524037/201122628-d852a9d8-8397-4524-bb35-bad655043a43.png"> | 
|:--:| 
| *Home page* |

| <img width="300" alt="Screen Shot 2022-11-10 at 11 43 57 PM" src="https://user-images.githubusercontent.com/70524037/201123079-3e2768af-4e34-4fa7-a1ae-db40c1052c41.png"> <img width="300" alt="Screen Shot 2022-11-10 at 11 45 30 PM" src="https://user-images.githubusercontent.com/70524037/201123143-98de09ba-781b-4270-b0ec-f135ba594352.png"> <img width="300" alt="Screen Shot 2022-11-10 at 11 46 10 PM" src="https://user-images.githubusercontent.com/70524037/201123198-9aed43e5-0fd9-4a62-8e03-e7043ed0bfa9.png"> | 
|:--:| 
| *Email through browser* |

| <img width="300" alt="Screen Shot 2022-11-10 at 11 46 48 PM" src="https://user-images.githubusercontent.com/70524037/201123533-8d556cbc-edd6-4220-9d42-7fe45e62cc27.png"> <img width="300" alt="Screen Shot 2022-11-10 at 11 47 05 PM" src="https://user-images.githubusercontent.com/70524037/201123594-f054c62b-f71b-4070-9d24-2046aaa9e4b9.png"> |
|:--:| 
| *Quick address fill out* |

