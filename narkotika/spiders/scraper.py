import scrapy

class PidanaUmumSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["putusan3.mahkamahagung.go.id"]
    start_urls = ["https://putusan3.mahkamahagung.go.id/direktori/index/pengadilan/pn-jombang/kategori/narkotika-dan-psikotropika-1.html"]
    
    def parse(self, response):
        next_page = response.xpath('//*[@id="tabs-1"]/div[3]/nav/ul/li[5]/a[2]/@href').extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse_first)
            
    def parse_first(self, response):
        per_link = response.css('div.spost.clearfix strong a')
        for page in per_link:
            link = page.attrib['href']
            if link:
                print(link)
                yield scrapy.Request(link, callback=self.parse_second)
    
    def parse_second(self, response):
        for selector in response.css('tbody'):
            yield {
                'Tanggal': selector.css('tr td h2::text')[1].get(),
                'Penuntut Umum': selector.css('tr td h2::text')[2].get(),
                'Terdakwa': selector.css('tr td h2::text')[4:].get(),
                'Nomor Putusan': selector.css('tr td')[2].get(),
                'Kata Kunci': selector.css('tr td')[8].get(),
                'Tanggal Register': selector.css('tr td')[12].get(),
                'Lembaga Peradilan': 'PN JOMBANG',
                'Hakim Ketua': selector.css('tr td')[18].get(),
                'Hakim Anggota': selector.css('tr td')[20].get(),
                'Panitera': selector.css('tr td')[22].get(),
                'Catatan Amar': selector.css('tr td')[28].get(),                
            }
        
