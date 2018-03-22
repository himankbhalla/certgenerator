from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

def readFile():
	file = open("names.txt",'r')
	names = file.read()
	names = names.split("\n")
	return names

def generate_certi():
	#print "Enter the date :"
	#date = raw_input()
	print "Enter Course Name :"
	course_original = raw_input()
	print course_original
	print type(course_original)
	course = course_original.lower()

	logo = ""
	if "python" in course:
		logo = "courseTemplates/python.jpg"
	elif "chatbots" in course:
		logo = "courseTemplates/chatbot.jpg"
        elif "competitive" in course:
                logo = "courseTemplates/CP.jpg"
	elif "launchpad" in course or "cpp" in course:
		logo = "courseTemplates/Launchpad.png"
	elif "nodejs" in course or "elixir" in course or "javascript" in course or "web development" in course:
		logo = "courseTemplates/Elixir.jpg"
	elif "crux" in course or "java" in course:
		logo = "courseTemplates/Crux.png"
	elif "android" in course or "pandora" in course:
		logo = "courseTemplates/Android.jpg"
	elif "perceptron" in course or "machine" in course:
		logo = "courseTemplates/Perceptron.jpg"
	elif "game" in course or "canvas" in course:
		logo = "courseTemplates/GameDev.png"
	elif "algo" in course:
		logo = "courseTemplates/Algo.png"

	names = readFile()
	if not os.path.exists(course_original):
		os.makedirs(course_original)
	for i , name in enumerate(names):
		img = Image.open(logo)
	#	img = Image.open("Logos/template.jpg")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("PTM55FT.ttf",50)
		font1 = ImageFont.truetype("PTM55FT.ttf",40)
		font2 = ImageFont.truetype("PTM55FT.ttf",35)
		width, height = img.size
		#course_logo = course_logo.resize((int(width * 1.5), int(height * 1.5)))
		#img.paste(course_logo,(162,190))
		x= (1040 - len(name)*30)/2 + 340
		#330 to 1400
		draw.text((x,640),name,(89,72,65),font=font)
		#draw.text((350,985),date,(89,72,65),font=font1)
		#draw.text((580,715), "for successfully completing",(89,72,65),font=font1)

		#if len(course_original)>15:
			#draw.text((460,760), course_original,(89,72,65),font=font)
		#else:
			#draw.text((650,770), course_original,(89,72,65),font=font)

		#draw.text((600,820), "at Coding Blocks, Delhi",(89,72,65),font=font1)
		certi_name = str(i+1) + "_"  + name + "_certi.png"
		img.save(course_original + "/" + certi_name)
		#img.show()
	print("done")

#readFile()
generate_certi()
