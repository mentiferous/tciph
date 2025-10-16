from pathlib import Path

from tciph.utils.characters import characters
from tciph.utils.console import console


def gen_key():
    key_file = "key.py"

    with open(key_file, "w") as file:
        file.write(characters.strip("\n"))

    console.print(f"[b][*][/b] Key generated: [b]{key_file}[/b]")


def get_key():
    key_file = Path("key.py")

    if not key_file.is_file():
        gen_key()


def cipher():
    get_key()

    from key import (
        a,
        apostrophe,
        b,
        c,
        capital_a,
        capital_b,
        capital_c,
        capital_d,
        capital_e,
        capital_f,
        capital_g,
        capital_h,
        capital_i,
        capital_j,
        capital_k,
        capital_l,
        capital_m,
        capital_n,
        capital_o,
        capital_p,
        capital_q,
        capital_r,
        capital_s,
        capital_t,
        capital_u,
        capital_v,
        capital_w,
        capital_x,
        capital_y,
        capital_z,
        comma,
        d,
        digit_0,
        digit_1,
        digit_2,
        digit_3,
        digit_4,
        digit_5,
        digit_6,
        digit_7,
        digit_8,
        digit_9,
        e,
        exclamation_mark,
        f,
        g,
        h,
        hyphen,
        i,
        j,
        k,
        l,
        m,
        n,
        o,
        p,
        period,
        q,
        question_mark,
        r,
        s,
        salt_0,
        salt_1,
        space,
        t,
        u,
        v,
        w,
        x,
        y,
        z,
    )

    text = console.input("[i]Text to cipher[/i]: ")

    text = text.replace("a", f"{salt_0}{a}{salt_0}")
    text = text.replace("b", f"{salt_1}{b}{salt_1}")
    text = text.replace("c", c)
    text = text.replace("d", d)
    text = text.replace("e", e)
    text = text.replace("f", f)
    text = text.replace("g", g)
    text = text.replace("h", h)
    text = text.replace("i", i)
    text = text.replace("j", j)
    text = text.replace("k", k)
    text = text.replace("l", l)
    text = text.replace("m", m)
    text = text.replace("n", n)
    text = text.replace("o", o)
    text = text.replace("p", p)
    text = text.replace("q", q)
    text = text.replace("r", r)
    text = text.replace("s", s)
    text = text.replace("t", t)
    text = text.replace("u", u)
    text = text.replace("v", v)
    text = text.replace("w", w)
    text = text.replace("x", x)
    text = text.replace("y", y)
    text = text.replace("z", z)

    text = text.replace("A", capital_a)
    text = text.replace("B", capital_b)
    text = text.replace("C", capital_c)
    text = text.replace("D", capital_d)
    text = text.replace("E", capital_e)
    text = text.replace("F", capital_f)
    text = text.replace("G", capital_g)
    text = text.replace("H", capital_h)
    text = text.replace("I", capital_i)
    text = text.replace("J", capital_j)
    text = text.replace("K", capital_k)
    text = text.replace("L", capital_l)
    text = text.replace("M", capital_m)
    text = text.replace("N", capital_n)
    text = text.replace("O", capital_o)
    text = text.replace("P", capital_p)
    text = text.replace("Q", capital_q)
    text = text.replace("R", capital_r)
    text = text.replace("S", capital_s)
    text = text.replace("T", capital_t)
    text = text.replace("U", capital_u)
    text = text.replace("V", capital_v)
    text = text.replace("W", capital_w)
    text = text.replace("X", capital_x)
    text = text.replace("Y", capital_y)
    text = text.replace("Z", capital_z)

    text = text.replace("0", digit_0)
    text = text.replace("1", digit_1)
    text = text.replace("2", digit_2)
    text = text.replace("3", digit_3)
    text = text.replace("4", digit_4)
    text = text.replace("5", digit_5)
    text = text.replace("6", digit_6)
    text = text.replace("7", digit_7)
    text = text.replace("8", digit_8)
    text = text.replace("9", digit_9)

    text = text.replace(" ", space)
    text = text.replace(".", period)
    text = text.replace(",", comma)
    text = text.replace("'", apostrophe)
    text = text.replace("?", question_mark)
    text = text.replace("!", exclamation_mark)
    text = text.replace("-", hyphen)

    console.print(f"[i]Ciphered text[/i]: {text}")


def decipher():
    get_key()

    from key import (
        a,
        apostrophe,
        b,
        c,
        capital_a,
        capital_b,
        capital_c,
        capital_d,
        capital_e,
        capital_f,
        capital_g,
        capital_h,
        capital_i,
        capital_j,
        capital_k,
        capital_l,
        capital_m,
        capital_n,
        capital_o,
        capital_p,
        capital_q,
        capital_r,
        capital_s,
        capital_t,
        capital_u,
        capital_v,
        capital_w,
        capital_x,
        capital_y,
        capital_z,
        comma,
        d,
        digit_0,
        digit_1,
        digit_2,
        digit_3,
        digit_4,
        digit_5,
        digit_6,
        digit_7,
        digit_8,
        digit_9,
        e,
        exclamation_mark,
        f,
        g,
        h,
        hyphen,
        i,
        j,
        k,
        l,
        m,
        n,
        o,
        p,
        period,
        q,
        question_mark,
        r,
        s,
        salt_0,
        salt_1,
        space,
        t,
        u,
        v,
        w,
        x,
        y,
        z,
    )

    text = console.input("[i]Text to decipher[/i]: ")

    text = text.replace(salt_0, "")
    text = text.replace(salt_1, "")

    text = text.replace(a, "a")
    text = text.replace(b, "b")
    text = text.replace(c, "c")
    text = text.replace(d, "d")
    text = text.replace(e, "e")
    text = text.replace(f, "f")
    text = text.replace(g, "g")
    text = text.replace(h, "h")
    text = text.replace(i, "i")
    text = text.replace(j, "j")
    text = text.replace(k, "k")
    text = text.replace(l, "l")
    text = text.replace(m, "m")
    text = text.replace(n, "n")
    text = text.replace(o, "o")
    text = text.replace(p, "p")
    text = text.replace(q, "q")
    text = text.replace(r, "r")
    text = text.replace(s, "s")
    text = text.replace(t, "t")
    text = text.replace(u, "u")
    text = text.replace(v, "v")
    text = text.replace(w, "w")
    text = text.replace(x, "x")
    text = text.replace(y, "y")
    text = text.replace(z, "z")

    text = text.replace(capital_a, "A")
    text = text.replace(capital_b, "B")
    text = text.replace(capital_c, "C")
    text = text.replace(capital_d, "D")
    text = text.replace(capital_e, "E")
    text = text.replace(capital_f, "F")
    text = text.replace(capital_g, "G")
    text = text.replace(capital_h, "H")
    text = text.replace(capital_i, "I")
    text = text.replace(capital_j, "J")
    text = text.replace(capital_k, "K")
    text = text.replace(capital_l, "L")
    text = text.replace(capital_m, "M")
    text = text.replace(capital_n, "N")
    text = text.replace(capital_o, "O")
    text = text.replace(capital_p, "P")
    text = text.replace(capital_q, "Q")
    text = text.replace(capital_r, "R")
    text = text.replace(capital_s, "S")
    text = text.replace(capital_t, "T")
    text = text.replace(capital_u, "U")
    text = text.replace(capital_v, "V")
    text = text.replace(capital_w, "W")
    text = text.replace(capital_x, "X")
    text = text.replace(capital_y, "Y")
    text = text.replace(capital_z, "Z")

    text = text.replace(digit_0, "0")
    text = text.replace(digit_1, "1")
    text = text.replace(digit_2, "2")
    text = text.replace(digit_3, "3")
    text = text.replace(digit_4, "4")
    text = text.replace(digit_5, "5")
    text = text.replace(digit_6, "6")
    text = text.replace(digit_7, "7")
    text = text.replace(digit_8, "8")
    text = text.replace(digit_9, "9")

    text = text.replace(space, " ")
    text = text.replace(period, ".")
    text = text.replace(comma, ",")
    text = text.replace(apostrophe, "'")
    text = text.replace(question_mark, "?")
    text = text.replace(exclamation_mark, "!")
    text = text.replace(hyphen, "-")

    console.print(f"[i]Deciphered text[/i]: {text}")
