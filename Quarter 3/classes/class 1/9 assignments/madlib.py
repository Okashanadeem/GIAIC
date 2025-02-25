def madlib_english():
    name = input("Enter a name: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    exclamation = input("Enter an exclamation: ")
    number = input("Enter a number: ")
    
    story = f"""
    Once upon a time, {name} was feeling very {adjective1}. So, they decided to go to {place} with their pet {animal}.
    On the way, they found a {adjective2} {noun1} lying on the ground. "{exclamation}!" they shouted.
    
    Suddenly, the {animal} started to {verb} uncontrollably! {name} had no choice but to ride a {noun2} to safety.
    After {number} hours of adventure, they finally made it home, only to realize their {noun1} had followed them!
    
    And that's how {name} became the most famous {animal}-whisperer in {place}!
    """
    
    print("\nHere’s your Mad Lib story:\n")
    print(story)
    
# madlib_english()




def madlib_urdu():
    name = input("Koi naam daalain: ")
    adjective1 = input("Aik sifat daalain: ")
    adjective2 = input("Aik aur sifat daalain: ")
    noun1 = input("Aik name daalain: ")
    noun2 = input("Aik aur name daalain: ")
    verb = input("Aik kaam daalain: ")
    place = input("Aik jagah ka naam daalain: ")
    animal = input("Aik janwar ka naam daalain: ")
    exclamation = input("Koi feeling likhein jese k Ohhh Ahhh waghera: ")
    number = input("Koi number daalain: ")
    
    story = f"""
    Aik din {name} bohat hi {adjective1} mehsoos kar raha tha. Usne socha kyun na {place} ki sair ki jaye.
    Raste mein usne aik {adjective2} {noun1} dekha aur zor se kaha, "{exclamation}!"
    
    Achanak, aik {animal} bhagta hua aya aur {verb} karne laga! {name} ghabra kar aik {noun2} par charh gaya.
    Taqreeban {number} ghantay baad, jab sab kuch normal hua, to {name} ne mehsoos kiya ke woh {place} mein sab se mashhoor shakhsiyat ban chuka hai!
    
    Aur yun aik aam din aik tareekhi din mein badal gaya!
    """
    
    print("\nYeh rahi aap ki mazedar kahani:\n")
    print(story)
    
# madlib_urdu()
