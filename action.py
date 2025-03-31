import datetime
import speak
import webbrowser
import weather
import os




def Action(send) :   
  
    data_btn  = send.lower()

    if "olá" in data_btn: 
        speak.speak("Olá, como posso te ajudar?")  
        return "Olá, como posso te ajudar?"  

    elif "horário" in data_btn or "horas" in data_btn:
          current_time = datetime.datetime.now()
          Time = f"{current_time.hour} Horas e {current_time.minute} Minutos" 
          speak.speak(Time)
          return str(Time) 

    elif "desligar" in data_btn or "quit" in data_btn:
            speak.speak("Até logo")
            return "Até logo"  

    elif "tocar música" in data_btn or "musica" in data_btn:
        webbrowser.open("https://open.spotify.com/intl-pt")   
        speak.speak("spotify está pronto para tocar")                   
        return "spotify está pronto para tocar"


    elif 'abrir google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("Abrindo google")  
        return "Abrindo google"

    elif 'youtube' in data_btn or "abrir youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("Abrindo YouTube") 
        return "YouTube Abrindo"    
    
    elif 'clima' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    else :
        speak.speak( "não entendi!")
        return "não entendi!"       

