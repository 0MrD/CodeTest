var t = String.fromCharCode
x = {
    compress: function (e) {
        return x.baseCompress(e, 16, function (e) {
            return x.toChart16(t(e))
        })
    },
    baseCompress: function (e, t, n) {
        if (null === e)
            return "";
        for (var r, a, o, i, s = {}, c = {}, l = "", d = 2, u = 3, g = 2, h = [], f = 0, v = 0, m = 0; m < e.length; m += 1)
            if (o = e.charAt(m),
            Object.prototype.hasOwnProperty.call(s, o) || (s[o] = u++,
                c[o] = !0),
                i = l + o,
                Object.prototype.hasOwnProperty.call(s, i))
                l = i;
            else {
                if (Object.prototype.hasOwnProperty.call(c, l)) {
                    if (l.charCodeAt(0) < 256) {
                        for (r = 0; r < g; r++)
                            f <<= 1,
                                v === t - 1 ? (v = 0,
                                    h.push(n(f)),
                                    f = 0) : v++;
                        for (a = l.charCodeAt(0),
                                 r = 0; r < 8; r++)
                            f = f << 1 | 1 & a,
                                v === t - 1 ? (v = 0,
                                    h.push(n(f)),
                                    f = 0) : v++,
                                a >>= 1
                    } else {
                        for (a = 1,
                                 r = 0; r < g; r++)
                            f = f << 1 | a,
                                v === t - 1 ? (v = 0,
                                    h.push(n(f)),
                                    f = 0) : v++,
                                a = 0;
                        for (a = l.charCodeAt(0),
                                 r = 0; r < 16; r++)
                            f = f << 1 | 1 & a,
                                v === t - 1 ? (v = 0,
                                    h.push(n(f)),
                                    f = 0) : v++,
                                a >>= 1
                    }
                    0 === --d && (d = Math.pow(2, g),
                        g++),
                        delete c[l]
                } else
                    for (a = s[l],
                             r = 0; r < g; r++)
                        f = f << 1 | 1 & a,
                            v === t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++,
                            a >>= 1;
                0 === --d && (d = Math.pow(2, g),
                    g++),
                    s[i] = u++,
                    l = String(o)
            }
        if ("" !== l) {
            if (Object.prototype.hasOwnProperty.call(c, l)) {
                if (l.charCodeAt(0) < 256) {
                    for (r = 0; r < g; r++)
                        f <<= 1,
                            v === t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++;
                    for (a = l.charCodeAt(0),
                             r = 0; r < 8; r++)
                        f = f << 1 | 1 & a,
                            v === t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++,
                            a >>= 1
                } else {
                    for (a = 1,
                             r = 0; r < g; r++)
                        f = f << 1 | a,
                            v == t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++,
                            a = 0;
                    for (a = l.charCodeAt(0),
                             r = 0; r < 16; r++)
                        f = f << 1 | 1 & a,
                            v == t - 1 ? (v = 0,
                                h.push(n(f)),
                                f = 0) : v++,
                            a >>= 1
                }
                0 === --d && (d = Math.pow(2, g),
                    g++),
                    delete c[l]
            } else
                for (a = s[l],
                         r = 0; r < g; r++)
                    f = f << 1 | 1 & a,
                        v == t - 1 ? (v = 0,
                            h.push(n(f)),
                            f = 0) : v++,
                        a >>= 1;
            0 == --d && (d = Math.pow(2, g),
                g++)
        }
        for (a = 2,
                 r = 0; r < g; r++)
            f = f << 1 | 1 & a,
                v == t - 1 ? (v = 0,
                    h.push(n(f)),
                    f = 0) : v++,
                a >>= 1;
        for (; ;) {
            if (f <<= 1,
            v === t - 1) {
                h.push(n(f));
                break
            }
            v++
        }
        return h.join("")
    },
    toChart16: function (e) {
        for (var t = "", n = e.length, r = 0; r < n; r++) {
            var a = e.charCodeAt(r).toString(16)
                , o = a.length;
            if (o < 4) {
                for (var i = 4 - o, s = "", c = 0; c < i; c++)
                    s += "0";
                a = s + a
            } else
                4 < o && console.log("More than four", a);
            t += a
        }
        return t
    }
}
function get_i() {
    var n = {
        "textLength": 34737,
        "HTMLLength": 107555,
        "documentMode": "CSS1Compat",
        "browserLanguage": "zh-CN",
        "browserLanguages": "zh-CN,zh",
        "devicePixelRatio": 1,
        "colorDepth": 24,
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "cookieEnabled": 1,
        "netEnabled": 1,
        "innerWidth": 1430,
        "innerHeight": 154,
        "outerWidth": 1446,
        "outerHeight": 901,
        "screenWidth": 1920,
        "screenHeight": 1080,
        "screenAvailWidth": 1920,
        "screenAvailHeight": 1040,
        "screenLeft": 66,
        "screenTop": 71,
        "screenAvailLeft": 0,
        "screenAvailTop": 0,
        "localStorageEnabled": 1,
        "sessionStorageEnabled": 1,
        "indexedDBEnabled": 1,
        "platform": "Win32",
        "doNotTrack": 0,
        "timezone": -8,
        "plugins": "PDFViewer,internal-pdf-viewer,ChromePDFViewer,internal-pdf-viewer,ChromiumPDFViewer,internal-pdf-viewer,MicrosoftEdgePDFViewer,internal-pdf-viewer,WebKitbuilt-inPDF,internal-pdf-viewer",
        "maxTouchPoints": 0,
        "flashEnabled": -1,
        "javaEnabled": 1,
        "hardwareConcurrency": 4,
        "webdriver": "",
        "performanceTiming": "0,0,12,0,0,0,0,14,63,619,519,519,525,956,956,1009,1734,1734,1734,0",
        "timestamp": 1713409901474,
        "cwidth": 300
    };
        n.timestamp = (new Date).getTime(),
        n.cwidth = 300;
    var r = [];
    return ["textLength", "HTMLLength", "documentMode"].concat("webdriver").concat(["screenLeft", "screenTop", "screenAvailLeft", "screenAvailTop", "innerWidth", "innerHeight", "outerWidth", "outerHeight", "browserLanguage", "browserLanguages", "systemLanguage", "devicePixelRatio", "colorDepth", "userAgent", "cookieEnabled", "netEnabled", "screenWidth", "screenHeight", "screenAvailWidth", "screenAvailHeight", "localStorageEnabled", "sessionStorageEnabled", "indexedDBEnabled", "CPUClass", "platform", "doNotTrack", "timezone", "canvas2DFP", "canvas3DFP", "plugins", "maxTouchPoints", "flashEnabled", "javaEnabled", "hardwareConcurrency", "jsFonts", "timestamp", "performanceTiming", "cwidth"]).map(function (e) {
        var t = n[e];
        r.push(void 0 === t ? -1 : t)
    }),
        encodeURIComponent(r.join("!!"))
}
function run(){
    return x.compress(get_i())
}
