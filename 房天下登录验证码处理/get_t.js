//var e1的e参数

//获取var e1里面的C函数
function C(e) {
    return "number" != typeof e ? e : 32767 < e ? e = 32767 : e < -32767 ? e = -32767 : Math.round(e)
}
//获取var t里面的e参数
var e1 = function (e) {
    var t = 0
        , n = 0
        , r = 0
        , a = 0
        , y = 300
        , o = 0
        , i = [];
    if (e.length <= 0)
        return [];
    for (var s = e.length, c = s < y ? 0 : s - y; c < s; c += 1) {
        var l = e[c]
            , d = l.e;
        "scroll" === d ? i.push([d, [l.x - r, l.y - a], C(o ? l.t - o : 0)], r = l.x, a = l.y, o = l.t) : -1 < ["mousedown", "mousemove", "mouseup"].indexOf(d) ? (i.push([d, [l.x - t, l.y - n], C(o ? l.t - o : 0)]),
            t = l.x,
            n = l.y,
            o = l.t) : -1 < ["blur", "focus", "unload"].indexOf(d) && (i.push([d, C(o ? l.x - o : 0)]),
            o = l.x)
    }
    return i
}

//var t中的E变量
var E = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-:@~*,.()[]/|"
//获取t参数
var get_t = function (e) {
    function g(e, t) {
        for (var n = e.toString(2), r = "", a = n.length + 1; a <= t; a += 1)
            r += "0";
        return r + n
    }

    function d(e, t) {
        for (var n = [], r = 0, a = e.length; r < a; r += 1)
            n.push(t(e[r]));
        return n
    }

    function u(e, t) {
        var n = function (e) {
            for (var t = (e = d(e, function (e) {
                return e = Math.min(32767, e),
                    e = Math.max(-32767, e)
            })).length, n = 0, r = []; n < t;) {
                for (var a = 1, o = e[n], i = Math.abs(o); !(t <= n + a) && e[n + a] === o && !(127 <= i || 127 <= a);)
                    a += 1;
                1 < a ? r.push((o < 0 ? 49152 : 32768) | a << 7 | i) : r.push(o),
                    n += a
            }
            return r
        }(e)
            , a = []
            , o = [];
        d(n, function (e) {
            var t, n, r = Math.ceil((t = Math.abs(e) + 1,
                n = 16,
                0 === t ? 0 : Math.log(t) / Math.log(n)));
            0 === r && (r = 1),
                a.push(g(r - 1, 2)),
                o.push(g(Math.abs(e), 4 * r))
        });
        var r, i, s = a.join(""), c = o.join(""), l = t ? d((r = function (e) {
            return 0 !== e && e >> 15 != 1
        }
            ,
            i = [],
            d(n, function (e) {
                r(e) && i.push(e)
            }),
            i), function (e) {
            return e < 0 ? "1" : "0"
        }).join("") : "";
        return g(32768 | n.length, 16) + s + c + l
    }

    var h = {
        mousemove: 0,
        mousedown: 1,
        mouseup: 2,
        scroll: 3,
        focus: 4,
        blur: 5,
        unload: 6,
        unknown: 7
    };
    return function (e) {
        for (var t = [], n = [], r = [], a = [], o = 0, i = e.length; o < i; o += 1) {
            var s = e[o]
                , c = s.length;
            t.push(s[0]),
                n.push(2 === c ? s[1] : s[2]),
            3 === c && (r.push(Math.round(s[1][0])),
                a.push(Math.round(s[1][1])))
        }
        var l = function (e) {
            for (var t = [], n = e.length, r = 0; r < n;) {
                for (var a = e[r], o = 0; !(16 <= o);) {
                    var i = r + o + 1;
                    if (n <= i)
                        break;
                    if (e[i] !== a)
                        break;
                    o += 1
                }
                r = r + 1 + o;
                var s = h[a];
                0 !== o ? (t.push(8 | s),
                    t.push(o - 1)) : t.push(s)
            }
            for (var c = g(32768 | n, 16), l = "", d = 0, u = t.length; d < u; d += 1)
                l += g(t[d], 4);
            return c + l
        }(t) + u(n, !1) + u(r, !0) + u(a, !0)
            , d = l.length;
        return d % 6 != 0 && (l += g(0, 6 - d % 6)),
            function (e) {
                for (var t = "", n = e.length / 6, r = 0; r < n; r += 1)
                t += E.charAt(parseInt(e.slice(6 * r, 6 * (r + 1)), 2));
                return t
            }(l)
    }(e)
}
//将函数统一一下，便于交给python执行
function main(l){
    return get_t(e1(l))
}
//console.log(main(l));

