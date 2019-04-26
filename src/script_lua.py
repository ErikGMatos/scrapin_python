# Exemplo de uso do Splash no Scrapy com script Lua
# Acesso o google.com.br e clico no botao 'estou com sorte'
# Depois aguardo até as imagens serem carregadas para entao devolver o html e um screenshot
function main(splash, args)
assert(splash: go(args.url))
assert(splash: wait(0.5))
local element = splash: select('.FPdoLc.VlcLAe [name="btnI"]')
local bounds = element: bounds()
assert(element: mouse_click{x=bounds.width/3, y=bounds.height/3})

while not splash:
    select('.thumb-image img') do
    splash: wait(0.1)
end
return {html = splash: html(), png = splash: png()}
end
