from common import config
import argparse
import news_page_objects as news
import logging
logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


def _news_scrapper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    logging.info('Init scrapper for {}'.format(host))
    homepage = news.HomePage(news_site_uid, host)
    for link in homepage.article_links:
        print(link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    new_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                        help='The news site that you want to scrape',
                        type=str,
                        choices=new_site_choices)
    args = parser.parse_args()
    _news_scrapper(args.news_site)
