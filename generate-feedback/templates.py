import random

FEEDBACK_TEMPLATES = {
    "multumit": {
        "text_positive": [
            "Cursul de {curs} sustinut de {prof} a fost excelent explicat.",
            "Mi-a placut mult modul in care {prof} a prezentat materia.",
            "Aplicatiile practice au fost foarte utile pentru intelegerea {curs}."
        ],
        "text_improve": [
            "Totul a fost ok, poate mai multe exemple practice.",
            "Nu am sugestii majore, cursul a fost bine structurat.",
            "As recomanda suplimentarea materialelor de curs cu mai multe slide-uri."
        ],
        "text_problem": [
            "Nu am intampinat probleme semnificative.",
            "Mici dificultati la inceput, dar {prof} a clarificat totul.",
            "Sala a fost uneori putin aglomerata, dar s-a rezolvat."
        ],
        "text_other": [
            "Multumesc echipei de la {curs}!",
            "Unul dintre cursurile mele preferate din acest semestru.",
            "Sper ca {prof} sa predea si in semestrul urmator."
        ]
    },
    "nemultumit": {
        "text_positive": [
            "Materia {curs} este interesanta in sine, dar greu de urmarit.",
            "Laboratorul a salvat putin situatia la acest curs.",
            "Am apreciat efortul minim de la final."
        ],
        "text_improve": [
            "Metoda de predare la {curs} trebuie regandita complet.",
            "{prof} ar trebui sa interactioneze mai mult cu studentii.",
            "Materia este prea teoretica si simt ca nu am invatat chestii practice."
        ],
        "text_problem": [
            "Explicatiile de la curs au fost foarte ambigue.",
            "Criteriile de notare nu au fost clare de la inceput la {curs}.",
            "Nivelul de dificultate este disproportionat fata de ce se preda."
        ],
        "text_other": [
            "Sunt dezamagit de experienta generala la aceasta materie.",
            "Nu as recomanda acest curs in forma actuala.",
            "Sper sa se ia masuri pentru imbunatatirea modului de predare."
        ]
    },
    "constructiv": {
        "text_positive": [
            "Structura cursului de {curs} este buna in linii mari.",
            "{prof} stapaneste bine subiectul prezentat.",
            "Sunt cateva puncte tari in programa de anul acesta."
        ],
        "text_improve": [
            "Ar fi util un ritm mai lent la prezentarea slide-urilor.",
            "Mai multa interactiune in timpul cursurilor ar fi binevenita.",
            "Actualizarea suportului de curs pentru {curs} ar ajuta mult."
        ],
        "text_problem": [
            "Timpul alocat laboratoarelor pare insuficient pentru volumul de munca.",
            "Unele materiale sunt dificil de accesat pe platforma.",
            "Comunicarea cu {prof} ar putea fi imbunatatita."
        ],
        "text_other": [
            "Per total o experienta medie, cu potential de crestere.",
            "Cursul este ok, dar necesita mici ajustari la partea practica.",
            "Feedback-ul de la laboratoare a fost destul de util."
        ]
    }
}

def clean_course_name(raw_name):
    """Curata numele cursului din formatul lung Moodle."""
    if ":" in raw_name:
        return raw_name.split(":")[-1].strip()
    return raw_name

def get_consistent_text(q_type, curs, prof, profil):
    """Alege un text random bazat pe profil si tip intrebare."""
    if profil not in FEEDBACK_TEMPLATES:
        profil = "constructiv"
        
    if q_type in FEEDBACK_TEMPLATES[profil]:
        template = random.choice(FEEDBACK_TEMPLATES[profil][q_type])
        curs_curat = clean_course_name(curs)
        return template.format(curs=curs_curat, prof=prof)
    
    return ""