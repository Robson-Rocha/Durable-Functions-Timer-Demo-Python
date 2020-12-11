import aiohttp
import os
from typing import Optional

class KeyValueStore:
    BASE_URL = os.getenv('KVS_BASE_URL')

    def __init__(self, app_key: str, base_url: Optional[str]=None):
        self.__app_key = app_key
        if base_url is not None:
            self.BASE_URL = base_url

    async def set_value(self, key: str, value: str) -> bool:
        async with aiohttp.ClientSession() as client:
            async with client.post(f'{self.BASE_URL}/UpdateValue/{self.__app_key}/{key}/{value}') as response:
                return response.status == 200 and await response.text() == 'true'

    async def get_value(self, key: str) -> str:
        async with aiohttp.ClientSession() as client:
            async with client.get(f'{self.BASE_URL}/GetValue/{self.__app_key}/{key}') as response:
                if response.status == 200:
                    return (await response.text())[1:-1]
                else:
                    return None

if __name__ == '__main__':
    import asyncio
    async def main():
        kvs = KeyValueStore(app_key='Teste-KVS', base_url='https://keyvalue.immanuel.co/api/KeyVal')
        await kvs.set_value(key='Minha-Chave', value='Meu Valor')
        print(await kvs.get_value(key='Minha-Chave'))

    asyncio.get_event_loop().run_until_complete(main())
