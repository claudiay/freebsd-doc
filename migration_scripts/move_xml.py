# Create a script move all xml files down a directory into the same level.
# Later on these should be turned into html templates.

import os
import shutil
templates = 'website/templates/'
languages = os.listdir(templates)
articles = {}
except_folders = ('base_templates',)

for lang in languages:
    if lang not in except_folders:
        print "Moving articles for %s" % lang
        try:
            articles[lang] = os.listdir('%s%s/articles/' % (templates, lang))
            for subject in articles[lang]:
                if (len(subject) > 5) and (subject[-5:] != '.html') and \
                    subject not in ('Makefile', 'Makefile.inc'):
                    search_path = '%s%s/articles/%s/' % (templates, lang, subject)
                    new_path = '%s%s/articles/%s.html' % (templates, lang, subject)
                    if ('article.xml' in os.listdir(search_path)):
                        print "Going to move file to %s and delete %s." % (new_path, search_path)
                        os.rename('%sarticle.xml' % search_path, new_path)
                        print 'renamed'
                        shutil.rmtree(search_path)
                        print 'deleted'
                        continue
        except Exception as e:
            print e
            pass




