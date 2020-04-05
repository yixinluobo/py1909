from scrapy import cmdline

name = 'doutula'
cmd = 'scray crawl {0}'.format(name)
cmdline.execute(cmd.split())
