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

<p>The ReadME documents details about configuring a Python Django Project for an IP Management tool</p>

<!-- Badges -->
## <h1> Description</h1>
<p>The Aim of the project is to build a Django REST framework for an IP Management tool that manages and allocates IP Addresses to customers, Tracks unused and used IPs and Ensures proper allocation of IPs without conflict</p>

<!-- Getting Started -->
## <h2><b>Getting Started</b></h2>
<p>To get a copy of the project up and running on your local machine for development and testing purposes.</p> 
<ul>
<li>Clone and start the Django Application in a Dockerized container</li>
<li>Clone and set up the Django Application in a virtual environment </li>
</ul>

## <h3>Starting Project in a Dockerized Environment</h3>
  <b>Docker</b>
      1. Install docker to create a virtualized container that will be used to run the python app
       Run docker using: <b>docker compose up [OPTIONS] [SERVICE...]</b>

## <h3>Starting Project in a Python Virtual Environment</h3>

## <p>1.Clone Project from GIT Repository.</p>
<b><p>HTTPS: git clone https://AndrewIndeche@bitbucket.org/syokinet-technical-assessment/ip-address-management-tool.git</p></b>

## <p>2.Create a virtual environment for your folder.</p>
<p>Use the prompt: <b>pipenv shell</b> to start a python Installer Package Environment</p>

<!-- Installation -->
## <p>3.Installation</p>
<b>1.Use Pipenv Install <package> to install individual packages
  2.else Pipenv Install requirements.txt to install a compilation of packages from a requirements.txt </b>

 <!-- Create .env --> 
 ## <p>4.Create an .env file</p>
    <b>1.Create an .env file on the root so as to store critical user and database information.
       2.add environment variables.
       3.Add the .env file to .gitignore.
       4.Use env.example to configure your env variables</b>
<!-- Run Locally -->
## <p> Running Locally</p>
   <b>MySQL</b>
      1. Use MYSQL installer from https://dev.mysql.com/downloads/installer/ to install 
      (a) MySql server for configuring server and user/DB variables and (b) MySql Workbench to manage database and user.
<!-- Navigating to the project Directory/Folder -->
<h2>Navigating to the project directory</h2>

  1.cd ipmgt
<!-- Running Tests on the Application -->
<h2>Running Tests</h2>
  Use the commands below to carry out test on the models and app functionality.
  1. pytest
  2. python3 manage.py test

<!-- Linting the Application -->
<h2>Linting the App</h2>
Us the command below to Lint the python syntax for typographical errors.
 1.pylint pylint_example.py.
<br>

## <h2>Authors</h2>
<b>Andrew Indeche - *Final work* </b> 