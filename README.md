## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Application view](#application-view)

### General info
<details>
<summary>Click here to see information about <b>Cipher</b></summary>
Application is called Cipher. It's command application which encrypts and decrypts user's words. It uses Caesar cipher 
ROT13 and ROT47. Encrypted or decrypted words could be saved to or loaded from json file. The Cipher used pattern 
desings - CipherManager as facade and abstract factory of ciphers - CipherROT13 and CipherROT47.
</details>

### Technologies / Tools
* Pytest
* Python 3.10
* pre-commit
### Setup
* Clone the repo `git clone https://github.com/krzycze4/cipher.git`
* Inside the project directory create new venv using `python -m venv venv` command
* Next enter the virtual environment using `source ./venv/bin/activate` for mac/linux and `./venv/Scripts/activate` 
for windows based machines
* Install all dependencies using `pip install -r requirements.txt` command. 
* To run application you should execute `main.py` module
### Application view
![app_view.png](app_view.png)
### Sources
This app is inspired by Devs-Mentoring.pl