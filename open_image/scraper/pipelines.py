from django.db.utils import IntegrityError
from open_image.models import Den, Article
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):
    
    def process_item(self, item, spider):
        try:
            item['news_website'] = spider.ref_object
            item['search_term'] = spider.search_terms #I added this its how we see what was searched per item
            
            checker_rt = SchedulerRuntime(runtime_type='C')
            checker_rt.save()
            item['checker_runtime'] = checker_rt
            item.save()


#            p1 = Den.objects.get(title='baby')
#            a1 = Article(search_term=spider.search_terms)
#            a1.dens.add(p1)


#            busi = item.save(commit=False)
#            p1 = Den.objects.get(title='pretty')
#            busi.dens.add(p1)
#            p1 = Den(title='pretty')
#            a1 = Article(search_term=spider.search_terms)
#            a1.dens.add(p1)
#            p1 = Den(title='pretty')
#            a1 = Article(search_term=spider.search_terms)
#            a1.dens.add(p1)

            spider.action_successful = True
            spider.log("Item saved.", log.INFO)
                
        except IntegrityError, e:
            spider.log(str(e), log.ERROR)
            raise DropItem("Missing attribute.")
                
        return item



