from practice_mulcho_classes import test 

#array of questions to be used as inpput for 
prompts = [
    "Proteins are made up of ___, joined together in a chain.\n (a) Carbohydrates\n (b) Starch\n (c) Genes\n (d) Amino acids\n",
    "\n___ is a nucleic acid that is usually single-stranded?\n (a) Genes\n (b) RNA\n (c) DNA\n (d) Chromosomes\n",
    "\nEndocytosis, exocytosis, and transcytosis are examples of?\n (a) Osmosis\n (b) Diffusion\n (c) Passive transport\n (d) Active transport\n",
    "\nThe organelles within the cell whose main functions are digestion and hydrolysis\n (a) Lysosomes\n (b) Ribosomes\n (c) Mitochondria\n (d) Golgi bodies\n",
    "\nProteins leaving rough endoplasmic reticulum are transported to the ___ for modification, packaging, and transport to the appropriate location.\n (a) Ribosomes\n (b) Mitochondria\n (c) Golgi apparatus\n (d) Nucleus\n",
    "\nWhich of the following system eliminates excess nitrogen from the body?\n (a) Digestive system\n (b) Urinary system\n (c) Respiratory system\n (d) Lymphatic system\n",
    "\nDuring which phase the nuclear envelope dissolve and the chromatin condenses?\n (a) Metaphase\n (b) Prophase\n (c) Interphase\n (d) Intraphase\n",
    "\nDuring which phase, the individual chromosomes line up in the middle of the cell?\n (a) Metaphase\n (b) Prophase\n (c) Anaphase\n (d) Telephase\n",
    "\nWhich of the following is a form of RNA that carries amino acids to the ribosome during protein synthesis?\n (a)mRNA\n (b)tRNA\n (c)rRNA\n (d)Genes\n",
    "\nThe system which protects and supports body organs is called?\n (a) Immune system\n (b) Nervous system\n (c) Skeletal system\n (d) Integumentary system\n"
]

#another array to define objects
list_of_q = [ 
    test(prompts[0], "d"), 
    test(prompts[1], "b"),
    test(prompts[2], "d"),
    test(prompts[3], "a"),
    test(prompts[4], "c"),
    test(prompts[5], "b"),
    test(prompts[6], "b"),
    test(prompts[7], "a"),
    test(prompts[8], "b"),
    test(prompts[9], "c")
]

def run_test(list_of_q): #parameter is the array = object
    score = 0
    for question in list_of_q:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(list_of_q)) + " correct")

run_test(list_of_q)

