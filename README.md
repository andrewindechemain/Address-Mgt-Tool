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
<h1> Description</h1>
<p>The Aim of the project is to build a Django REST framework for an IP Management tool that manages and allocates IP Addresses to customers, Tracks unused and used IPs and Ensures proper allocation of IPs without conflict</p>

<!-- Getting Started -->
<b>Getting Started</b>
<p>To get a copy of the project up and running on your local machine for development and testing purposes.</p> 

## Clone the project from Github on terminal. 
<p>HTTPS: git clone https://AndrewIndeche@bitbucket.org/syokinet-technical-assessment/ip-address-management-tool.git</p>

<b>Create a virtual environment for your folder.</b>
<p>pipenv shell</p>

<!-- Installation -->
### <h2>Installation</h2>
Pipenv Install <package>
  <br>Pipenv Install requirements.txt
<!-- Run Locally -->
### <h2> Running Locally</h2>
  docker compose up [OPTIONS] [SERVICE...]

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

**Andrew Indeche** - *Final work* 