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
βλέπουμε και την απάντηση που επιστρέφετε user created επικυρώνοντας την εισαγωγή. Μέσω της εφαρμογής της mongoDB μπορούμε να δούμε την επιτυχή εγγραφη.
![εικόνα](https://user-images.githubusercontent.com/75616736/177609140-34505625-8be9-442f-a165-d562caadfa30.png)

## Function login():
Αφου έχουμε δημιουργίσει χρήση τότε κάνουμε login στο endpoint /login με τα στοιχεία όπως φαινονται παρακάτω:
![εικόνα](https://user-images.githubusercontent.com/75616736/177613180-0aaccc7c-0261-44c6-9686-50a69431eaa2.png)
Αφου κάνουμε login επιστρεφεται και ένα timespamp με την ώρα login.

## Function createNote():
Αφού έχουμε κανει login μπορούμε στο endpoint /createNote να δημιουργήσουμε ένα note με τα στοιχεια όπως φαίνονται παρακατω (υποχρεωτικά title και content):
![εικόνα](https://user-images.githubusercontent.com/75616736/177613616-17a3c61d-b107-409d-afd6-2bbc4cf7f903.png)
Για πολλαπλά κλειδία στέλνουμε τα keys με "," αναμεσα τους και βάζουμε αγκύλες:
![εικόνα](https://user-images.githubusercontent.com/75616736/177613792-a8a9bdb8-f50a-49d6-bd8d-315528b6c5a6.png)

## Function searchNoteTitle():
Αναζήτηση note με βάση τον τίτλο endpoint /searchNote:
![εικόνα](https://user-images.githubusercontent.com/75616736/177614704-29c5c872-b1be-4367-81ab-9730c81f2f37.png)

## Function searchNoteKey():
Εμφανίζει όλα τα notes που περιέχουν ενα συγκεκριμένο key endpoint /searchNoteKey;
![εικόνα](https://user-images.githubusercontent.com/75616736/177614977-c41d23b5-4b6f-4bd1-bb99-f2ba52d213f7.png)
