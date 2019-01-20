#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

url = "https://rc.qzone.qq.com/infocenter?via=toolbar"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
            "Cookie":"pgv_pvi=3272294400; RK=1EXauWaKMF; "
                     "ptcz=788c440f575755e150e1d36e109e31632a9e3b9d7418dde4002246875a7ff4df; "
                     "pgv_pvid=9808651936; tvfe_boss_uuid=a10842a77468090a; "
                     "o_cookie=569159845; QZ_FE_WEBP_SUPPORT=1; pt2gguin=o0569159845; "
                     "pgv_si=s7070034944; _qpsvr_localtk=0.7326845608341328; "
                     "pgv_info=ssid=s8204448218; uin=o0569159845; skey=@pqFsp8rLt; "
                     "ptisp=cm; p_uin=o0569159845; pt4_token=DsQxOSUTBwyZDYTPCJVXYC7qIF6MvgUQ19iUxBBQvHI_; "
                     "p_skey=Hv0SK1CpLLXPUEVwaayu2Qqd5gMeodVhRf5Ms8CMN8A_; qz_screen=1920x1080; "
                     "569159845_todaycount=0; 569159845_totalcount=68932; "
                     "cpu_performance_v8=1; rv2=8090DAF8A8E3D25D23190FC5EAB6815E87197CA9D167AA52E6; "
                     "property20=B47472EE81477A9938858C1A495A42B05FA512E9B10924ADB9A51C0224BF555A5FF1B1F7A0EB3069"
            }
cookie = "pgv_pvi=3272294400; RK=1EXauWaKMF; ptcz=788c440f575755e150e1d36e109e31632a9e3b9d7418dde4002246875a7ff4df; pgv_pvid=9808651936; tvfe_boss_uuid=a10842a77468090a; o_cookie=569159845; QZ_FE_WEBP_SUPPORT=1; pt2gguin=o0569159845; pgv_si=s7070034944; _qpsvr_localtk=0.7326845608341328; pgv_info=ssid=s8204448218; uin=o0569159845; skey=@pqFsp8rLt; ptisp=cm; p_uin=o0569159845; pt4_token=DsQxOSUTBwyZDYTPCJVXYC7qIF6MvgUQ19iUxBBQvHI_; p_skey=Hv0SK1CpLLXPUEVwaayu2Qqd5gMeodVhRf5Ms8CMN8A_; qz_screen=1920x1080; 569159845_todaycount=0; 569159845_totalcount=68932; cpu_performance_v8=1; rv2=8090DAF8A8E3D25D23190FC5EAB6815E87197CA9D167AA52E6; property20=B47472EE81477A9938858C1A495A42B05FA512E9B10924ADB9A51C0224BF555A5FF1B1F7A0EB3069"
cookie_dict = {i.split("=")[0]:i.split("=")[1] for i in cookie.split(";")}
print(cookie_dict)
# headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}

response = requests.get(url,headers = headers)
# response = requests.get(url,headers = headers,cookies = cookie_dict)

with open("qqkongjian.html","w",encoding="utf-8") as f:
    f.write(response.content.decode())