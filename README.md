# SOLANA-Based-CrowdFunding-System
The project is Crowdfunding System based on Blockchain (Decentralized) which performs the task of donating using SOLANA [Phantom wallet]. It is called “DonaMate” &amp; it is a web based application which uses WEB3 Technology and is more safe and secure.

Crowdfunding is a decentralized application based on Ethereum blockchain platform that allows users to invest money to the campaigns that interest them. By using blockchain, we can make sure that the investors engage in low-risk support of new ventures and venture creators can gain more supporters globally making it easy for them to raise large amount of funds in minimal time. Especially in blockchain world at present, there are lot of projects created by individuals or small-distributed teams that want to raise funds by issuing tokens to the investors. Crowdfunding platform simplifies the whole idea of raising capital with help of global public that might be interested in the campaign for an incentive that is profitable to the investor.


# Problem statement
A blockchain-based crowdfunding system is a platform that uses blockchain technology to facilitate the process of raising funds for a project or venture through small contributions from a large number of people.

The problem that such a system aims to solve is the need for a more efficient and secure way to raise funds for projects and startups. Traditional crowdfunding platforms can be subject to fraud and lack of transparency, as there is often no way to verify the identity of the project creator or the use of funds.

Additionally, traditional platforms also charge high fees, which can make it difficult for smaller projects to raise enough money to be successful.

A blockchain-based crowdfunding system can address these issues by using the transparency and immutability of the blockchain to provide a secure and transparent way for project creators to raise funds. 

In summary, a blockchain-based crowdfunding system aims to solve the issues of security, transparency and high fees that traditional crowdfunding platforms face.

## Tech stack 
FRONTEND:
- HTML
- CSS
- JS
- BOOTSTRAP

BACKEND: 
- DJANGO ( web development framework )
- PYTHON ( backend programming language )
- Sqlite3 ( Django database )
- Ganache (Truffle Suite framework).
- WEB3

## TO CLONE THIS PROJECT
To clone this project run

```bash
https://github.com/aniketsh22/SOLANA-Based-CrowdFunding-System.git
```

## TO RUN LOCALLY
After cloning, for running the cloned project go to the project folder / path where the manage.py file is located and then run the following commands into the command prompt:
### First making migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Creating superuser for accessing the database:
After running the following command, create one superuser by adding username, password
```bash
python manage.py createsuperuser
```
### Running the project on the local host:
```bash
python manage.py runserver
```
<img width="527" alt="image" src="https://user-images.githubusercontent.com/89505839/224913817-6fa4a461-b528-4a60-bb5a-a0f8e9a4e1a6.png">

### If you face difficulty in creating superuser try with this old database credentials

USERNAME: crowdfunding
PASSWORD: crowdfunding@123

## FOR ACCESSING ADMIN PANEL
```bash
http://127.0.0.1:8000/admin
```
Enter username and paswword, which you have made while creating superuser. To get access to the database.
<img width="806" alt="saversadmin" src="https://user-images.githubusercontent.com/89505839/211482412-d096ed28-0491-4500-a07f-d063a4fa6d32.png">


# NOTE:
If css is giving error even if properly linked (Go to chrome > settings > clear cache)
<img width="701" alt="savers1" src="https://user-images.githubusercontent.com/89505839/170664313-81deb74f-0ff2-4e48-883c-b18e1babfafe.png">
