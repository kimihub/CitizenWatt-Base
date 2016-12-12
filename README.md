# CitizenWatt for Raspberry Pi 3

Adaptations pour fonctionner l'application CitizenWatt sur Raspberry Pi 3.  
_Work in progress_ : https://hackpad.com/DAISEE-Installation-CitizenWatt-sur-RPi3-ooSfcWLcyl8    

## Listes des changements  :
* Installation manuelle des packages (mode debug, le temps de stabiliser)  
  
* Ajout de la compilation du package **citizenwatt-visu**  
  
* Compilation d'une librairie RF24 en remplacement du package **librf24-dev**   
Utilisation de la librairie [TMRh20](https://github.com/TMRh20/RF24)  
documentation : http://tmrh20.github.io/RF24/RPi.html  

* Remplacement du programme **receive.cpp** par **receive.py**  
impact : utilisation de la [version PINE64+ du **process.py**](https://github.com/DAISEE/CitizenWatt-Base-PINE64/blob/master/process.py) (écriture des data dans un fichier log)  
