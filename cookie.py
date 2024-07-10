# -*- coding:utf-8 -*-

import os
import time
from http.cookies import SimpleCookie
from threading import Thread

import requests

from utils import COMMON_HEADERS


class HedraCookie:
    def __init__(self):
        self.cookie = SimpleCookie()
        self.session_id = None
        self.token = None

    def load_cookie(self, cookie_str):
        self.cookie.load(cookie_str)

    def get_cookie(self):
        return ";".join([f"{i}={self.cookie.get(i).value}" for i in self.cookie.keys()])

    def get_token(self):
        return self.token

    def set_token(self, token: str):
        self.token = token


hedra_auth = HedraCookie()
hedra_auth.load_cookie(os.getenv("COOKIE"))


def update_token(hedra_cookie: HedraCookie):
    headers = {"cookie": "__Host-next-auth.csrf-token=031d7c841db2607a9c7bf059eb0dec18e97867d5f4228a4db361ce8bfc5a53a7%7Ce6c58b7be847279ff7da2f1f975d548171b059a884412ff6dae9e9892137d70f;ph_phc_LPkfNqgrjYQMX7vjw63IAdpzDFpLNUz4fSq3dgbMRgS_posthog=%7B%22distinct_id%22%3A%2201909646-d7d0-7862-be40-ec87205a0ef7%22%2C%22%24sesid%22%3A%5B1720508148587%2C%2201909646-d7ce-7fab-bb1c-8f4ab3a9dcb8%22%2C1720508143566%5D%7D;__Secure-next-auth.callback-url=https%3A%2F%2Fwww.hedra.com%2Flogin%3Fref%3Dnav;__Secure-next-auth.session-token.0=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0.._VgfCwPaZjmPBWXA.9WokbNqUUkJD0Xa43CeG-Nmm60AL80xToUyMKAXsaML0ha9PDQZFvAh63kGHpk_ioWe3FtlR1SztVrZNj-jIEEL8G1UTd1_rcmGQ5aDkm23PhfRnPvuPB7s9w31w6Kh4faUjK_LwVIUETeXaVOKoG59U7G4eDxoxp2A5pC-g5I_eUOuqPRtHhkQAemsM4hWwjMjNUNsOnAehVpIpKjvwzOlqG8LajTcorxVUA3fkBjgvJQnBs43y11Q0zf2ZtxyA9iTICRdXRj-V7frXmZQnvCFHFLzAunGQqLqhNGHsz0W191Qwi7WBPKi0UnAw4ZLYJ762W7d4U8KLd1p__oXqoOMPg5t0B6nfclOR2vOPP-64WLLOxsOVHBb7s-ZjYtOOFQATzWt87cK9WjFTRjAAyMdvyt4CApon5HOex9Dy9IYkqfSjgSp-wVtRE74WR4eYdnwQT8hsrZ3ZG4gAUypzsJ1Mi6tiZw3Wrpwp6OYzm6Ybi1T90p_L6GhQPdfpV044VdhsW8QvYRPrwxUiLzy0k2hsSTgKL7q8wA85fU6BZpiXrmKlD0WYf1TKjM_zYs3G5rK0m5_4PH8tv6Gwwzq-5o1YFe2gS23dkl3RPuoYJlsk-v-XRbPfHharBj57mRp5dxRO1SmCupjOzAIXhKlR9imIuBm94Fhdbto0NRqjBmt9wkkvogIiibvdoz-7enEe0pFx7anuUzRX7QL1pOEI3SW96kyZYFOLHM-c7724WXzhcoJUscW1UmyWJ_Nxkz8g1Nus8fj8VDJwx9icPvwoq2cCnj8fTwWkRANlcE2LIzN6cpcH2cbBLTNL0ASdjNCbtgfaIgAYFv9k8CJCzH97qAKqrPnpJRN6wBEaO76PXe7nVB3fC1rm_pFWeaNHYvVzj20H1NbQN4YImKlOpFwrYSgT-QL0WPd3517dvn3QAFrWOaTWBPO-70Qh2SiZlEaT9OIV_WiLm_zLdwNOUntiCDIHrx5Cf7SvTW3gM6W8VlSX7suh8_S9xVAdojYria1DJphydok6Q_slcR5bCKiVBLCYY6OuFB5_FADUpWUBkAqnlfabMUfwXA6FgpkoZ5xFyT5-lVPYSk8SY397FKuqyR1TAL3vVMMsiquOCy0SOPh2wOPqEFZvAIooT8_uxzu_wcvzYxGj52i9WjMiNWSXPidarUkXxMMRhTqEWQdaf9980rCtJ1Xf5Ngc8TuPEw0XyRgCaZR0At4bqnlMCqFuWvVPhjofI6pi57dskvXn5dlKFINZVl4G-ckGuBKlNZiparYxEULgxNPblSDzBxhoUgez5ZR0DicB2P7i4eh57qfXfqOYfqpHXgBBKaWM2b3ADTDTZcaDUkZyGx6f-9LLPeg_OUWiJghEmaUAB_btDQcH2yw8Gtzrxn46DDSauySuQMgwFHtYBMoPjasit4fgiHJN1MIXD-OLCcF9VldWOpISHEYPYGTp1qDVICZqBmV9nZqh5XBilgYHiayfHq2iXjNlRnPuWBm2_mE9AdHN3_LQDXU57NlHxjcd5Pbfy3H5SXWvGu82PbfKNL0m01aXBfd4qGBrK9SO1Ca6yHjNtSzRTiMppbaopCnZY60KiCNQE3Ih4tOFpqkddNOXbL_cLOeAZTQ2b_35Hjzkq4SUu_FvSzTXGIx9QtR_9uy4MFKSXDzx1K7jQE0IBga1_r7RhpYfH4hv40ToK9Fzs__-8URZK-Sw4RlhCETrLyKgFoI1-jQskV4j3xMtlXp9-1HEYJmECi4NcDKD5yB8B7AkwpPTIyx5Y9hEH148HyZnSjLzZjZETuT56fFjGjXx1jlu0oB6EPtOoxT6fY1EDV2s0TA54d9fwtL6FFDkymPjFJGdkBgOIMPp5UKeD4c3vj-O26TCBImA29IKxbR3r58PcY1a_9B0uAUhiGD8PRz01ovdb8dTWqfgcZmNSnvnGwQWeUvS4LUq1LM3-Eig6T70q8jwtC-nB2xtypv1eSf9MZJ4a4oDo-_CNs6AQEbOofgiLX-fN-HHxTkFjSsACTSWyZ4kViya6yXzBiJ4iGvsTx-11kcNEmcwMx4Iiv2Z-pUH0X-U41ak7PtaPWfc6FlFj0XOr_80lMmNB03077_bD_a3j0I71L7EWFskVQAcBZD_3-ZUD2IqsE0AvGgKWLAK9DDgwzd7C03pdq86DJgt85jqxybi2EguKM845_tKTTj_OKwWZV5wSIimUqA7VKad6LAok1ESei-ni9-Sne4LA2t5jDYoz-q7DKED1fZMxHjoXoafupQ2xlI2OyU4Pm0sCuXERe4zLwLLwystMoPmEIe4quDcOE5mxcIf1yLFkuZehhFxkNeU_JGOxkVby-wc9b_h9yB9CLGMaYxqN2VXUSbgEx4ENWNxjZxESDDlmMJ5H2VcN23Ozno7uRAUARyBe5PEmMq1jdUS5QKn-SJo3wuUbD8KwmbzqcgkYlffEeR9NcOylpCetH769Z_uy6LT2Ly7dIKYWRN1Umd-Y3f4dg19ocCSU1_7YYFPlFvsXbATFGhn3KUsu3Qf-D3TYKoM3kBDRgKQNNf3pfzW-aJxi74kGDhVAqRGq_YnKqHW3WrqCBmNXQLb5VfFhfT37ku4U-eoz08aBtEjEf3sByBewzgxOPaRyFlhSxi3IS6lQnS5UGWxTNB_q6P1jQGxIpavmuYGQGFzaRMpRKAFC7U-fkmF9w_orr9JoYcJFjX6TYZHHg-5i0tA0ggD_0MtfKcvNYECj1PN6qHL1d277L-cmU4xftlvT_f85kgbJxleeb0OVxcCySICMNdT6MSZXcclQi1U8Wum87ejjltEe28pKpbVQcf3raRljwV3RndNAzCnrcHGbRocez6LSGryNOh5xt4NwqFWu4rEuYM00MDyPE0nKaKY20vGhsDR3XYVkXi92TehWEarNGm6xQeo9bYfgfqcZJPXEnzi5ARSlIxVKcUG0SY1deEdDV7klQR-OF2KPy7Sd4pK9UeGa5rzLLbdgb--2IjrfJ4jiHdTONgq6vl_kJvATGuF-nr3CslONPhAe3K1_gwpVWhFwJ1KGtpNnReCsiUTGSBCNPT8_lp0I7o1behEMBFf0WKqdFqwAAjq-ED3y-2rKtqO8-p4Q3drn_dvDZXzLNOhp2LCGeOg8qSl40r7lpQEBF4lpXHcL2s32gxwNaFgrkywm5r3N5oYaSdJ3ZOUqYiiL0OkfsKgQ0IcvHD57RA7E9ex8D8dttX7ZvytW3kyb7tfJiXiFfCRqRZLL4aUmZbGbTyxBVwpw7LkoJyZOtweOwCN3fTGhV-ZaltZyW7AfDgFnhuwHYX02s794Su_ZUOqWfwj_jqnW7OcVJaQIF2Cl4UMLirATImjcMaWnmsdHYYmLonJCP29J6KrgVxK1P4Tbx5oRkBbTc2yX9eDe5PSq73zWbFIvpzjKy5InQlcakYZJejeMmsVA3Hf2Hkoky3R5T5t0u9s9a-nbOWF-yu_pHhkbpsb-PUJAlayRx0sWlT-2Ston-2S4rjH-lJccrSyRBtB8JvnzYnd_gwbHY4BPFmH58Gzb9Kq9CMm_C07XegKAXqGRShHlXbpqFsYs6ikK0XWQx3w9npKVT1n6MUuR12U7DdY0JFyx0mlgchoeOXLnfMR73eqlIDSFcsRGCY_UDRxCFnFWxWtcHO5kchfaQEdwCIC_WphyZlOhX8Z9Cl5NJDLe7eCdYPkUW8yiCXucbOMrdqvyu5fs4UAQHkVv5rFecM0jEhkwwr3EuugvrNQStzju0saXEPkuZ4DDo_yy4lugbbksSGNVt_6OwMPs3KddivSNV-UI-LooC7RwQhk8LWJx-N2-WKJ9qa-rXPmZ04CDFxW4RVPMau7BXV_aocoNXx-omcQOYHkvJGViSUyWxw;__Secure-next-auth.session-token.1=zm0T6gARrwTi8IhFpKlIGCo9H5dCOy-6GBAQbEQ1dfp_ZcRwCTiFVD12sZ7-oiR82yheJWpUPJALgjtx1VpY1ZQZAzmsE212kdlnJsPh6ZZnziWGvCsLl7xrs_jD64QxifH5GVKy4h-TWnVLp3RXl2qzd22p-tjERMIhmMvUDCMgJHePLlS3K4CjMWcJse5gjSi_mxEiEq7jHnDThuoFmHvnECfLdNqQRnc8aNNjJ7uzicW3Trg.SsqXywAcBZbjxPe3BiNLpQ"}
    headers.update(COMMON_HEADERS)
    resp = requests.get(
        url="https://www.hedra.com/api/auth/session",
        headers=headers,
    )
    resp_headers = dict(resp.headers)
    set_cookie = resp_headers.get("Set-Cookie")
    hedra_cookie.load_cookie(set_cookie)
    token = resp.json().get("user").get("access_token")
    hedra_cookie.set_token(token)
    # print(set_cookie)
    # print(f"*** token -> {token} ***")


def keep_alive(hedra_cookie: HedraCookie):
    while True:
        try:
            update_token(hedra_cookie)
        except Exception as e:
            print(e)
        finally:
            time.sleep(5)


def start_keep_alive(hedra_cookie: HedraCookie):
    t = Thread(target=keep_alive, args=(hedra_cookie,))
    t.start()


start_keep_alive(hedra_auth)
