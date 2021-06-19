from src_python.httpsRequests import ( site,
                                        url_class,
                                        )
from src_python.utilities import (
                                    output_formatter,
                                    AuthConstructor
                                )
import json

#secrets
environ=json.load(open('secrets/login.json','r'))
KITE_USER= environ['KITE_USER']
KITE_PASSWORD= environ['KITE_PASSWORD']
TWO_FA=environ['TWO_FA']
#trial to work with zerodha trading 
#https://kite.trade/docs/connect/v3/market-quotes/

#prep****************************************

zerodha=site(
    host_url='https://kite.zerodha.com',
        )
zerodha.set_headers( header_dict={
                            'X-Kite-Version': '2.9.1',
                            #'X-Kite-Userid': KITE_USER,
                            }
                    )

login=url_class(name='login',url='/')
login_post=url_class(name='login_post', url='/api/login')
login_two_factor=url_class(name='login_two_factor', url='/api/twofa')
live_orders=url_class(name='live_orders', url='/oms/orders', Authentication=True)
holdings=url_class(name='holdings', url='/oms/portfolio/holdings')
historical=url_class( name='historical',
                      url='/oms/instruments/historical/%s/minute',
                      Authentication=True)
zerodha.set_url_map([login,
                    login_post,
                    login_post,
                    login_two_factor,
                    live_orders,
                    holdings,
                    historical,
                    ])

#**************************************************

#*************************************************
# login process
zerodha.start_session()
r0_tmp=zerodha.session_url_get('login')
r1_tmp=zerodha.session_url_post(key='login_post',
                              payload={'user_id':KITE_USER,
                                        'password':KITE_PASSWORD}
                             )
tmpkey='request_id'
tmpResult=output_formatter(r1_tmp,'json').get('data').get(tmpkey)
r_n=zerodha.session_url_post(
                    key='login_two_factor',
                    payload={'user_id':KITE_USER,
                            'twofa_value':str(TWO_FA),
                             tmpkey :tmpResult ,
                             'skip_session':''},
                        )

#quick check r_n.status_code == 200
auth=zerodha.save_authorization(AuthConstructor)
#*zerodha login complete ***********************************************

#*various zerodha url api ***********************************************

r2_tmp=zerodha.session_url_get(
                                key='live_orders',
                                )
r3_tmp=zerodha.session_url_get(
                                key='holdings',
                                auth=auth
                                )

r4_tmp=zerodha.session_url_get(
                                key='historical',
                                payload={
                                    'user_id':'SV1967',
                                    'oi':'1',
                                    'from':'2021-04-21',
                                    'to':'2021-06-20'},
                                url_fillers=356865,
                                )
#***********************************************************************


    