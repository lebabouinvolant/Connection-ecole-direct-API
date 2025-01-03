# Connection-ecole-direct
Un petit programme en python pour faciliter la connection par API vers école direct (parce que franchement c'est une purge)
## Présentation
Le projet se présente sous la forme de 2 script, le script de connection marchant en totale indépendance de l'autre qui donne quant-à-lui un exemple d'utilisation de la connection. En effet, il vous permet de vous connecter via une interface graphique et de calculer votre moyenne pour un trimestre sélectionné et de l'afficher. De plus, le script de connection contient une fonction pour obtenir toutes les notes, cette fonction peut d'ailleurs être déclinée pour obtenir d'autres infos, vous pouvez pour cela regarder cette doc: https://github.com/EduWireApps/ecoledirecte-api-docs
## Dépendances
Pour utiliser ce projet, vous aurez besoin d'une version récente de python (une version 3 devrait suffire), des bibliothèques de bases incluses et de customtkinter (en gros tkinter en plus beau) pour le script des moyennes. Pour installer tkinter, il faut utiliser le pip suivant:
```
pip install customtkinter
```
## Note
- Le fait qu'il y ait 2 fonctions pour se connecter à école direct est dû à leur système de QCM, la première question renvoie donc la liste des questions et vous devez renvoyer la version encodée en base 64 de la bonne réponse à la fonction ConnectToEDPart2 (comme fait dans le programme moyenne)
