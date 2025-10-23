# Erstelle ein Benutzer-Login-System, in dem sich der Benutzer zuerst registrieren und dann einloggen kann. 
# Das Programm sollte überprüfen, ob der Benutzer den richtigen Benutzernamen und das richtige Passwort eingegeben hat, # wenn er sich einloggt (also die gleichen, die er bei der Registrierung verwendet hat).

# Da wir das Speichern von Daten noch nicht abgedeckt haben, erstelle das Programm einfach so, dass das Registrieren und Einloggen in der gleichen Ausführung erfolgt.
# User If-Anweisungen und Benutzereingaben und Methoden zur Lösung der Herausforderung. (Hinweis: if- else Verwendung)


username=str()
password=str()

username=input(f"Bitte tragen Sie einen neuen Benutzernamen ein: ")
password=input(f"Bitte geben Sie nun ein Passwort ein: ")
print(f"Vielen Dank, Benutzer {username}. Sie können sich nun einloggen.")
print("------------------------------------------------------------------")
user_login=input(f"Bitte geben Sie Ihren Benutzernamen zur Anmeldung an: ")
if user_login==username:
    print(f"Hallo Benutzer {username}, bitte geben Sie nun Ihr Passwort ein: ")
    password_login=input()
    if password_login==password:
        print(f"{username}, Sie sind nun erfolgreich angemeldet")
    else:
        print(f"Falsches Passwort eingegeben. Bitte starten Sie die Anmeldung erneut")
        print("----------------------------------------------------------------------")
else:
    print(f"Dieser Benutzer existiert nicht. Bitte starten Sie die Anmeldung erneut.")
    print("----------------------------------------------------------------------")


