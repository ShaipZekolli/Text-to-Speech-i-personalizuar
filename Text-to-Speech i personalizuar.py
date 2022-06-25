#ShZ
import sys
import os
import re
from time import sleep
import num2words

from deep_translator import GoogleTranslator
from playsound import playsound

import wave
import librosa
import numpy
import soundfile

def apply_fadeout(audio, sr, duration=0.3):
    # convert to audio indices (samples)
    length = int(duration*sr)
    end = audio.shape[0]
    start = end - length

    # compute fade out curve
    # linear fade
    fade_curve = numpy.linspace(0.5, 0.0, length)

    # apply the curve
    audio[start:end] = audio[start:end] * fade_curve

print("""\

▀▀█▀▀ █▀▀ █─█ ▀▀█▀▀ ── ▀▀█▀▀ █▀▀█ ── █▀▀ █▀▀█ █▀▀ █▀▀ █▀▀ █──█ 　 　 ░█▀▀▀█ █──█ █▀▀█ ─▀─ █▀▀█ 
──█── █▀▀ ▄▀▄ ──█── ▀▀ ──█── █──█ ▀▀ ▀▀█ █──█ █▀▀ █▀▀ █── █▀▀█ 　 　 ─▀▀▀▄▄ █▀▀█ █──█ ▀█▀ █──█ 
──▀── ▀▀▀ ▀─▀ ──▀── ── ──▀── ▀▀▀▀ ── ▀▀▀ █▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ 　 　 ░█▄▄▄█ ▀──▀ ▀▀▀█ ▀▀▀ █▀▀▀""")

zhgjethja = 0
print("""\
	\n
	1.Lexo Alfabetin
	2.Lexo Tekstin nga fajjli
	""")

zhgjethja = int(input("Zgjedhe opsionin: "))

alfabeti = ['>','a','b','c','d','e','ë','f','g','gj','h','i','j','k','l','m','n','nj','o','p','q','r','s','sh','t','u','v','x','z','zh']
#Konvertimi i numrave ne fjale
try:	
	input = sys.argv[1]
except:
	if zhgjethja == 1:
		print()
	else:
		input = str(input("Emri i fajllit: "))
try:
	text=""
	with open(input) as f_input:
		text = ">> "+f_input.read()
except:
	print("Jepni një file si input.\np.sh 'python Projekti.py shembull.txt'")

texts = text.split()
print(texts)
#Perkthimi nga english ne shqip
translated =[]
for num in texts:
	if num.isdigit():
		num = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), num)
		translated.append(GoogleTranslator(source='english', target='albanian').translate(f'{num}'))
	else:
		translated.append(num.lower())

special_char = '@_!#$%^&*()<?/\|}{~:,;.[]'
 
# using join() + generator to remove special characters
translated = [''.join(x for x in string if not x in special_char) for string in translated]
print(translated)
print()
if zhgjethja == 1:
	translated = alfabeti
else:
	translated = translated
#Gjenerimi i .txt fiajllit nga teksti
with open('output.txt', 'w') as f_output:
	str1 = " " 
	# return string  
	translated = str1.join(translated)
	f_output.write(translated)



# Get the list of all files and directories
path = "/home/ipi/Desktop/Projekti/SoundFiles"
path2 = "/home/ipi/Desktop/Projekti/temp/"
dir_list = os.listdir(path)

dir_list_no_ex = []

for token, _ in (entry.split(".", 1) for entry in dir_list):
	dir_list_no_ex.append(token)

print(f'Databaza --> \n{dir_list_no_ex}\n')
#print("Files and directories in '", path, "' :")
 
# prints all files
#print(dir_list)

numriFjaleve = len(re.findall(r'\w+', translated))
print(f'Numri i fjaleve: {numriFjaleve}')

fajlet = translated.split()

print(f'Fjalet per ti lexuar --> \n{fajlet}')

	#if translated == "provë":  
	# for playing mp3 file
		# for playing note.wav file
for ii in range(0,len(fajlet)):
	sleep(1.0)
	try:
		bool(dir_list_no_ex.index(fajlet[ii]))
		sleep(0.2)
		print(f'>> {dir_list_no_ex[dir_list_no_ex.index(fajlet[ii])]}')
		pathlib = f"{path}/{fajlet[ii]}.wav"
		orig, sr = librosa.load(pathlib)

		dur = librosa.get_duration(y=orig, sr=sr)
		if zhgjethja == 1:
			dur = dur - 0.06
		elif dur >= 0.5:
			dur = dur - 0.25
		else:
			dur = dur - 0.1
		out = orig.copy()
		apply_fadeout(out, sr, dur)

		#soundfile.write(f"{path2}{fajlet[ii]}.wav", orig, samplerate=sr)
		soundfile.write(f"{path2}{fajlet[ii]}f.wav", out, samplerate=sr)
		playsound(f"{path2}{fajlet[ii]}f.wav")
		os.remove(f"{path2}{fajlet[ii]}f.wav")

	except:
		fj = fajlet[ii]
		fj1 = fajlet[ii]
		o = []

		while fj1:
				o.append(fj1[:2])
				fj1 = fj1[2:]
		# print(o)
		# print(len(o))
		# cunt = len(fj)
		for x in range(0,len(o)):
			try:
				#print(o)
				if dir_list_no_ex.index(o[x]):
					sleep(0.5)
					fj = fj.replace(f"{o[x]}","")
					print(f'>> {dir_list_no_ex[dir_list_no_ex.index(o[x])]}')
					playsound(f'SoundFiles/{dir_list_no_ex[dir_list_no_ex.index(o[x])]}.wav')
							
			except:
				#print(fj)
				for w2 in o[x]:
					if dir_list_no_ex.index(w2):
						sleep(0.7)
						print(f'>> {dir_list_no_ex[dir_list_no_ex.index(w2)]}')
						playsound(f'SoundFiles/{dir_list_no_ex[dir_list_no_ex.index(w2)]}.wav')
						
