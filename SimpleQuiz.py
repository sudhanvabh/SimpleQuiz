from time import sleep as delay

# ---------------------------
BL = '\033[94m'
WH = '\033[97m'
GR = '\033[92m'
RD = '\033[91m'
MG = '\033[95m'
YL = '\033[93m'
RS = '\033[0m'
# ---------------------------
questions = (
    "What is the capital of Japan?",
    "Which element has the chemical symbol 'O'?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "Which year did the Berlin Wall fall?",
    "What is the longest river in South America?",
    "In what year was the first iPhone released?",
    "Who discovered penicillin?",
    "What is the highest mountain in Africa?",
    "Which ancient civilization built Machu Picchu?",
    "What is the hardest natural substance on Earth?",
    "In which country would you find the Taj Mahal?",
    "What is the smallest unit of matter?",
    "Which physicist developed the theory of quantum mechanics?",
    "What is the Heisenberg Uncertainty Principle?"
)  # ---------------------------
options = [
    ["A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"],
    ["A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Helium"],
    ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. 1987", "B. 1988", "C. 1989", "D. 1990"],
    ["A. Amazon", "B. Nile", "C. Mississippi", "D. Yangtze"],
    ["A. 2005", "B. 2006", "C. 2007", "D. 2008"],
    ["A. Marie Curie", "B. Alexander Fleming", "C. Louis Pasteur", "D. Gregor Mendel"],
    ["A. Mount Kilimanjaro", "B. Mount Everest", "C. Mount Elbrus", "D. Mount McKinley"],
    ["A. Mayans", "B. Aztecs", "C. Incas", "D. Olmecs"],
    ["A. Diamond", "B. Gold", "C. Silver", "D. Platinum"],
    ["A. India", "B. Pakistan", "C. Bangladesh", "D. Nepal"],
    ["A. Atom", "B. Molecule", "C. Quark", "D. Electron"],
    ["A. Isaac Newton", "B. Niels Bohr", "C. Albert Einstein", "D. Max Planck"],
    ["A. It states that particles can have exact momentum and position at the same time.",
     "B. It states that the position and velocity of an object cannot both be measured exactly, at the same time, "
     "even in theory.",
     "C. It explains the dual nature of light.",
     "D. It is a principle in classical mechanics that describes the dynamics of particles."]
]
# ---------------------------
answers = ("B", "A", "C", "C", "C", "A", "C", "B", "A", "C", "A", "A", "C", "D", "B")
# ---------------------------
statement = (
    f"The capital of Japan is {GR}Tokyo{RS}.",
    f"The element with the chemical symbol 'O' is {GR}Oxygen{RS}.",
    f"The Mona Lisa was painted by {GR}Leonardo da Vinci{RS}.",
    f"The largest planet in our solar system is {GR}Jupiter{RS}.",
    f"The Berlin Wall fell in {GR}1989{RS}.",
    f"The longest river in South America is the {GR}Amazon{RS}.",
    f"The first iPhone was released in {GR}2007{RS}.",
    f"Penicillin was discovered by {GR}Alexander Fleming{RS}.",
    f"The highest mountain in Africa is {GR}Mount Kilimanjaro{RS}.",
    f"Machu Picchu was built by the {GR}Incas{RS}.",
    f"The hardest natural substance on Earth is {GR}Diamond{RS}.",
    f"The Taj Mahal is located in {GR}India{RS}.",
    f"The smallest unit of matter is a {GR}Quark{RS}.",
    f"The physicist who developed the theory of quantum mechanics is {GR}Max Planck{RS}.",
    f"The Heisenberg Uncertainty Principle states that the position and velocity of an object cannot both be measured "
    f"exactly, at the same time, even in theory."
)
# ---------------------------
prizes = (
    "100", "200", "300", "500", "1,000", "2,000", "4,000", "8,000", "16,000", "32,000", "64,000", "125,000", "250,000",
    "500,000", "1,000,000")


# ---------------------------
def ask_ques(q_no):
    print(f"{BL}Question {q_no + 1}{RS}, for ${GR}{prizes[q_no]}{RS}. On your screen, please!")
    delay(1)
    print(f"    {q_no + 1}. {BL}{questions[q_no]}{RS}")
    delay(2)
    print(f"       Your options are ")
    delay(1)
    for i in range(len(options[q_no])):
        print(f"           {options[q_no][i][0:2]}{MG}{options[q_no][i][2:]}{RS}")
        delay(1)


# ---------------------------
def choose_option(q_no):
    while True:
        if input(f"So {name}, do you want to answer the question? {YL}[Y/N]{RS}: ").upper() != "N":
            while True:
                choosen_option = input(f"   {BL}Choose an option: {RS}").upper()
                if choosen_option in ["A", "B", "C", "D"]:
                    opt_name = {"A": f"{options[q_no][0]}", "B": f"{options[q_no][1]}", "C": f"{options[q_no][2]}",
                                "D": f"{options[q_no][3]}"}.get(choosen_option)
                    if input(f"      You chose {MG}{opt_name}{RS}. Are you sure? {YL}[Y/N]{RS}: ").upper() != "N":
                        return choosen_option
                    else:
                        pass
                else:
                    print(f"        {RD}Type 'A', 'B', 'C', or 'D' {RS}")
        else:
            if input(f"Do you want to walk away with {GR}${prizes[i]}{RS}? {YL}[Y/N]:").upper() == "Y":
                print(f"You walked away with {GR}${prizes[i]}{RS}")
                while True:
                    delay(1000)
                    print("")
            else:
                pass


# ---------------------------
def check_answer(q_no, c_opt):
    opt_name = {"A": f"{options[q_no][0]}", "B": f"{options[q_no][1]}", "C": f"{options[q_no][2]}",
                "D": f"{options[q_no][3]}"}.get(c_opt)
    print(f"So you say its{MG}{opt_name[2:]}{RS}")
    delay(2)
    if c_opt == answers[q_no]:
        print(f"{GR}    Correct!{RS}")
        delay(1)
        print(f"    {statement[q_no]}")
        delay(2)
        print(f"You have won ${GR}{prizes[q_no]}{RS}")
        delay(4)
        print("\n" + "------------------------------------------" + "\n")
    else:
        print(f"{RD}    Wrong!{RS}")
        delay(1)
        print(f"    {statement[q_no]}")
        delay(2)
        print(f"You walk away with ${GR}0{RS}")
        while True:
            delay(1000)
            print("")


name = input(f"Welcome to {YL}Who wants to be a Millionire{RS}! \nEnter your name to start: ").capitalize()
if name == "":
    name = "Player"
for i in range(0, 15):
    ask_ques(i)
    c_opt = choose_option(i)
    check_answer(i, c_opt)
print(f"{YL} CONGRATULATIONS! YOU HAVE WON A MILLION DOLLARS! {RS}")
