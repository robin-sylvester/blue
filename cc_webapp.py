import asab
import asab.web
import asab.web.rest
import aiohttp

class MyApplication(asab.Application):

    async def initialize(self):
        # Load the web service module
        from asab.web import Module
        self.add_module(Module)

        # Locate the web service
        websvc = self.get_service("asab.WebService")

        # Create a container
        container = asab.web.WebContainer(websvc, 'example:web', config={"listen": "0.0.0.0:9000"})

        container.WebApp.router.add_get('/test', self.test)
        container.WebApp.router.add_get('/exchange', self.exchange)

    async def test(self, request):
        return asab.web.rest.json_response(request=request, data={'success': True})

    async def exchange(self, request):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.exchangeratesapi.io/latest') as resp:
                if resp.status == 200:
                    response_text = await resp.json()
                    return asab.web.rest.json_response(request=request, data={'success': response_text})
                else:
                    return asab.web.rest.json_response(request=request, data={'success': False})

if __name__ == '__main__':
    app = MyApplication()
    app.run()
