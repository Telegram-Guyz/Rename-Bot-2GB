from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("JishuBotz")


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app






#Token Verification Added by @The_TGguy
#Don't remove credit 💳 
#Editing this or selling this codes are prohibited 
#Verification codes by @GK-BOTZ
#Original repo by @Techifybots 
