import json
import random
import time

import cv2
import ddddocr
import requests
from runJS import get_parames
import get_data1


class CodeTest():

    #获取challenge 和 gt 参数的值,这两个参数在后面校验滑块验证和获取短信验证码的时候会用到
    def getSlideCodeInit(self):
        url = "https://passport.fang.com/getslidecodeinit.api"
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Content-Length': '0',
            # 'Cookie': 'city=www1; global_cookie=pinrca9ipgy19tkoms7vdl78m19lq3l1edd; __utmz=147393320.1702460544.1.1.utmcsr=www1.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; g_sourcepage=txz_dl%5Egg_pc; __utmc=147393320; __utma=147393320.356182415.1702460544.1712483365.1712541581.4; __utmt_t0=1; __utmt_t1=1; token=0f5ca873fabd4003bb292dbff3bc85d4; unique_cookie=U_c7hkmp9iraa6oncqoguoi0adq38lupcdliy*6; __utmb=147393320.4.10.1712541581',
            'Origin': 'https://passport.fang.com',
            'Referer': 'https://passport.fang.com/?backurl=https%3A%2F%2Fpassport.fang.com%2F',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        response = requests.post(url=url,headers=headers)
        json_response = json.loads(response.text)
        gt = json_response["gt"]
        challenge = json_response["challenge"]
        return gt,challenge
    #获取到背景和滑块图
    def getImage(self,gt,challenge):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Referer': 'https://passport.fang.com/'
        }
        url = "https://recaptcha.fang.com/"
        callback = "fangcheck_" + str(int(1e4 * random.random()) + int(time.time() * 1000))
        params = {
            "c":"index",
            "a":"jigsaw",
            "gt":gt,
            "challenge":challenge,
            "callback":callback,
            "_200226":"",
        }
        response = requests.get(url=url,params=params,headers=headers).text
        json_response = json.loads(response.split("(")[-1].split(")")[0])
        bg_image = "https://static.soufunimg.com/common_m/m_recaptcha/jigsawimg/"+json_response["url"]#背景图
        slider_image = "https://static.soufunimg.com/common_m/m_recaptcha/jigsawimg/"+json_response["surl"]#滑块图
        with open("images/bg.jpg", "wb") as f:
            f.write(requests.get(bg_image).content)
        with open("images/tp.png", "wb") as f:
            f.write(requests.get(slider_image).content)

    #方式一：图片缺口识别得到x
    def detect_captcha_gap(self,bg,tp):
        '''
        bg: 背景图片
        tp: 缺口图片
        return:空缺距背景图左边的距离
        '''
        # 读取背景图片
        bg_img = cv2.imread(bg)  # 背景图片
        r_bg_img = cv2.resize(bg_img,(300,150)) #因为页面渲染图片的大小和原图的背景图片大小不一样,要进行缩放一下,不然识别缺口距离会有误
        cv2.imwrite("images/bg2.jpg", r_bg_img)  # 保存在本地
        # 缺口图片
        tp_img = cv2.imread(tp,cv2.IMREAD_UNCHANGED)  # 缺口图片,cv2.IMREAD_UNCHANGED读取,则透明背景不会被忽略
        r_tp_img = cv2.resize(tp_img, (57, 150))
        cv2.imwrite("images/tp2.png", r_tp_img)
        # 边缘检测：识别图片边缘
        bg_edge = cv2.Canny(r_bg_img, 100, 200)
        tp_edge = cv2.Canny(r_tp_img, 100, 200)
        # 图片二值图格式转换为RGB格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
        # 模版匹配：缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
        th, tw = tp_pic.shape[:2]   #缺口的宽和高
        # 最大值时图像左下角的坐标
        tl = max_loc
        # 根据左下角坐标和缺口宽高得到右上角点的坐标
        br = (tl[0] + tw, tl[1] + th)
        cv2.rectangle(r_bg_img, tl, br, (0, 0, 255), 2)  # 绘制缺口的外接矩形
        cv2.imwrite("images/result_new.png", r_bg_img)  # 保存在本地
        # 返回缺口的左上角X坐标,滑块移动这么多就是可以正确识别
        return tl[0]

    #方式二：图片缺口识别得到x,其实ddddocr内部实现的就是方式一里的模版匹配
    def ddddocr(self,bg,tp):
        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
        with open(bg, 'rb') as f:
            target_bytes = f.read()
        with open(tp, 'rb') as f:
            background_bytes = f.read()
        res = det.slide_match(target_bytes, background_bytes, simple_target=True)
        x = int(res['target'][0] * (300 / 320)) #图片渲染和原图比例不一样,则对x进行缩放
        return x

    #滑块请求成功或设备接口
    def slider_request(self,start,end,i,t,gt,challenge):
        callback = "fangcheck_" + str(int(1e4 * random.random()) + int(time.time() * 1000))
        params = {
            "c": "index",
            "a": "codeDrag",
            "start": start,
            "end": end,
            "i": i,
            "t": t,
            "gt":gt,
            "challenge":challenge,
            "callback": callback,
            "_200226": "",
        }
        url = "https://recaptcha.fang.com/"
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': 'city=www1; global_cookie=pinrca9ipgy19tkoms7vdl78m19lq3l1edd; __utmz=147393320.1702460544.1.1.utmcsr=www1.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; g_sourcepage=txz_dl%5Egg_pc; __utmc=147393320; token=57e0f19ddacd417baabde3f890b66045; __utma=147393320.356182415.1702460544.1712626949.1712822525.9; unique_cookie=U_c7hkmp9iraa6oncqoguoi0adq38lupcdliy*18',
            'Referer': 'https://passport.fang.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        print(requests.get(url=url, headers=headers, params=params).text)
    def main_run(self,codetest):
        gt, challenge = codetest.getSlideCodeInit()
        codetest.getImage(gt, challenge)
        #x = codetest.detect_captcha_gap("images/bg.jpg","images/tp.png")    #得到x坐标
        x = codetest.ddddocr("images/bg.jpg", "images/tp.png")    #得到x坐标
        data = get_data1.get_silde_track(x) #得到data数据
        start = data[0]['t']
        end = data[len(data)-1]['t']
        i = get_parames.get_i(self)  # 获取i参数
        t = get_parames.get_t(self,data) # 获取t参数
        time.sleep(3)
        codetest.slider_request(start,end,i,t,gt,challenge)


if __name__ == '__main__':
    codetest = CodeTest()
    codetest.main_run(codetest)
