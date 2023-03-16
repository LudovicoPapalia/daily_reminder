import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import datetime
import threading

# Imposta il logging per debuggare eventuali errori
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Inserisci qui il token del tuo bot
TOKEN = "your token here"

#definisco bot fuori da ogni variabile così è accessibile globalmente
bot = telegram.Bot(token=TOKEN)

# Inserisci qui l'ID di Utente A e Utente B
#utente a è il notificato mentre utente b è admin nonchè colui che riceve la notifica quando utente a clicca
USER_A_ID = another user id
USER_B_ID = your user id

# Crea una variabile globale per contare il numero di invii della notifica. tutti gli invvìii dei giorni sommati
send_count = 0

#Crea una variabile globale per il conteggio GIORNALIERO (numero di invii in un giorno)
send_count_today = 0

#Crea una variabile globale per contare il numero DI GIORNI
send_count_day_number = 0

# Crea una variabile globale per tenere traccia dello stato del bottone (cliccato o non cliccato)
button_status = "non cliccato"

#Creo una funzione per inviare la notifica quando voglio
def send_notification_now():
    print("inizio della funzione send_notification_now")
    global send_count # Usa la variabile globale send_count
    global send_count_today
    global send_count_day_number
    
    # Crea un oggetto bot con il token del tuo bot
    bot = telegram.Bot(token=TOKEN)
    
    # Crea un bottone inline con un callback data "clicked"
    button = InlineKeyboardButton("Compito eseguito! 🤗", callback_data="clicked")
    
    # Crea una tastiera inline con il bottone creato
    keyboard = InlineKeyboardMarkup([[button]])

    # Invia la notifica ad Utente A con la tastiera inline allegata
    bot.send_message(chat_id=USER_A_ID, text=f"Ciao, questa è una notifica. è la {send_count_today+1}° volta oggi. Questo è il {send_count_day_number+1}° giorno che ti scrivo. ti ho inviato {send_count+1} notifica in totale", reply_markup=keyboard)
    
    # Incrementa il contatore di invii di 1
    send_count_today += 1
    send_count += 1

    # Resetta lo stato del bottone a "non cliccato"
    global button_status 
    button_status = "non cliccato"
    
    # Crea un timer per richiamare la funzione check_button (scritta sotto) dopo 30 minuti (1800 secondi)
    #threading.Timer(1800, check_button).start()

    #simulo l'attesa di 30 minuti. ora sarà di 5 secondi
    threading.Timer(5, check_button).start()

    print("fine della funzione send_notification now")

# Crea una funzione per controllare lo stato del bottone dopo 30 minuti. non contiene timer perchè i timer sono nella funzione send_notification_now
def check_button():
     
    print("inizio controllo bottone")
    
    # Usa la variabile globale button_status 
    global button_status 

    # Se lo stato è ancora "non cliccato"
    if button_status == "non cliccato":
        # Invia un messaggio ad Utente B segnalando che Utente A non ha cliccato il bottone 
        bot.send_message(chat_id=USER_B_ID, text=f"Utente A non ha cliccato il bottone. invii oggi {send_count_today+1} .Questo è il {send_count_day_number+1}° giorno che ti scrivo. ti ho inviato {send_count+1} in totale")
        
        # Invia di nuovo la notifica ad Utente A 
        send_notification()

# Crea una funzione per inviare la notifica ad Utente A ogni 24 ore
def send_notification():
    print("inizio della funzione send_notification - ogni 24 ore")

    send_notification_now()

    # Crea un timer per richiamare questa funzione dopo 24 ore (86400 secondi)
    #threading.Timer(86400, send_notification).start()

    #simulo 24 ORE DI ATTESA. 5 minuti
    threading.Timer(300, send_notification).start()

    print ("fine della funzione send_notification")

# Crea una funzione per gestire i callback dei bottoni inline
def button(update, context):
    
    # Ottieni i dati del callback (in questo caso "clicked")
    query = update.callback_query.data
    
    # Se il callback è "clicked"

    print ("inizio controllo del click")

    if query == "clicked":

        print("inizio della esecusione causa cliccatura")

        global button_status 
        button_status = "cliccato"
        
        # Invia un messaggio ad Utente B dicendo che Utente A ha cliccato il bottone 
        context.bot.send_message(chat_id=USER_B_ID, text=f"Utente A ha cliccato il bottone💋.")
        
        # Invia un messaggio ad Utente A confermando che ha cliccato il bottone 
        update.callback_query.edit_message_text(text=f"Hai cliccato il bottone.")
        
        # Resetta il contatore di invii a zero 
        #global send_count 
        #send_count = 0

        #Reset del numero di invii giornaliero
        global send_count_today
        send_count_today = 0

        global send_count_day_number
        send_count_day_number = (send_count_day_number+1)


        # Cancella il timer precedente 
        #threading.Timer.cancel()
        
        # Crea un nuovo timer per inviare la prossima notifica dopo 24 ore 
        #threading.Timer(86400, send_notification).start()

        print("inizio la attesa causa cliccatura")

        #timer test. SIMULO 24 ORE. 5 minuti. QUESTO TIMER CHIAMA LA FUNZIONE send_notification
        threading.Timer(300, send_notification).start()
    

    print ("fine controllo del click")

# Crea una funzione principale per avviare il bot e registrare gli handler 
def main():
    
    print("funzione main iniziata")
    # Crea un oggetto updater con il token del tuo bot 
    updater = Updater(TOKEN)
    
    # Ottieni lo dispatcher dal updater 
    dp = updater.dispatcher
    
    # Registra un handler per i callback dei bottoni inline 
    dp.add_handler(CallbackQueryHandler(button))
    
    # Avvia il polling del bot 
    updater.start_polling()
    
    # Invoca la funzione per inviare la prima notifica ad Utente A 
    send_notification()

    print("funzione main finita")
    
    

if __name__ == '__main__':
   print("avvio del codice principale")
   main() 
   print("fine del codice principale")
