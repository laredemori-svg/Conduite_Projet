import json
import sys

current_state = "START"


def react(emotion, confidence):

    boite_noire = {
        ("joy", "low"): "ask_clarification",
        ("joy", "medium"): "continue",
        ("joy", "high"): "suggest_pause",

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
        ("surprise", "high"): "suggest_pause",
    }

    emotions_allowed = {"joy", "sadness", "anger", "fear", "disgust", "surprise"}
    confidence_allowed = {"low", "medium", "high"}

    if emotion not in emotions_allowed or confidence not in confidence_allowed:
        return "ask_clarification", "L'emotion ou le niveau de confiance n'existe pas !!"

    messages = {
    "offer_support": "I am here to help and support you. C'est oké de ressentir ça, t'es juste dans une tempête émotionnelle !", 
    "de_escalate": "Mon reuf, il faut rester calm, let's slow down... Tu es en train de péter un câble !", 
    "slow_down": "Chill mate ! On va juste slow down un peu pour mieux discuter.", 
    "continue": "Grave cool ma vie, tu gères change rien ! Autre chose ?",
    "ask_clarification": "Je capte pas trop, tu peux éclaircir ça pour me help ?", 
    "suggest_pause": "Let's take a pause. On s'arrête là pour aujourd'hui." 
}
    action = boite_noire.get((emotion, confidence), "ask_clarification")
    message = messages.get(action, "Je ne sais pas comment réagir à cette émotion.") 

    return action, message

"""
def main():
    global current_state

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        data = json.loads(line)

        emotion = data.get("emotion", "")
        confidence = data.get("confidence", "")

        action, message = react(emotion, confidence)

        if current_state != "END":
            if action == "offer_support":
                current_state = "SUPPORT"
            elif action == "de_escalate":
                current_state = "DEESCALATE"
            elif action == "suggest_pause":
                current_state = "END"
        else :
            current_state = "END"

        output = {
            "action": action,
            "message": message,
            "next_state": current_state
        }

        print(json.dumps(output, ensure_ascii=False))

"""
def main():
    global current_state
    nom_fichier = "action_message_users.json"

    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    data = json.loads(line)
                    emotion = data.get("emotion", "")
                    confidence = data.get("confidence", "")

                    # 1. On calcule la réaction
                    action, message = react(emotion, confidence)

                    # 2. On gère la transition d'état (Mémoire)
                    if current_state != "END":
                        if action == "offer_support":
                            current_state = "SUPPORT"
                        elif action == "de_escalate":
                            current_state = "DEESCALATE"
                        elif action == "suggest_pause":
                            current_state = "END"
                    
                    # 3. On prépare l'objet de sortie
                    output = {
                        "action": action,
                        "message": message,
                        "next_state": current_state
                    }

                    # 4. On affiche le résultat
                    print(json.dumps(output, ensure_ascii=False))

                except json.JSONDecodeError:
                    print(f"Saut d'une ligne mal formante dans {nom_fichier}")
                    continue

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' est introuvable dans le dossier.")


if __name__ == "__main__":       
    main()


