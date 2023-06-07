# OCR
Transforme pdf et jpg en format texte brut

Il faut d'abord pip installer les librairies dans les commentaires du haut du code.

Il faut aussi installer pytesseract et ajouter dans le PATH la variable.
Au moment d'installer pytesseract, sélectionner toutes les langues que vous lisez.
Dans le code, préciser la langue d'origine. Ex.: extracted_text = pytesseract.image_to_string(img, lang='frak'). Ce qui implique que j'ai sélectionné Allemand Fraktur au moment de l'installation. On peut aussi après installation ajouter des langues à partir d'ici : https://github.com/tesseract-ocr/tessdata_fast/blob/main/fra.traineddata. Il faut les ajouter dans C:\Program Files\Tesseract-OCR\tessdata

J'ai ajouté une barre de progrès.
