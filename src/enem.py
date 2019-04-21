import scrapy


class AosFatosSpider(scrapy.Spider):
    name = 'aosfatos',
    login_url = 'http://sistemasenem.inep.gov.br/EnemSolicitacao/login.seam'
    start_urls = [login_url]

    def parse(self, response):
        JFV = response.css('[name="javax.faces.ViewState"]::attr(value)').get()
        print(JFV)
        form_data = {
            'formLogin': 'formLogin',
            'username': 'xxxxxxxxx',
            'password': 'xxxxxxx',
            'j_id19.x': '109',
            'j_id19.y': '17',
            'javax.faces.ViewState': JFV
        }

        yield scrapy.FormRequest(url=self.login_url, formdata=form_data, callback=self.parse_home)

    def parse_home(self, response):
        JFV = response.css('[name="javax.faces.ViewState"]::attr(value)').get()
        form_data={
            'menuForm': 'menuForm',
            'panelMenuStatemenugroup_1': 'opened',
            'panelMenuActionmenugroup_1':'', 
            'panelMenuActionj_id10':'', 
            'panelMenuStatemenugroup_4': 'opened',
            'panelMenuActionmenugroup_4':'', 
            'panelMenuStatemenugroup_4_11':'', 
            'panelMenuActionmenugroup_4_11':'', 
            'panelMenuActionj_id20':'', 
            'panelMenuActionj_id21':'', 
            'panelMenuActionj_id22':'', 
            'panelMenuActionj_id23':'', 
            'panelMenuStatemenugroup_4_10':'', 
            'panelMenuActionmenugroup_4_10':'', 
            'panelMenuActionj_id24':'', 
            'panelMenuActionj_id25':'', 
            'panelMenuActionj_id26':'', 
            'panelMenuActionj_id27':'', 
            'panelMenuStatemenugroup_4_9':'', 
            'panelMenuActionmenugroup_4_9': '',
            'panelMenuActionj_id28': '',
            'panelMenuActionj_id29': '',
            'panelMenuActionj_id30': '',
            'panelMenuActionj_id31': '',
            'panelMenuStatemenugroup_4_8':'', 
            'panelMenuActionmenugroup_4_8': '',
            'panelMenuActionj_id32': '',
            'panelMenuActionj_id33': '',
            'panelMenuActionj_id34': '',
            'panelMenuActionj_id35': '',
            'panelMenuStatemenugroup_4_7':'', 
            'panelMenuActionmenugroup_4_7': '',
            'panelMenuActionj_id36': '',
            'panelMenuActionj_id37': '',
            'panelMenuActionj_id38': '',
            'panelMenuActionj_id39': '',
            'panelMenuStatemenugroup_4_6':'', 
            'panelMenuActionmenugroup_4_6': '',
            'panelMenuActionj_id40': '',
            'panelMenuActionj_id41': '',
            'panelMenuActionj_id42': '',
            'panelMenuActionj_id43': '',
            'panelMenuStatemenugroup_4_5':'', 
            'panelMenuActionmenugroup_4_5': '',
            'panelMenuActionj_id44': '',
            'panelMenuActionj_id45': '',
            'panelMenuActionj_id46': '',
            'panelMenuActionj_id47': '',
            'panelMenuStatemenugroup_4_4':'', 
            'panelMenuActionmenugroup_4_4': '',
            'panelMenuActionj_id48': '',
            'panelMenuActionj_id49': '',
            'panelMenuActionj_id50': '',
            'panelMenuActionj_id51': '',
            'panelMenuStatemenugroup_4_3': 'opened',
            'panelMenuActionmenugroup_4_3': '',
            'panelMenuActionj_id52': '',
            'panelMenuActionj_id53': '',
            'panelMenuActionj_id54': '',
            'panelMenuActionj_id55': 'j_id55',
            'panelMenuStatemenugroup_4_2': '',
            'panelMenuActionmenugroup_4_2': '',
            'panelMenuActionj_id56': '',
            'panelMenuActionj_id57': '',
            'panelMenuActionj_id58': '',
            'panelMenuActionj_id59': '',
            'panelMenuStatemenugroup_4_1':'', 
            'panelMenuActionmenugroup_4_1': '',
            'panelMenuActionj_id60': '',
            'panelMenuActionj_id61': '',
            'panelMenuStatemenugroup_5': 'opened',
            'panelMenuActionmenugroup_5': '',
            'panelMenuActionj_id62': '',
            'panelMenuStatemenugroup_6': 'opened',
            'panelMenuActionmenugroup_6': '',
            'panelMenuActionj_id63': '',
            'j_id8selectedItemName': 'j_id55',
            'javax.faces.ViewState':JFV 
        }

        yield scrapy.FormRequest(url='http://sistemasenem.inep.gov.br/EnemSolicitacao/home.seam', formdata=form_data, callback=self.parse_home2)

    def parse_home2(self, response):
        
    
        JFV = response.css('[name="javax.faces.ViewState"]::attr(value)').get()
        print(JFV)
        form_data = {
            'formularioForm': 'formularioForm',
            'cpfDecorate:cpfInput': '111111111111',
            'j_id91.x': '74',
            'j_id91.y': '15',
            'javax.faces.ViewState': JFV
        }

        yield scrapy.FormRequest(url='http://sistemasenem.inep.gov.br/EnemSolicitacao/solicitacao/resultado2010/cpf/solicitacaoPelaInternet.seam', formdata=form_data, callback=self.parse_home3)
        

    def parse_home3(self, response):
        # form_data={

        # }
        pass