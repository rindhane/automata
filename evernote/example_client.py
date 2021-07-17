#! /usr/bin/env python
from src_python.client_maker import get_client

client=get_client(
        auth_path='secrets/auth.json',
        client_path='secrets/client.json'
            )

print(client.get_user_store().getUser().name)