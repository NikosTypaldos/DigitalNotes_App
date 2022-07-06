# DigitalNotes_App

## Install

Για την εκτέλεση του Project απαιτούνται τα παρακάτω libraries της Python:

   * Pymongo
   * Flask
   * json
   * uuid
   * bson.json_util
   * bson import ObjectId
   * time
   
## Λειτουργία εφαρμογής
    
    *Δημιουργία ενός docker image που συνδέεται με ένα container της MongoDB , εισαγωγή της βάσης δεδομένων InfoSys που περιέχει τα collections "Clients" ,         "Notes" στο image.
    *Εκκίνηση του Docker Image/container , εισαγωγή του κώδικα σε ενα code Editor με την ονομασία app.py εκκίνηση του κώδικα με την επιλογή Flask run
    
## WebService
Σε όλα τα function του προγράμματος πλήν createUser γίνεται έλεγχος μέσω uuid το οποίο δημιουργείτε αυτόματα

## Function create_user():
Για να κάνουμε νέο χρήστη στέλνουμε ένα request (πχ μεσω Postman) και εισάγουμε τα πεδία username, email, fullname, password και ταυτοχρονα δημιουργείται και ενα στοιχείο και άλλο ενα πεδίο category με τιμη user το οποίο χρησιμοποιώ για τον έλεγχο των δικαιωμάτων παρακάτω screeshot επιτυχούς POST request μεσω postman.
![εικόνα](https://user-images.githubusercontent.com/75616736/177608652-7fe6813b-2430-4b62-8cf2-a77d23d59ca6.png)

