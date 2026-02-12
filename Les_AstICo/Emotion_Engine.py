import json

def react (emotion, confidence):
    
    boite_noire = {
        ("joy", "low"): "ask_clarification",
        ("joy", "medium"): "continue",
        ("joy", "high"): "continue",
        
        ("sadness", "low"): "ask_clarification",
        ("sadness", "medium"): "offer_support",
        ("sadness", "high"): "offer_support",
        
        ("anger", "low"): "ask_clarification",
        ("anger", "medium"): "slow_down",
        ("anger", "high"): "de_escalate",
        
        ("fear", "low"): "ask_clarification",
        ("fear", "medium"): "slow_down",
        ("fear", "high"): "offer_support",
        
        ("disgust", "low"): "ask_clarification",
        ("disgust", "medium"): "slow_down",
        ("disgust", "high"): "de_escalate",
        
        ("surprise", "low"): "ask_clarification",
        ("surprise", "medium"): "continue",
        ("surprise", "high"): "continue",
    }

    emotions_allowed = {"joy", "sadness", "anger", "fear", "disgust", "surprise"}
    confidence_allowed = {"low", "medium", "high"}
    users_text = {"", "J'ai perdu ma montre trop deg", "Hein ?! 1Million sur mon compte", "Les clignotants c'est pour les cons", "J'adore DIOR, For Sure", "J'ai écrasé une fourmi aujourd'hui *snif*", }

    if emotion not in emotions_allowed or confidence not in confidence_allowed:
        return "aslk_clarification", "L'emotion ou le niveau de confiance n'existe pas !!"
    

    messages = {
            "continue": "Grave cool ma vie, tu gères change rien ! Autre chose ?",
            "offer_support": "C'est complètement oké de ressentir ça, t'es juste dans une tempête émotionnelle !",
            "slow_down":"Chill mate ! Arrête de te turlupiner...",
            "de_escalate":"Mon reuf tu es en train de péter un câble, calme toi !",
            "ask_clarification":"Erreur 404, l'émotion ou le niveau de confiance n'est pas clair. Veuillez répéter !!", 
        }

    action = boite_noire.get((emotion, confidence), "ask_clarification")
    message = messages.get(action, "Je ne sais pas comment réagir à cette émotion.") 

    return action, message


def main () :

    try:
        results = []
        with open("action_message.json", "r", encoding='utf-8') as f:
            data = json.load(f)

        for i in range(len(data)):
            emotion = data[i].get("emotion")
            confidence = data[i].get("confidence")

        
            emotion = data[i].get("emotion")
            confidence = data[i].get("confidence")

            action, message = react(emotion, confidence) 

            output = {
                "action": action,
                "message": message
            }

            results.append(output)
        results = json.dumps(results, indent=4, ensure_ascii=False)
        print(results)

            
        
        with open("output.json", "w", encoding='utf-8') as f:
            f.write(results)


    except Exception : 
        print(json.dumps({"error": "Une erreur est survenue lors du traitement de l'input."}))
    


main()
