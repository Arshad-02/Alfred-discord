import os
import discord
import wikipedia
import random
from time import time,gmtime,strftime
from keep_alive import keep_alive
from replit import db



#global
no = random.randint(0, 9)
wiki_find = []
wiki_search = []
wiki_img = []

#a strt in the plan

server_1 = 751316396742410281
chnl_s1 = 848969368556929073

global_channel = "<#751316396742410284>"
dump_prblms = "<#751320993632616560>"
game_talk = "<#752894738411290666>"
forza = "<#848145112675516457>"
wiki = "<#848588628766097428>"
vadivelu = "<#836083586125791283>"

#somebodyother

server_2 = 851280136015839243
chnl_s2 = 851280136803713076

#test_server

server_3 = 845729877767225344
chnl_s3 = 848932882381537372
bot_DM = 867353258203545620
bot_attachments = 868804966092013568

#colors
colours = [
    0xfc0303, 0xfc7303, 0xfcdf0, 0x88fc03, 0x03fc80, 0x03fcdb, 0x03b1fc,
    0x9d03fc, 0xd203fc, 0xfc03c6, 0xfc0303
]
events = ["Your events"]

#presence intent

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#Wiki_bot link

wiki_add = "https://discord.com/api/oauth2/authorize?client_id=845730225249452112&permissions=2148001856&scope=bot"
wiki_logo = "https://qph.fs.quoracdn.net/main-qimg-779140d430142f1106de50c12a07cb97"
bot_id = ["<@845730225249452112>"]
#Choices

options = ["Paper", "Rock", "Scissors", "Rock", "Scissors", "Paper"]
soccer = ["Left", "Middle", "Right"]
goalkeeper = [
    ''':goal::goal::goal:
:man_dancing:
          
          :soccer:''', ''':goal::goal::goal:
             :man_dancing:
          
          :soccer:''', ''':goal::goal::goal:
                          :man_dancing:
          
          :soccer:'''
]
die_face = [
    ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":one:", ":two:",
    ":three:", ":four:", ":five:", ":six:"
]
sad_emojis = [
    ":smiling_face_with_tear:", ":slight_smile:", ":disappointed:",
    ":pensive:", ":worried:", ":confused:", ":slight_frown:", ":frowning2:",
    ":persevere:", ":confounded:", ":tired_face:", ":weary:", ":cry:", ":sob:",
    ":disappointed_relieved:"
]
happy_emojis = [
    ":partying_face:", ":star_struck:", ":relieved:", ":wink:", ":grin:",
    ":smile_cat:", ":handshake:", ":crown:", ":star2:", ":dizzy:", ":boom:",
    ":rainbow:", ":snowman2:", ":sparkling_heart:", ":wink:"
]
gif = "https://media.tenor.com/images/e54cc144e10289281a8e14974ea665bf/tenor.gif"

#Database_Functions


def create_suggestion(suggest):
	if "suggestions" in db.keys():
		suggestions = db["suggestions"]
		suggestions.append(suggest)
		db["suggestions"] = suggestions
	else:
		db["suggestions"] = [suggest]


def del_suggestion(index):
	suggestions = db["suggestions"]
	if len(suggestions) > index:
		del suggestions[index]
		db["suggestions"] = suggestions


#initialisations


@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online,
	                             activity=discord.Game("Alfred help"))
	print("We have logged in as {0.user}".format(client))
	guild = client.get_guild(server_3)
	channel = guild.get_channel(chnl_s3)

	await channel.send("I am back")


#bot_commands


@client.event
async def on_member_join(member):
	if member.guild.id == server_1:
		guild = client.get_guild(server_1)
		channel = guild.get_channel(chnl_s1)
		user_name = str(member).split('#')[0]
		my_embed = discord.Embed(
		    title=f"NEW MEMBER ALERT",
		    description=
		    f'''welcome {member.mention} to {guild.name} :partying_face:. Enjoy your stay:hugging:.
          here are the channels and their purposes,
          :one:{global_channel} To just hang around.
          :two:{dump_prblms} Venting.
          :three:{game_talk} Games.
          :four:{forza} Forza.
          :five: {wiki} Wikipedia bot. 
          :six: {vadivelu} Vadivelu bot.''',
		    color=colours[random.randrange(0, 10)])
		my_embed.add_field(name="BOTS", value="various Bots to hangout")
		my_embed.add_field(name="VOICE CHANNELS", value="For discussing")
		my_embed.set_author(name=f"Hello {user_name}",
		                    icon_url=member.avatar_url)
		my_embed.set_footer(text="Type Alfred help to know more")
		my_embed.set_image(url=str(gif))
		await channel.send(embed=my_embed)

	elif member.guild.id == server_2:
		guild = client.get_guild(server_2)
		channel = guild.get_channel(chnl_s2)
		user_name = str(member).split('#')[0]
		my_embed = discord.Embed(
		    title=f"NEW MEMBER ALERT",
		    description=
		    f'''welcome {member.mention} to {guild.name} :partying_face:. Enjoy your stay:hugging:''',
		    color=colours[random.randrange(0, 10)])
		my_embed.set_author(name=f"Hello {user_name}",
		                    icon_url=member.avatar_url)
		my_embed.set_footer(text="Type Alfred help to know more")
		my_embed.set_image(url=str(gif))
		await channel.send(embed=my_embed)

	elif member.guild.id == server_3:
		guild = client.get_guild(server_3)
		channel = guild.get_channel(chnl_s3)
		user_name = str(member).split('#')[0]
		my_embed = discord.Embed(
		    title=f"NEW MEMBER ALERT",
		    description=
		    f'''welcome {member.mention} to {guild.name} :partying_face:. Enjoy your stay:hugging:''',
		    color=colours[random.randrange(0, 10)])
		my_embed.set_author(name=f"Hello {user_name}",
		                    icon_url=member.avatar_url)
		my_embed.set_footer(text="Type Alfred help to know more")
		my_embed.set_image(url=str(gif))
		await channel.send(embed=my_embed)

	else:
		guild = client.get_guild(845729877767225344)
		channel = guild.get_channel(848932882381537372)
		user_name = str(member).split('#')[0]
		my_embed = discord.Embed(
		    title=f"NEW MEMBER ALERT",
		    description=
		    f'''welcome {member.mention} to {guild.name} :partying_face:. Enjoy your stay:hugging:''',
		    color=colours[random.randrange(0, 10)])
		my_embed.set_author(name=f"Hello {user_name}",
		                    icon_url=member.avatar_url)
		my_embed.set_footer(text="Type Alfred help to know more")
		my_embed.set_image(url=str(gif))
		await channel.send(embed=my_embed)


@client.event
async def on_member_remove(member):
	if member.guild.id == server_1:
		guild = client.get_guild(server_1)
		channel = guild.get_channel(chnl_s1)
		my_embed = discord.Embed(
		    title="SOMEONE LEFT",
		    description=f"{member.name} has left the server")
		await channel.send(embed=my_embed)

	elif member.guild.id == server_2:
		guild = client.get_guild(server_2)
		channel = guild.get_channel(chnl_s2)
		my_embed = discord.Embed(
		    title="SOMEONE LEFT",
		    description=f"{member.name} has left the server")
		await channel.send(embed=my_embed)

	elif member.guild.id == server_3:
		guild = client.get_guild(server_3)
		channel = guild.get_channel(chnl_s3)
		my_embed = discord.Embed(
		    title="SOMEONE LEFT",
		    description=f"{member.name} has left the server")
		await channel.send(embed=my_embed)

	else:
		guild = client.get_guild(server_3)
		channel = guild.get_channel(chnl_s3)
		my_embed = discord.Embed(
		    title="SOMEONE LEFT",
		    description=f"{member.name} has left the server")
		await channel.send(embed=my_embed)


@client.event
async def on_message(message):
	user_name = str(message.author).split('#')[0]
	if message.author == client.user:
		return
	msg = message.content

	if msg.startswith('Alfred help'):
		features = '''    :space_invader: **WELCOME TO WIKI BOT** :space_invader: 
    :one: Wf(Wiki find): Searches for the topic in wikipedia.
    :two: Ws(Wiki summary): Returns a short summary of the topic.
    :three: Wimg(Wiki img): Returns a image related to the topic.
    :four: Wiki random : Returns a random article from wikipedia.
    :five: Time : returns Time (IST)

    **TRY OUR MINI GAMES** :video_game:
    :one: :rock: Rock :scroll: Paper :scissors: Scissors.
    :two: Roll :Rolls a :game_die: for you.

    :notebook_with_decorative_cover: **TRY OUR EVENTS REMINDER** :notebook_with_decorative_cover:
    :warning: It's still in beta and all events are stored under same name/Database \n Individual event reminder will be available soon :warning:
    :one: re(Read events): Returns existing events.
    :two: ae(Add events): To create a new event/reminder.
    :three: de(Event delete): To delete a existing event/reminder by its index.

    :technologist:**SERVER LEVEL COMMANDS**:technologist:
    :one: id <mention>/sticker:Returns the id.
    :two: Tag <mention/s>:Tags the person anonymously.
    :three: Pfp <mention>:Returns the pfp of the person.
    :four: Add Alfred: Returns a link to add to new servers.

    **WELCOMING USERS AND ALERTS**:
    :new:Welcomes new users and sends alerts when a member leaves:new:.
    With customizable welcome message.

    :e_mail: **BOT DMs** :e_mail:
    :one: You can send and recieve msgs to and from bot DMs which can be viewed by developers. 
    :two: You can now send and recieve pictures, to and from the developers through bot DMs.

    **:gear:BETA::gear:**
      :one: When sent a yt link:Returns downloadable link
      :two: Soccer:soccer:.
      **MORE FEATURES COMING SOON**'''
		my_embed = discord.Embed(title="Bot commands",
		                         description=features,
		                         color=colours[random.randrange(0, 10)])
		my_embed.set_author(name=f"Hello {user_name}, here are my",
		                    icon_url=message.author.avatar_url)
		my_embed.set_footer(text="Drop your suggestion at Bot DMs ")

		await message.channel.send(embed=my_embed)

	if msg.startswith("Hello Alfred"):
		await message.channel.send(
		    f"Hello {happy_emojis[random.randrange(0,14)]} ,{message.author.mention}\n How can I help you, type 'Alfred help' to know what I can do."
		)

	names = ''' '''
	if msg.startswith("Server count"):
		if str(message.author.id) == "751290034552045681":
			server_names = list(client.guilds)
			n = 0
			for guild in client.guilds:
				n = n + 1
				names += f"{n}.{guild.name}" + "\n"
			my_embed = discord.Embed(
			    title="**Server infos**",
			    description=f"I am monitoring {len(server_names)} servers",
			    color=colours[random.randrange(0, 10)])
			my_embed.add_field(name="**Servers**", value=names, inline=False)
			my_embed.add_field(
			    name="**Latency**",
			    value=(f'Pong! In {round(client.latency * 1000)}ms'))
			my_embed.set_author(name=f"Hello Master {user_name}",
			                    icon_url=message.author.avatar_url)
			await message.channel.send(embed=my_embed)
		else:
			return

	if msg.startswith("Wf"):
		try:
			wiki_find = msg.split("Wf ", 1)[1]
			await message.channel.send(
			    f"Processing your request... :mag: ,{user_name}.")
			await message.channel.send(wikipedia.search(wiki_find, results=5))
		except wikipedia.DisambiguationError as e:
			await message.channel.send(e.options)
		except:
			await message.channel.send(
			    f"Invalid or no argument found {sad_emojis[random.randrange(0,14)]}"
			)

	if msg.startswith("Ws"):
		try:
			wiki_search = msg.split("Ws ", 1)[1]
			wiki_search_colon = ":" + wiki_search + ":"
			await message.channel.send(
			    f"Processing your request... :mag: ,{user_name}.")
			no = random.randrange(0, 9)
			title_url = wikipedia.page(wiki_search_colon).url
			img = wikipedia.page(wiki_search_colon).images[no]
			check = img.split(".s", 1)
			if check[-1] == "vg":
				img = ""
			else:
				img = img
			info = wikipedia.summary(wiki_search_colon, sentences=6)
			my_embed = discord.Embed(title=wiki_search,
			                         url=title_url,
			                         description=info,
			                         color=colours[random.randrange(0, 10)])
			my_embed.set_image(url=str(img))
			my_embed.set_author(name=user_name,
			                    icon_url=message.author.avatar_url)

			await message.channel.send(embed=my_embed)
			await message.channel.send(
			    ":information_source: Tip:\n If your search result is found to be incorrect,try being more specific or try adding 'history of' before the topic. Ex: History of Earth"
			)
		except wikipedia.DisambiguationError as e:
			test = e.options
			test = test[0]
			t_url = wikipedia.page(test).url
			t_info = wikipedia.summary(test, sentences=6)
			t_img = wikipedia.page(test).images[0]
			check = t_img.split(".s", 1)
			if check[-1] == "vg":
				t_img = ""
			else:
				t_img = t_img
			my_embed = discord.Embed(title=wiki_search,
			                         url=t_url,
			                         description=t_info,
			                         color=colours[random.randrange(0, 10)])
			my_embed.set_image(url=str(t_img))
			my_embed.set_author(name=user_name,
			                    icon_url=message.author.avatar_url)
			await message.channel.send(embed=my_embed)
		except:
			await message.channel.send(
			    f"Invalid or no argument found,try being more specific{sad_emojis[random.randrange(0,14)]}"
			)
			await message.channel.send(
			    f'''here are some suggestions or try adding history of "topic" ex: History of Earth :arrow_down:
      
      {wikipedia.search(wiki_search,results = 5)}''')

	if msg.startswith("Wiki random"):
		random_pg = wikipedia.random(pages=1)
		await message.channel.send(
		    f"Processing your request... :mag: ,{user_name}.")
		title_url = wikipedia.page(random_pg).url
		info = wikipedia.summary(random_pg, sentences=6)
		r_img = wikipedia.page(random_pg).images[0]
		check = r_img.split(".s", 1)
		if check[-1] == "vg":
			img = ""
		else:
			r_img = r_img
		my_embed = discord.Embed(title=random_pg,
		                         url=title_url,
		                         description=info,
		                         color=colours[random.randrange(0, 10)])
		my_embed.set_image(url=str(r_img))
		my_embed.set_author(name=user_name, icon_url=message.author.avatar_url)
		await message.channel.send(embed=my_embed)

	if msg.startswith("Wimg"):
		try:
			wiki_img = msg.split("Wimg ", 1)[1]
			wiki_img_colon = ":" + wiki_img + ":"
			await message.channel.send(
			    f"Processing your request... :mag: ,{user_name}.")
			no = random.randrange(0, 9)
			img = wikipedia.page(wiki_img_colon).images[no]
			my_embed = discord.Embed(title=wiki_img,
			                         description=message.author.mention,
			                         url=img,
			                         color=colours[random.randrange(0, 10)])
			my_embed.set_image(url=str(img))
			my_embed.set_author(name=user_name,
			                    icon_url=message.author.avatar_url)
			await message.channel.send(embed=my_embed)

		except wikipedia.DisambiguationError as e:
			await message.channel.send(e.options)
		except:
			await message.channel.send(
			    f"Invalid or no argument found {sad_emojis[random.randrange(0,14)]}"
			)

	if msg.startswith("Add Alfred"):
		my_embed = discord.Embed(
		    title="**Invite Link**",
		    description=
		    "Add Alfred to your server using the :link:[link](https://discord.com/api/oauth2/authorize?client_id=845730225249452112&permissions=2148001856&scope=bot)",
		    color=colours[random.randrange(0, 10)])
		my_embed.set_author(name=user_name, icon_url=message.author.avatar_url)
		my_embed.set_footer(text="Thank you(❤ ω ❤)")
		await message.reply(embed=my_embed)

	multi_str = ''' '''
	if msg.startswith("ae"):
		try:
			remind = msg.split("ae ", 1)[1]
			create_suggestion(remind)
			await message.reply(
			    f"Event added successfully {happy_emojis[random.randrange(0,14)]},{user_name}"
			)
		except:
			await message.channel.send(
			    f"Invalid or no argument found{sad_emojis[random.randrange(0,14)]}"
			)

	if msg.startswith("de"):
		try:
			suggestions = []
			if "suggestions" in db.keys():
				index = int(msg.split("de ", 1)[1])
				del_suggestion(index)
			await message.channel.send(
			    f"Event deleted,the remaining events are")
			suggestions = db["suggestions"]
			n = len(suggestions)
			for i in range(1, n):
				multi_str += (f"{i}. {suggestions[i]}") + "\n"
			my_embed = discord.Embed(title="The events are :-",
			                         description=multi_str,
			                         color=colours[random.randrange(0, 10)])
			my_embed.set_thumbnail(url=wiki_logo)
			my_embed.set_author(name=user_name,
			                    icon_url=message.author.avatar_url)
			my_embed.set_footer(text="Nothing to look here")
			await message.channel.send(embed=my_embed)

		except:
			await message.channel.send(
			    f"Invalid or no argument found{sad_emojis[random.randrange(0,14)]}"
			)

	if msg.startswith("re"):
		reminders = []
		if "suggestions" in db.keys():
			reminders = db["suggestions"]
			n = len(reminders)
			for i in range(1, n):
				multi_str += (f"{i} .{reminders[i]}") + "\n"
			my_embed = discord.Embed(title="The events are :-",
			                         description=multi_str,
			                         color=colours[random.randrange(0, 10)])
			my_embed.set_author(name=user_name,
			                    icon_url=message.author.avatar_url)
			my_embed.set_footer(
			    text="To add new events use 'ae' to delete use 'de'.")
			await message.channel.send(embed=my_embed)

	if any(word in msg for word in options):
		bot_pick = random.choice(options)
		if bot_pick == "Rock":
			if bot_pick == msg:
				await message.channel.send(
				    f"My {bot_pick} nullifies your {msg} it's a draw {happy_emojis[random.randrange(0,14)]} "
				)
			elif msg == "Scissors":
				await message.channel.send(
				    f"My {bot_pick} brakes your {msg} horrah :clap: I won,well played {happy_emojis[random.randrange(0,14)]}"
				)
			elif msg == "Paper":
				await message.channel.send(
				    f"My {bot_pick} is wrapped by your {msg} you won :sparkles:"
				)

		elif bot_pick == "Paper":
			if bot_pick == msg:
				await message.channel.send(
				    f"My {bot_pick}  nullifies your {msg} it's a draw {happy_emojis[random.randrange(0,14)]}"
				)
			elif msg == "Scissors":
				await message.channel.send(
				    f"My {bot_pick} is shredded by your {msg} hurrah :clap: you won,well played {happy_emojis[random.randrange(0,14)]}"
				)
			elif msg == "Rock":
				await message.channel.send(
				    f"My {bot_pick} wrapped your {msg}, Rimp I won :sparkles:")

		elif bot_pick == "Scissors":
			if bot_pick == msg:
				await message.channel.send(
				    f"My {bot_pick} nullifies your {msg} it's a draw {happy_emojis[random.randrange(0,14)]}"
				)
			elif msg == "Rock":
				await message.channel.send(
				    f"My {bot_pick} were broken by your {msg} horrah :clap: you won,well played {happy_emojis[random.randrange(0,14)]}"
				)
			elif msg == "Paper":
				await message.channel.send(
				    f"My {bot_pick} cuts your {msg} Rimp I won :sparkles:")

		else:
			await message.channel.send(
			    f"Unable to process response {sad_emojis[random.randrange(0,14)]}"
			)

	if msg.startswith("Pfp"):
		try:
			pfp = msg.split("Pfp ", 1)[1]
			pfp = pfp.replace("<", "")
			pfp = pfp.replace(">", "")
			pfp = pfp.replace("@", "")
			user = await message.guild.fetch_member(int(pfp))
			my_embed = discord.Embed(title=f"Pfp of {user}",
			                         color=colours[random.randrange(0, 10)])
			my_embed.set_image(url=user.avatar_url)
			await message.channel.send(embed=my_embed)
		except:
			await message.channel.send(
			    f"Invalid or no argument found{sad_emojis[random.randrange(0,14)]}"
			)

	if msg.startswith("Roll"):
		await message.reply(die_face[random.randrange(0, 12)])

	if msg.startswith("Tag"):
		try:
			id = msg.split("Tag ")[1]
			await message.delete()
			await message.channel.send(f"Hello {id}")
		except:
			await message.channel.send(
			    f"Invalid or no argument found{sad_emojis[random.randrange(0,14)]}"
			)
	if msg.startswith("id"):
		try:
			emoji = msg.split("id ")[1]
			emoji = emoji.replace("<", "|")
			emoji = emoji.replace(">", "|")
			await message.reply(emoji)
		except:
			await message.reply(
			    f"Invalid or no argument found{sad_emojis[random.randrange(0,14)]}"
			)

	if msg.startswith("Soccer"):
		get_msg = await message.channel.send(goalkeeper[1])
		get_id = get_msg.id
		time.sleep(2)
		msgs = await message.channel.fetch_message(get_id)
		choice = goalkeeper[random.randrange(0, 3)]
		await msgs.edit(content=choice)
		time.sleep(5)
		#try getting user id by which you can get user response
		print(msg)
		if any(word in msg for word in soccer):
			print(msg)
			if choice == goalkeeper[0] and msg == soccer[0]:
				await message.channel.send(":sparkles: you scored :sparkles:")
			elif choice == goalkeeper[1] and msgs == soccer[1]:
				await message.channel.send(":sparkles: you scored :sparkles:")
			elif choice == goalkeeper[2] and msgs == soccer[2]:
				await message.channel.send(":sparkles: you scored :sparkles:")
			else:
				await message.channel.send("Invalid choice")

	if any(word in msg for word in bot_id):
		my_embed = discord.Embed(
		    description=
		    "Yes, How can I help you,To lodge query, DM the bot <your complain>,else use Alfred help to know more"
		)
		await message.reply(embed=my_embed)

	if msg.startswith("Time"):
		time_rn = strftime("%H:%M", gmtime())
		hrs = time_rn.split(":", 1)[0]
		mts = time_rn.split(":", 1)[1]
		mts = int(mts) + 30
		hrs = int(hrs) + 5
		noon = "AM"
		if hrs >= 13:
			noon = "PM"
			hrs -= 12
		if mts > 60:
			hrs += 1
			mts = mts - 60
		get_time = (f"{hrs}:{mts} {noon}")
		await message.channel.send(get_time)

	get_attachment = []
	if str(message.channel.type) == "private":
		guild = client.get_guild(server_3)
		channel = guild.get_channel(bot_DM)
		try:
			if message.attachments != get_attachment:
				files = message.attachments
				for file in files:
					await channel.send(file.url)
			else:
				my_embed = discord.Embed(title="**Bot DM**",
				                         description=msg,
				                         color=colours[random.randrange(0,
				                                                        10)])
				my_embed.set_author(name=message.author,
				                    icon_url=message.author.avatar_url)
				await channel.send(embed=my_embed)
		except:
			await message.channel.send(
			    f"Invalid or no argument found{sad_emojis[random.randrange(0,14)]}"
			)

	if str(message.channel) == "bot-dm" and msg.startswith("<"):
		mem_mention = message.mentions[0]
		try:
			if message.attachments != get_attachment:

				files = message.attachments
				for file in files:
					await mem_mention.send(file.url)
			else:
				index = msg.index(" ")
				send_msg = msg[index:]
				await mem_mention.send(send_msg)
		except:
			await message.channel.send(
			    f"Invalid or no argument found{sad_emojis[random.randrange(0,14)]}"
			)

	if msg.startswith("Testing"):
		await message.reply("Got it")
  



#Execution

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)
