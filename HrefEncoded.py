import sublime
import sublime_plugin
from re import match
from urllib import parse

class HrefEncodedCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# all the href in the file
		hrefRegions = self.view.find_all('href="([^"]*)"')[::-1]

		# once we get all the regions
		# we loop on them
		for href in hrefRegions:
			# the full text (href="...")
			text = self.view.substr(href)

			# the link in the text
			link = match('href="([^"]*)"', text).group(1)

			# the link encoded
			link = parse.quote_plus(link)

			# the final href encoded
			finalHref = 'href="'+link+'"'

			# the replace
			self.view.replace(edit, href, finalHref)
		
