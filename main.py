import asyncio
from module_adm import module_adm
from module_bos import module_bos
from module_cum import module_cum
from module_doc import module_doc
from module_lds import module_lds
from setup import PARAMS, setup_log, setup_folder


class run_module:
    def __init__(self) -> None:
        setup_folder()
        setup_log()
            
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.results = self.loop.run_until_complete(self.mapping_module())
    
    async def mapping_module(self):
        coros = []
        for module in PARAMS["source"]:
            
            if module == "ADM":
                tasks  = module_adm().run(module)
                coros.append(asyncio.create_task(tasks))
                
            elif module == "BOS":
                tasks  = module_bos().run(module)
                coros.append(asyncio.create_task(tasks))
                
            elif module == "CUM":
                tasks  = module_cum().run(module)
                coros.append(asyncio.create_task(tasks))
                
            elif module == "DOC":
                tasks  = module_doc().run(module)
                coros.append(asyncio.create_task(tasks))
                
            elif module == "LDS":
                tasks  = module_lds().run(module)
                coros.append(asyncio.create_task(tasks))
                
        return await asyncio.wait(coros)
        
class start_app(run_module):
    pass
            
            