person = { "name": "John Carver" , "age": 30, "skills": ["Python" , "C++", "Java"]}


def sprawdzam(person, skill):
        
                return(all(skills in person["skills"] for skills in skill))  

                                   
                    
skillsy = ["C++"]

print(sprawdzam(person, skillsy))  
