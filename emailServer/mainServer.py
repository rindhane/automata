#! /usr/bin/env python
import asyncio
from functools import partial

class ExampleHandler:
    async def handle_RCPT(server, session, envelope, address, rcpt_options):
        if not address.endswith('@example.com'):
            return '550 not relaying to that domain'
        envelope.rcpt_tos.append(address)
        return '250 OK'
    
    async def handle_DATA(server, session, envelope):
        print('Message from %s' % envelope.mail_from)
        print('Message for %s' % envelope.rcpt_tos)
        print('Message data:\n')
        for ln in envelope.content.decode('utf8', errors='replace').splitlines():
            print(f'> {ln}'.strip())
        print()
        print('End of message')
        return '250 Message accepted for delivery'


from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Sink
from aiosmtpd.smtp import SMTP, DATA_SIZE_DEFAULT

HOST='127.0.0.1'
PORT=8025
SMTPS_CONTEXT = None
handler= ExampleHandler()
serverFactory = partial(
        SMTP,
        handler,
        data_size_limit=DATA_SIZE_DEFAULT,
        enable_SMTPUTF8=False,
        tls_context=SMTPS_CONTEXT,
        require_starttls=False,
    )


controller = Controller(ExampleHandler,timeout=200, server_kwargs=dict(timeout=400))

if __name__ == "__main__" : 
    try:
        loop = asyncio.get_event_loop()
        server=loop.create_server(serverFactory,host=HOST, port=PORT, ssl=SMTPS_CONTEXT)
        controller.start()
        server_loop = loop.run_until_complete(server)
        loop.run_forever()
        print('controller started')
    except KeyboardInterrupt:
        pass
    except:
        print("Something went wrong")
    finally:
        controller.stop()
        loop.run_until_complete(server_loop.wait_closed())
        server_loop.close()
        loop.close()
