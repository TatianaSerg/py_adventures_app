from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["final_work"]
collection = db["events"]

docs = [
    {"date": "01-10", "event": "Naujametinis vakarėlis namuose su draugais"},
    {"date": "03-31", "event": "Šventėme katalikų Velykas kaime"},
    {"date": "04-27", "event": "Važinėjome mašinėlėmis Vingio parke"},
    {"date": "05-05", "event": "Šventėme stačiatikių Velykas"},
    {"date": "05-05", "event": "Stebėjome, kaip dėdė įkelia bites į avilius"},
    {"date": "05-05", "event": "Lukas pjovė žolę kaime traktoriumi"},
    {"date": "05-12", "event": "Važinėjome mašinėlėmis Vingio parke"},
    {"date": "05-14", "event": "Lukas vyko į ekskursiją su klase"},
    {"date": "05-18", "event": "Stebėjome, kaip kyla oro balionai"},
    {"date": "05-18", "event": "Važinėjome dviračiais"},
    {"date": "05-19", "event": "Važiavome į botanikos sodą"},
    {"date": "05-29", "event": "Lukas dalyvavo karatė turnyre baltų diržų"},
    {"date": "05-26", "event": "Aleksas valgė ledus balkone"},
    {"date": "06-03", "event": "Lukas sveikino mokytojus su mokslo metų pabaiga"},
    {"date": "06-04", "event": "Lukas gavo medalį už puikų mokymąsi"},
    {"date": "06-08", "event": "Aleksas valgė spragėsius kaime"},
    {"date": "06-16", "event": "Rinkome braškes miške"},
    {"date": "06-28", "event": "Lukas valgė kavineje „Vasilki“"},
    {"date": "06-29", "event": "Skrido lėktuvu"},
    {"date": "07-01", "event": "Lukas valgė picą svečiuose pas močiutę ir senelį"},
    {"date": "07-03", "event": "Lukas maudėsi upėje"},
    {"date": "07-08", "event": "Lukas lankėsi pas Anją"},
    {"date": "07-14", "event": "Aleksas suplėšė marškinėlius kaime"},
    {"date": "07-11", "event": "Lukas ir Anją laimėjo žaislus automatuose"},
    {"date": "07-14", "event": "Grįžome su mama namo"},
    {"date": "07-18", "event": "Lipome į kalną kaime su pusseserėmis"},
    {"date": "07-21", "event": "Aleksas valgė mėlynes kaime ir susitepė"},
    {"date": "07-23", "event": "Senelis vežė Aleksą traktoriuje"},
    {"date": "07-28", "event": "Pynėme apyrankes su pusseserėmis"},
    {"date": "08-11", "event": "Šventėme Elif gimtadienį"},
    {"date": "08-15", "event": "Aleksas žaidė su Brio"},
    {"date": "08-31", "event": "Tėtis vežė Aleksą traktoriuje kaime"},
    {"date": "09-04", "event": "Padarėme juokingus akinius iš spalvoto popieriaus"},
    {"date": "09-01", "event": "Atgal į mokyklą"},
    {"date": "09-13", "event": "Aleksas šventė grupės mergaitės gimtadienį"},
    {"date": "09-14", "event": "Vaikščiojome Vilniaus centre"},
    {"date": "09-22", "event": "Važinėjome traukinuku skvere centre"},
    {"date": "09-30", "event": "Svečiuose buvo Vitukas"},
    {"date": "10-11", "event": "Lukas piešėme paveikslą „Ruduo“ "},
    {"date": "10-20", "event": "Lukas buvo gimtadienyje"},
    {"date": "10-25", "event": "Į mokyklą pas Luką atvyko cirkas"},
    {"date": "10-31", "event": "Rinkome ir dalinome saldainius per Heloviną"},
    {"date": "11-14", "event": "Lukas vyko į ekskursiją į Trakus gaminti kibinų"},
    {"date": "11-15", "event": "Lukas baigė autorinį paveikslą „Arklys“"},
    {"date": "11-20", "event": "Aleksas šventė grupės berniuko gimtadienį"},
    {"date": "11-30", "event": "Važiavome į pagrindinę šalies eglutę troleibusu"},
    {"date": "12-04", "event": "Papuošėme eglutę mokykloje"},
    {"date": "12-06", "event": "Lukas gamino muilą mokykloje"},
    {"date": "12-17", "event": "Aleksui į darželį atėjo Kalėdų Senelis"},
    {"date": "12-20", "event": "Diskoteka mokykloje"},
    {"date": "12-20", "event": "Papuošėme eglutę namuose"},
    {"date": "12-24", "event": "Papuošėme eglutę kaime"},
    {"date": "12-25", "event": "Išvyniojome dovanas nuo Kalėdų Senelio"},
    {"date": "12-25", "event": "Važiavome į eglutę Kaune"},
    {"date": "12-26", "event": "Važiavome į eglutę Birštone"},
    {"date": "12-27", "event": "Pasivaikščiojome po Prienus"},
    {"date": "12-31", "event": "Naujametinis vakaras namuose su draugais"}
]

collection.insert_many(docs)
