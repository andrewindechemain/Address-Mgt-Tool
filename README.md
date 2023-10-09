<!--The Readme file documents the project description and installation and set up instructions-->
<!--Align main heading to the center of the page-->
| Tool                | Description                    | Tags for tools used                                                                                               |
| ------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------- |
| 1.Git                  | Version Control | [Version-Control]; [Bitbucket]; [Repo];|
| 2.Django               | Python-Based Framework| [Python]; [Production];[Development];|
| 3.Django Rest Framework| API Toolkit| [API]; [REST Framework];|
| 4.PyLint/PyLance       | Linter   | [static]; [analyzer];|
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
<p>The Aim of the project is to build a Django REST framework for an IP Management tool that manages and allocates IP Addresses to customers, Tracks unused and used IPs and Ensures proper allocation of IPs without conflict and has a IP subnet calculator tool, which takes an IP and a subnet mask and returns details like the network address, broadcast address, and usable IP range.</p>

<!-- Getting Started -->
## <h2><b>Getting Started</b></h2>
<p>To get a copy of the project up and running on your local machine for development and testing purposes.</p> 
<ul>
<li>Clone and start the Django Application in a Dockerized container</li>
                                    or
<li>Clone and set up the Django Application in a virtual environment </li>
</ul>

## <h2>Swagger End Points</h2>
<b>NB:USE DJANGO ADMIN TO CREATE IP AND CUSTOMER OBJECTS</b>
<p>Swagger UI has been used to document the End Points of the Project on a Front End.</p> 
<p><b> Swagger End Points</b></p>
<ul>
 <li><p>Allocate IP Address</p><b>POST:</b> /Allocate IP Address/{customer_id}/{email}/{name}/</li>
 <li><p>List Allocated IPs</p><b>GET:</b> /List Allocated IPs></li>
 <li><p>List Available IPs</p><b>GET:</b> /List Available IPs</li></li>
 <li><p>Release IP Address</p><b>PUT:</b> /Release IP Address/{Address}/</li></li>
 <li><p>Subnet Calculator</p><b>PUT:</b> /Subnet Calculator/{ip}/{mask}</li>
</ul>

## <h3>Starting Project in a Dockerized Environment</h3>
<p>Use https://docs.docker.com/engine/install/ubuntu/ for instructions on installing and configuring docker.</p>
    1.Install docker to create a virtualized container that will be used to run the python app
    2.Run the docker deamon service. Open docker app on supported os.
    3.Building container: docker build -t {app-name} .
    4.Running the container: docker-compose up .
    5.Run docker using: docker login -u username -p password for password protected container

## <h3>Starting Project in a Python Virtual Environment</h3>

<p><b>1.Clone the Project from GIT Repository.</b></p>
  1.HTTPS cloning: git clone <repo>
  2.SSH cloning: 
  <ul>
  <li>Generate an SSH key pair on your machine, if you donâ€™t have one already. You can use the command ssh-keygen -t rsa -b 4096 -C "your_email@example.com" and follow the prompts. You can also refer to this guide1 for more details.</li>
  <li>Copy the public key to your clipboard. You can use the command pbcopy < ~/.ssh/id_rsa.pub or cat ~/.ssh/id_rsa.pub and copy the output manually.</li>
  <li>Add the SSH key to your Bitbucket account. You can follow this guide2 for the instructions.
  </li>
  </ul>

<p><b>2.Create a virtual environment for your folder.</b></p>
<p>Use the prompt: <b>pipenv shell</b> to start a python Installer Package Environment</p>

<!-- Installation -->
<p><b>3.Installation</b></p>
<ol>
  <li>Use Pipenv Install <package> to install individual packages</li>
                                    or
  <li>Pipenv Install requirements.txt to install a compilation of packages from a requirements.txt</li>
</ol>
 <!-- Create .env --> 
 <p><b>4.Create an .env file</b></p>
      <ol>
       <li>Create an .env file on the root so as to store critical user and database information.</li>
       <li>Add environment variables. for 1.Name 2.User 3.Password 4.Host 5.Port</li>
       <li>Add the .env file to .gitignore.</li>
       <li>Use env.example to configure your env variables</li>
       </ol>
<!-- Run Locally -->

## <h2>Running MySQL Locally</h2>
<p>Use MYSQL installer from https://dev.mysql.com/downloads/installer/ to install:</p>
<ol>
  <li> MySql server for configuring server and user/DB variables</li> and 
  <li> MySql Workbench to manage database and user.</li>
  </ol>
<p>Runing Database</p>
<ol>
<li> Use the command: mysql uroot -p to access database as root user </li>
<li> change default root user password and create other users/Databases,grant permissions</li>
</ol>
<!-- Navigating to the project Directory/Folder -->
<h2>Navigating to the project directory</h2>
<p>Use the command below to navigate to the project folder in terminal:</p>
  <ul>
  <li>cd ipmgt</li>
  </ul>
<!-- Running Tests on the Application -->
<h2>Running Tests</h2>
<p>Use the commands below to carry out test on the models and app functionality.:</p>
  <ul>
  <li>for pytest: pytest test_sample.py</li>
  <li>for unittests:python3 manage.py test</li>
  </ul>
<!-- Linting the Application -->
<h2>Linting the App</h2>
<p>Use the command below to Lint the python syntax for typographical errors.:</p>
<ol>
<li>export DJANGO_SETTINGS_MODULE=address_management.settings</li>
 <li>pylint pylint_example.py.</li>
          or
  <li>pylint --load-plugins pylint_django --rcfile *</li>
 </ol>

## <h2>Authors</h2>
<p style="font-size: 2em; font-weight: bold">Andrew Indeche - *Final work*</p> 