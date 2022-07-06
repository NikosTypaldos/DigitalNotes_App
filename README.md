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

## Function updateNote():
Πραγμοτοποιείται η αναζήτηση της σημείωσης και έπειτα αλλαζει τα πεδία που έχουν εισαχθεί απο τον χρήστη endpoint /updateNote. Η αναζήτηση γίνεται με βάση τον τίτλο παράδειγμα:
![εικόνα](https://user-images.githubusercontent.com/75616736/177618052-68f81122-82db-4ac6-860a-6dfa0b23d040.png)
Αλλαγμένο note
![εικόνα](https://user-images.githubusercontent.com/75616736/177618090-f5d24896-aae0-474a-8638-acf721d4fbdc.png)

## Function deleteNote():
Διαγραφή σημειώματος με βάση τον τίτλο endpoint /deleteNote:
![εικόνα](https://user-images.githubusercontent.com/75616736/177618299-9cd155dc-0a03-461e-a857-cc3fdcc974a3.png)
Πηγαίνουμε στην βάση και παρατηρούμε οτι εχει διαγραφεί επιτυχώς:
![εικόνα](https://user-images.githubusercontent.com/75616736/177618379-d3028aee-13a1-4464-8ed8-de324e2c487a.png)

## Function showNotesChronological():
Εμφάνιση όλων των note με χρονολογική σειρά. Για την εκτέλεση παραδείγματος δημιουργώ 3 notes με ονομα noteTitle3, noteTitle4, noteTitle5 με αυτή την σειρά χρονολογικά. Το endpoint /showNotesTime δέχεται σαν είσοδο το πεδίο "order" με τιμές είτε "asc" είτε "desc" με βάση πια σείρα θέλει να δεί τα notes.
Με descenting order:

![εικόνα](https://user-images.githubusercontent.com/75616736/177619244-e440403e-05d2-44b8-811c-8d6348163fcb.png)

Με ascenting order:
![εικόνα](https://user-images.githubusercontent.com/75616736/177619312-c09ce8bc-1abb-42ff-ac5f-cca2b7d1310f.png)


## Function deleteAccount():
Εισαγωγή του email του χρήστη "email" και έπειτα διαγραφή του client με εκείνο το email (μοναδικό email για κάθε χρήστη για αποφυγή σφαλμάτων) επίσης διαγράφονται και όλα τα note που έχει κάνει αυτός ο χρήστης:
![εικόνα](https://user-images.githubusercontent.com/75616736/177619859-a96c06f8-1922-42b3-99d1-9e14dc4d0f04.png)

Πηγαίνοντας στην βάση παρατηρούμε ότι ο χρηστης και όλα τα notes του έχουν διαγραφεί:
![εικόνα](https://user-images.githubusercontent.com/75616736/177619936-8d5697cc-f23f-4b80-b57a-ae861ba37be4.png)

![εικόνα](https://user-images.githubusercontent.com/75616736/177619960-bfbd24a8-1658-4428-b910-ef44258d5a56.png)

## Function createUserAdmin():
Δημιουργία διαχειριστή με την ίδια διαδικάσια που υπάρχει στο function createUser(). Η διαδικασία αυτη μπορεί να εκτελεστεί μονο απο διαχειριστή "category": "admin" endpoint /createUserAdmin:

![εικόνα](https://user-images.githubusercontent.com/75616736/177622405-eb65e723-d7b6-4f5a-b963-db6f0c2041bd.png)

Παρακάτω βλέπουμε τον καινουργιο διαχειριστή:
![εικόνα](https://user-images.githubusercontent.com/75616736/177622473-2abf6511-a662-453e-961b-6e89d14729e1.png)


## Function deleteUserAdmin():
Διαγραφή admin. Η διαδικασία αυτη μπορεί να εκτελεστεί μονο απο διαχειριστή "category": "admin" endpoint /deleteUserAdmin:

![εικόνα](https://user-images.githubusercontent.com/75616736/177623023-8b0bfc8e-65b5-4715-af21-445d2ec5c774.png)

Επιτυχής διαγραφή:
![εικόνα](https://user-images.githubusercontent.com/75616736/177623038-16f6424c-f3cf-47b4-8fe3-4d9e88509543.png)






