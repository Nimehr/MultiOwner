import discord
import time
import datetime
from discord.ext import commands

class opAlert:

	global utcDatetime
	utcDatetime = datetime.datetime.utcnow()
	utcDatetime.strftime("%Y-%m-%d %H:%M:%S")
	global opHour
	opHour = 19
	global now
	now = {
	"day" : utcDatetime.strftime("%a"),
	"hour" : utcDatetime.strftime("%H"),
	"minute" : utcDatetime.strftime("%M"),
	"hourInt" : int(utcDatetime.strftime("%H"))+1,
	"minuteInt" : int(utcDatetime.strftime("%M"))
	}

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def opAuto(self):
		nowMinute = int(utcDatetime.strftime("%M"))
		nowHour = int(utcDatetime.strftime("%H"))
		starttime=time.time()
		await self.bot.say(str(nowHour) + ":" + str(nowMinute))
		if nowHour == 14 and nowMinute == 11:
			await self.bot.say("Tick")
			time.sleep(1.0 - ((time.time() - starttime) % 1.0))

	@commands.command(name="op")
	async def op(self):
		# if str(now["day"]) is "Sun":
		hourOP = opHour - now["hourInt"]
		minuteOP = 60 - now["minuteInt"]
		msg = "The OP is in {} hours and {} minutes".format(str(hourOP), str(minuteOP))
		await self.bot.say(msg)


def setup(bot):
	bot.add_cog(opAlert(bot))
