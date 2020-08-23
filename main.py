import mail
import scraper

if __name__ == "__main__":

    URL_with_querry = 'https://www.index.hr/oglasi/rezultat-pretrage?pojamZup=-2&pojam=audi+a4+branik&tipoglasa=1&sortby=4&elementsNum=10&grad=0&naselje=0&num='
    noPages = 1
    html_filename = 'test.html'
    scraper.get_site(URL_with_querry, noPages, html_filename)

    sender = 'XGammaRayzX@gmail.com'
    receivers = ['antonio.ilinovic1@gmail.com']
    message = ''

    mail.send_email(sender, receivers, message)
