<!--
The Readme file documents the project description and installation and set up instructions
-->
<!--
Align main heading to the center of the page
-->
| Tool                | Description                    | Tags for tools used                                                                                               |
| ------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------- |
| 1.Git                  | Version Control | [Version-Control];[Bitbucket]; [Repo];                                                         |
| 2.Django               | Python-Based Framework| [Python]; [Production];[Development];|
| 3.Django Rest Framework| API Toolkit| [API]; [REST Framework];|
| 4.PyLint               | Linter   | [static]; [analyzer];|
| 5.Pipenv               | Packaging & Virtual Environment Tool| [VirtualEnv]; [Dependency Management];|
| 6.Pytest/Unit test     | Testing framework| [Test]; [Test Cases];|
| 7.Docker               | Virtualization Deployment of software in Containers | [Virtualization];|
| 8.MySQL                | Relational Database Management | [Database]; [Relational Database];|
| 9.Heroku               | Cloud Deployment Platform | [Platform As a Service] ; [Cloud];| 
| 10.Swagger             | API Design & Documentation | [Open API] ; [Design] ; |


<div align="left">

<h1>Python Django Documentation</h1> 

<p>The ReadME documents details about configuring a Python Django Project</p>

<!-- Badges -->
## <h1> Description</h1>
<p>The Aim of the project is to build a Django REST framework for an IP Management tool that manages and allocates IP Addresses to customers, Tracks unused and used IPs and Ensures proper allocation of IPs without conflict</p>

<!-- Getting Started -->
## <h2><b>Getting Started</b></h2>
<p>To get a copy of the project up and running on your local machine for development and testing purposes.</p> 

<b><p>HTTPS: git clone https://AndrewIndeche@bitbucket.org/syokinet-technical-assessment/ip-address-management-tool.git</p></b>

## <h3>2.Create a virtual environment for your folder.</h3>
<b><p>pipenv shell</p></b>

<!-- Installation -->
## <h3>3.Installation</h3>
<b>1.Use Pipenv Install <package> to install
  2.else Pipenv Install requirements.txt </b>

 <!-- Create .env --> 
 ## <h3>4.Create a .env file</h3>
    <b>1.Create a .env file on the root
       2.add environment variables
       3.Use env.example to configure your env variables</b>
<!-- Run Locally -->
## <h3> Running Locally</h3>
   <b>MySQL</b>
      1. Use MYSQL installer from https://dev.mysql.com/downloads/installer/ to install 
      (a) MySql server for configuring server and user/DB variables and (b) MySql Workbench to manage database and user.
    <b>Docker</b>
      1. Install docker to create a virtualized container that will be used to run the python app
       Run docker using: <b>docker compose up [OPTIONS] [SERVICE...]</b>

<!-- Going into the project Directory/Folder -->
<h2>Go to the project directory</h2>

  1.cd ipmgt

<!-- Running Tests on the Application -->
<h2>Running Tests</h2>

  1. pytest
  2. python3 manage.py test

<!-- Linting the Application -->
<h2>Linting the App</h2>
 1.pylint pylint_example.py.

<br>
## <h2>Authors</h2>

<b>Andrew Indeche - *Final work* </b> 