# CitizenWatt for Raspberry Pi 3

Adaptations pour fonctionner l'application CitizenWatt sur Raspberry Pi 3.  
_Work in progress_ : https://hackpad.com/DAISEE-Installation-CitizenWatt-sur-RPi3-ooSfcWLcyl8    

## Listes des changements  :
* Installation manuelle des packages (mode debug, le temps de stabiliser)  
  
* Flags dans les fichiers Makefile  
`CCFLAGS=-Wall -Ofast -mfpu=neon-vfpv4 -mfloat-abi=hard -march=armv7-a -mtune=cortex-a7`  
au lieu de  
`CCFLAGS=-Wall -Ofast -mfpu=vfp -mfloat-abi=hard -march=armv6zk -mtune=arm1176jzf-s`  
  
* Compilation du package citizenwatt-visu  
  
* Compilation d'une librairie RF24 en remplacement du package librf24-dev  
