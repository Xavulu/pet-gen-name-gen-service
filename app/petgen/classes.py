import json 
import os 
import markovify
from typing import List
import random
import logging

ages: List[str] = ["young", "adult", "senior"]

def chainmake(animal: str): 
    pathstr = f"{animal}_namegen.json"
    with open(os.path.join(os.path.dirname(__file__), pathstr), 'r' , encoding='utf-8' ) as file: 
        data = file.read()
    chain = json.loads(data)
    pets = markovify.Text.from_json(chain)
    return pets

def shuffle(arr: List[str], n: int) -> List[str]: 
    #fisher-yates babey !!!!!!
    for i in range (n - 1, 0, -1): 
        j = random.randint(0, i + 1)
        try:
            arr[i], arr[j] = arr[j], arr[i]
        except IndexError as error: 
            logging.warning(f'could not shuffle: {error}')
            return arr.reverse()
    return arr

def getItem(arr: List[str], n: int) -> str: 
    ind: List[int] = []
    for i in range (len(arr)): 
        ind.append(i)

    res_dct = dict(zip(ind, arr))
    qi = random.randint(0, n)
    if qi in res_dct.keys():
        return str(res_dct[qi]) 
    else: 
        return " "

class CatBreeds: 
    def __init__(self): 
        self.list = [
            "Abyssinian",
            "American Bobtail",
            "American Curl",
            "American Shorthair",
            "American Wirehair",
            "Applehead Siamese",
            "Balinese",
            "Bengal",
            "Birman",
            "Bombay",
            "British Shorthair",
            "Burmese",
            "Burmilla",
            "Calico",
            "Canadian Hairless",
            "Chartreux",
            "Chausie",
            "Chinchilla",
            "Cornish Rex",
            "Cymric",
            "Devon Rex",
            "Dilute Calico",
            "Dilute Tortoiseshell",
            "Domestic Long Hair",
            "Domestic Medium Hair",
            "Domestic Short Hair",
            "Egyptian Mau",
            "Exotic Shorthair",
            "Extra-Toes Cat / Hemingway Polydactyl",
            "Havana",
            "Himalayan",
            "Japanese Bobtail",
            "Javanese",
            "Korat",
            "LaPerm",
            "Maine Coon",
            "Manx",
            "Munchkin",
            "Nebelung",
            "Norwegian Forest Cat",
            "Ocicat",
            "Oriental Long Hair",
            "Oriental Short Hair",
            "Oriental Tabby",
            "Persian",
            "Pixiebob",
            "Ragamuffin",
            "Ragdoll",
            "Russian Blue",
            "Scottish Fold",
            "Selkirk Rex",
            "Siamese",
            "Siberian",
            "Silver",
            "Singapura",
            "Snowshoe",
            "Somali",
            "Sphynx / Hairless Cat",
            "Tabby",
            "Tiger",
            "Tonkinese",
            "Torbie",
            "Tortoiseshell",
            "Toyger",
            "Turkish Angora",
            "Turkish Van",
            "Tuxedo",
            "York Chocolate"
        ]
        self.breedCount = len(self.list)
        self.breeds = shuffle(self.list, self.breedCount)
        self.breed = getItem(self.breeds, self.breedCount)
    
    def getBreed(self) -> str: 
        if self.breed == " ": 
            return self.breeds[0] 
        else:
            return self.breed

class DogBreeds: 
    def __init__(self): 
        self.list = [
            "Affenpinscher",
            "Afghan Hound",
            "Airedale Terrier",
            "Akbash",
            "Akita",
            "Alaskan Malamute",
            "American Bulldog",
            "American Bully",
            "American Eskimo Dog",
            "American Foxhound",
            "American Hairless Terrier",
            "American Staffordshire Terrier",
            "American Water Spaniel",
            "Anatolian Shepherd",
            "Appenzell Mountain Dog",
            "Aussiedoodle",
            "Australian Cattle Dog / Blue Heeler",
            "Australian Kelpie",
            "Australian Shepherd",
            "Australian Terrier",
            "Basenji",
            "Basset Hound",
            "Beagle",
            "Bearded Collie",
            "Beauceron",
            "Bedlington Terrier",
            "Belgian Shepherd / Laekenois",
            "Belgian Shepherd / Malinois",
            "Belgian Shepherd / Sheepdog",
            "Belgian Shepherd / Tervuren",
            "Bernedoodle",
            "Bernese Mountain Dog",
            "Bichon Frise",
            "Black and Tan Coonhound",
            "Black Labrador Retriever",
            "Black Mouth Cur",
            "Black Russian Terrier",
            "Bloodhound",
            "Blue Lacy",
            "Bluetick Coonhound",
            "Boerboel",
            "Bolognese",
            "Border Collie",
            "Border Terrier",
            "Borzoi",
            "Boston Terrier",
            "Bouvier des Flandres",
            "Boxer",
            "Boykin Spaniel",
            "Briard",
            "Brittany Spaniel",
            "Brussels Griffon",
            "Bull Terrier",
            "Bullmastiff",
            "Cairn Terrier",
            "Canaan Dog",
            "Cane Corso",
            "Cardigan Welsh Corgi",
            "Carolina Dog",
            "Catahoula Leopard Dog",
            "Cattle Dog",
            "Caucasian Sheepdog / Caucasian Ovtcharka",
            "Cavachon",
            "Cavalier King Charles Spaniel",
            "Cavapoo",
            "Chesapeake Bay Retriever",
            "Chihuahua",
            "Chinese Crested Dog",
            "Chinese Foo Dog",
            "Chinook",
            "Chiweenie",
            "Chocolate Labrador Retriever",
            "Chow Chow",
            "Cirneco dell'Etna",
            "Clumber Spaniel",
            "Cockapoo",
            "Cocker Spaniel",
            "Collie",
            "Coonhound",
            "Corgi",
            "Coton de Tulear",
            "Curly-Coated Retriever",
            "Dachshund",
            "Dalmatian",
            "Dandie Dinmont Terrier",
            "Doberman Pinscher",
            "Dogo Argentino",
            "Dogue de Bordeaux",
            "Dutch Shepherd",
            "English Bulldog",
            "English Cocker Spaniel",
            "English Coonhound",
            "English Foxhound",
            "English Pointer",
            "English Setter",
            "English Shepherd",
            "English Springer Spaniel",
            "English Toy Spaniel",
            "Entlebucher",
            "Eskimo Dog",
            "Feist",
            "Field Spaniel",
            "Fila Brasileiro",
            "Finnish Lapphund",
            "Finnish Spitz",
            "Flat-Coated Retriever",
            "Fox Terrier",
            "Foxhound",
            "French Bulldog",
            "Galgo Spanish Greyhound",
            "German Pinscher",
            "German Shepherd Dog",
            "German Shorthaired Pointer",
            "German Spitz",
            "German Wirehaired Pointer",
            "Giant Schnauzer",
            "Glen of Imaal Terrier",
            "Golden Retriever",
            "Goldendoodle",
            "Gordon Setter",
            "Great Dane",
            "Great Pyrenees",
            "Greater Swiss Mountain Dog",
            "Greyhound",
            "Hamiltonstovare",
            "Harrier",
            "Havanese",
            "Hound",
            "Hovawart",
            "Husky",
            "Ibizan Hound",
            "Icelandic Sheepdog",
            "Illyrian Sheepdog",
            "Irish Setter",
            "Irish Terrier",
            "Irish Water Spaniel",
            "Irish Wolfhound",
            "Italian Greyhound",
            "Jack Russell Terrier",
            "Japanese Chin",
            "Jindo",
            "Kai Dog",
            "Karelian Bear Dog",
            "Keeshond",
            "Kerry Blue Terrier",
            "Kishu",
            "Klee Kai",
            "Komondor",
            "Kuvasz",
            "Kyi Leo",
            "Labradoodle",
            "Labrador Retriever",
            "Lakeland Terrier",
            "Lancashire Heeler",
            "Leonberger",
            "Lhasa Apso",
            "Lowchen",
            "Lurcher",
            "Maltese",
            "Maltipoo",
            "Manchester Terrier",
            "Maremma Sheepdog",
            "Mastiff",
            "McNab",
            "Miniature Bull Terrier",
            "Miniature Dachshund",
            "Miniature Pinscher",
            "Miniature Poodle",
            "Miniature Schnauzer",
            "Mixed Breed",
            "Morkie",
            "Mountain Cur",
            "Mountain Dog",
            "Munsterlander",
            "Neapolitan Mastiff",
            "New Guinea Singing Dog",
            "Newfoundland Dog",
            "Norfolk Terrier",
            "Norwegian Buhund",
            "Norwegian Elkhound",
            "Norwegian Lundehund",
            "Norwich Terrier",
            "Nova Scotia Duck Tolling Retriever",
            "Old English Sheepdog",
            "Otterhound",
            "Papillon",
            "Parson Russell Terrier",
            "Patterdale Terrier / Fell Terrier",
            "Pekingese",
            "Pembroke Welsh Corgi",
            "Peruvian Inca Orchid",
            "Petit Basset Griffon Vendeen",
            "Pharaoh Hound",
            "Pit Bull Terrier",
            "Plott Hound",
            "Pointer",
            "Polish Lowland Sheepdog",
            "Pomeranian",
            "Pomsky",
            "Poodle",
            "Portuguese Podengo",
            "Portuguese Water Dog",
            "Presa Canario",
            "Pug",
            "Puggle",
            "Puli",
            "Pumi",
            "Pyrenean Shepherd",
            "Rat Terrier",
            "Redbone Coonhound",
            "Retriever",
            "Rhodesian Ridgeback",
            "Rottweiler",
            "Rough Collie",
            "Saint Bernard",
            "Saluki",
            "Samoyed",
            "Sarplaninac",
            "Schipperke",
            "Schnauzer",
            "Schnoodle",
            "Scottish Deerhound",
            "Scottish Terrier",
            "Sealyham Terrier",
            "Setter",
            "Shar-Pei",
            "Sheep Dog",
            "Sheepadoodle",
            "Shepherd",
            "Shetland Sheepdog / Sheltie",
            "Shiba Inu",
            "Shih poo",
            "Shih Tzu",
            "Shollie",
            "Siberian Husky",
            "Silky Terrier",
            "Skye Terrier",
            "Sloughi",
            "Smooth Collie",
            "Smooth Fox Terrier",
            "South Russian Ovtcharka",
            "Spaniel",
            "Spanish Water Dog",
            "Spinone Italiano",
            "Spitz",
            "Staffordshire Bull Terrier",
            "Standard Poodle",
            "Standard Schnauzer",
            "Sussex Spaniel",
            "Swedish Vallhund",
            "Tennessee Treeing Brindle",
            "Terrier",
            "Thai Ridgeback",
            "Tibetan Mastiff",
            "Tibetan Spaniel",
            "Tibetan Terrier",
            "Tosa Inu",
            "Toy Fox Terrier",
            "Toy Manchester Terrier",
            "Treeing Walker Coonhound",
            "Vizsla",
            "Weimaraner",
            "Welsh Springer Spaniel",
            "Welsh Terrier",
            "West Highland White Terrier / Westie",
            "Wheaten Terrier",
            "Whippet",
            "White German Shepherd",
            "Wire Fox Terrier",
            "Wirehaired Dachshund",
            "Wirehaired Pointing Griffon",
            "Wirehaired Terrier",
            "Xoloitzcuintli / Mexican Hairless",
            "Yellow Labrador Retriever",
            "Yorkshire Terrier"
        ]
        self.breedCount = len(self.list) 
        self.breeds = shuffle(self.list, self.breedCount)
        self.breed = getItem(self.breeds, self.breedCount)
    
    def getBreed(self) -> str: 
        if self.breed == " ": 
            return self.breeds[0] 
        else:
            return self.breed

class CatGen: 
    def __init__(self): 
        cat_breeds = CatBreeds()
        catNames = chainmake("cat")
        self.cat = str(catNames.make_short_sentence(20, tries=100)) 
        self.breed = cat_breeds.getBreed()
        self.group = getItem(ages, len(ages))

    def getName(self) -> str: 
        return self.cat

    def getGroup(self) -> str: 
        if self.group == " ": 
            return "young"
        else:
            return self.group

    def catJSON(self) -> dict: 
        return {"cat" : self.cat, 
                "breed" : self.breed, 
                "age" : self.getGroup()}

class DogGen: 
    def __init__(self): 
        dog_breeds = DogBreeds()
        dogNames = chainmake("dog")
        self.dog = str(dogNames.make_short_sentence(20, tries=100))
        self.breed = dog_breeds.getBreed()
        self.group = getItem(ages, len(ages))

    def getName(self) -> str: 
        return self.dog 

    def getGroup(self) -> str: 
        if self.group == " ": 
            return "young"
        else:
            return self.group

    def dogJSON(self) -> dict: 
        return {"dog" : self.dog, 
                "breed" : self.breed, 
                "age" : self.getGroup()}






