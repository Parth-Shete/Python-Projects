from gtts import gTTS

from playsound import playsound

audio = 'speech.mp3'
language = 'mr'
sp = gTTS(text = "कधी तू रिमझिम झरणारी बरसात कधी तू चम चम करणारी चांदरात कधी तू ...... कोसळत्या धारा थैमान वारा बिजलीची नक्षी अंबरात ... सळसळत्या लाटा भिजलेल्या वाटा चिंब पावसाची ओली रात ....", lang = language,slow=False)
sp.save(audio)
playsound(audio)