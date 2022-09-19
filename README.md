# Raza-Insurance_Price_prediction_ML_project_02


### Software and account requirements. 

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

##Creating Conda environment
```
conda create -p <environment_name(here venv used)> python==3.7 -y
```
Above -p is prefix if we give -p then same name folder will be created in the current directory and if we give -n then it will be created in conda env.list.


##Activating the virtual environment 
```
conda activate venv/
```  
OR
```
conda activate venv
```
##Installing libraries or requirements.
```
pip install -r requirements.txt
```

To add files to git
```
git add <file_name>
```

OR
```
git add .  (It will add all the files in the current directory)
```


> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the status of git
```
git status
```

To check all the versions maintained by git
```
git log
```

To create version/commmit all changes by git
```
git commit -m "custom message"
```

To send changes/version to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMIAL = tanatif@gmail.com
2. HEROKU_API_KEY = <Enter Heroku API key>
3. HEROKU_APP_NAME = ml-regresion--app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
>Note : Image name for docker must be lowercase

To list docker image
```
docker image
```
To run the  image
```
docker run -p 5000:5000 -e PORT=5000 <IMAGE ID>
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```



TO install all the libraries mentioned  in requirements.txt
```
python setup.py install
```

Install ipykernel
```
pip install ipykernel
```

Hypothesis Testing
```
Here in this project while re-training our model, Hypothesis testing has been used to compare the distribution of the dataset from the old dataset to the new dataset. 

ks_2samp from scipy.stats has been used here for hypothesis testing .
from ks_2samp we will get p value and from that we will get to know our p-test or Null Hypothesis testing.

Null : Two dataset are from same distribution.
Alternate : Two dataset are not from the same distributiion

if p >= 0.5 then we have sufficient proof that null hypothesis is True.
```