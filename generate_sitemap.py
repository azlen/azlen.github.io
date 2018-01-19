from lxml import html

print "reading sitemap/index.html"

tree = html.parse('sitemap/index.html')

sitemap = open('sitemap.txt', 'w')

links = list(set(tree.xpath('//a/@href')))
links.sort()

print "writing links to sitemap.txt"

for link in links:
	sitemap.write(link + '\n')

print "complete"