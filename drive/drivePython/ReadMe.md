### Get Started Procedure :
1. Build the dependencies for python virtual env from the requirements.txt
2. Create a client credential with oauth_api as desktop client by following instruction in the [link](https://developers.google.com/workspace/guides/create-credentials#desktop-app)
4. save the client credentials into json file under name env_secrets folder with name "client_secret.json". To set different path use the config.json file and set the variable "client_secret" with that path.
3. use start.py to test the gdrive manager setup. 

### Pending things : 
1. Move config manager class from oauth file and move to helper file.
2. Move helper.py file to helpers folder