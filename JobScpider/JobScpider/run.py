from scrapy import cmdline

name = 'pythonPosition'
cmd = 'scray crawl {0}'.format(name)
cmdline.execute(cmd.split())
