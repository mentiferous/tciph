from pathlib import Path

from tciph.key.characters import characters
from tciph.utils.console import console


def gen_key():
    with open("key.py", "w") as file:
        file.write(characters.strip("\n"))

    console.print(f"[b][*][/b] Key generated")


def key_check():
    if not Path("key.py").is_file():
        gen_key()


def load_key():
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
        equals,
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
        rotate,
        s,
        salt_0,
        salt_1,
        salt_2,
        salt_3,
        salt_4,
        salt_5,
        salt_6,
        space,
        t,
        u,
        underscore,
        v,
        w,
        x,
        y,
        z,
    )

    return locals()


def cipher():
    key_check()

    key = load_key()

    text = console.input("[i]Cipher[/i]: ")

    text = text.replace("a", f"{key['salt_0']}{key['a']}{key['salt_0']}")
    text = text.replace("b", f"{key['salt_1']}{key['b']}{key['salt_1']}")
    text = text.replace("c", f"{key['salt_2']}{key['c']}{key['salt_2']}")
    text = text.replace("d", f"{key['salt_3']}{key['d']}{key['salt_3']}")
    text = text.replace("e", f"{key['salt_4']}{key['e']}{key['salt_4']}")
    text = text.replace("f", f"{key['salt_5']}{key['f']}{key['salt_5']}")
    text = text.replace("g", f"{key['salt_6']}{key['g']}{key['salt_6']}")
    text = text.replace("h", f"{key['salt_7']}{key['h']}{key['salt_7']}")
    text = text.replace("i", f"{key['salt_8']}{key['i']}{key['salt_8']}")
    text = text.replace("j", f"{key['salt_9']}{key['j']}{key['salt_9']}")
    text = text.replace("k", f"{key['salt_10']}{key['k']}{key['salt_10']}")
    text = text.replace("l", f"{key['salt_11']}{key['l']}{key['salt_11']}")
    text = text.replace("m", f"{key['salt_12']}{key['m']}{key['salt_12']}")
    text = text.replace("n", f"{key['salt_13']}{key['n']}{key['salt_13']}")
    text = text.replace("o", f"{key['salt_14']}{key['o']}{key['salt_14']}")
    text = text.replace("p", f"{key['salt_15']}{key['p']}{key['salt_15']}")
    text = text.replace("q", f"{key['salt_16']}{key['q']}{key['salt_16']}")
    text = text.replace("r", f"{key['salt_17']}{key['r']}{key['salt_17']}")
    text = text.replace("s", f"{key['salt_18']}{key['s']}{key['salt_18']}")
    text = text.replace("t", f"{key['salt_19']}{key['t']}{key['salt_19']}")
    text = text.replace("u", f"{key['salt_20']}{key['u']}{key['salt_20']}")
    text = text.replace("v", f"{key['salt_21']}{key['v']}{key['salt_21']}")
    text = text.replace("w", f"{key['salt_22']}{key['w']}{key['salt_22']}")
    text = text.replace("x", f"{key['salt_23']}{key['x']}{key['salt_23']}")
    text = text.replace("y", f"{key['salt_24']}{key['y']}{key['salt_24']}")
    text = text.replace("z", f"{key['salt_25']}{key['z']}{key['salt_25']}")

    text = text.replace("A", key["capital_a"])
    text = text.replace("B", key["capital_b"])
    text = text.replace("C", key["capital_c"])
    text = text.replace("D", key["capital_d"])
    text = text.replace("E", key["capital_e"])
    text = text.replace("F", key["capital_f"])
    text = text.replace("G", key["capital_g"])
    text = text.replace("H", key["capital_h"])
    text = text.replace("I", key["capital_i"])
    text = text.replace("J", key["capital_j"])
    text = text.replace("K", key["capital_k"])
    text = text.replace("L", key["capital_l"])
    text = text.replace("M", key["capital_m"])
    text = text.replace("N", key["capital_n"])
    text = text.replace("O", key["capital_o"])
    text = text.replace("P", key["capital_p"])
    text = text.replace("Q", key["capital_q"])
    text = text.replace("R", key["capital_r"])
    text = text.replace("S", key["capital_s"])
    text = text.replace("T", key["capital_t"])
    text = text.replace("U", key["capital_u"])
    text = text.replace("V", key["capital_v"])
    text = text.replace("W", key["capital_w"])
    text = text.replace("X", key["capital_x"])
    text = text.replace("Y", key["capital_y"])
    text = text.replace("Z", key["capital_z"])

    text = text.replace("0", key["digit_0"])
    text = text.replace("1", key["digit_1"])
    text = text.replace("2", key["digit_2"])
    text = text.replace("3", key["digit_3"])
    text = text.replace("4", key["digit_4"])
    text = text.replace("5", key["digit_5"])
    text = text.replace("6", key["digit_6"])
    text = text.replace("7", key["digit_7"])
    text = text.replace("8", key["digit_8"])
    text = text.replace("9", key["digit_9"])

    text = text.replace(" ", key["space"])
    text = text.replace(".", key["period"])
    text = text.replace(",", key["comma"])
    text = text.replace("'", key["apostrophe"])
    text = text.replace("?", key["question_mark"])
    text = text.replace("!", key["exclamation_mark"])
    text = text.replace("-", key["hyphen"])
    text = text.replace("=", key["equals"])
    text = text.replace("_", key["underscore"])

    if key["rotate"] == 1:
        text = text[::-1]

    console.print(f"[i]Ciphered[/i]: {text}")


def decipher():
    key_check()

    key = load_key()

    text = console.input("[i]Decipher[/i]: ")

    if key["rotate"] == 1:
        text = text[::-1]

    text = text.replace(key["salt_0"], "")
    text = text.replace(key["salt_1"], "")
    text = text.replace(key["salt_2"], "")
    text = text.replace(key["salt_3"], "")
    text = text.replace(key["salt_4"], "")
    text = text.replace(key["salt_5"], "")
    text = text.replace(key["salt_6"], "")
    text = text.replace(key["salt_7"], "")
    text = text.replace(key["salt_8"], "")
    text = text.replace(key["salt_9"], "")
    text = text.replace(key["salt_10"], "")
    text = text.replace(key["salt_11"], "")
    text = text.replace(key["salt_12"], "")
    text = text.replace(key["salt_13"], "")
    text = text.replace(key["salt_14"], "")
    text = text.replace(key["salt_15"], "")
    text = text.replace(key["salt_16"], "")
    text = text.replace(key["salt_17"], "")
    text = text.replace(key["salt_18"], "")
    text = text.replace(key["salt_19"], "")
    text = text.replace(key["salt_20"], "")
    text = text.replace(key["salt_21"], "")
    text = text.replace(key["salt_22"], "")
    text = text.replace(key["salt_23"], "")
    text = text.replace(key["salt_24"], "")
    text = text.replace(key["salt_25"], "")

    text = text.replace(key["a"], "a")
    text = text.replace(key["b"], "b")
    text = text.replace(key["c"], "c")
    text = text.replace(key["d"], "d")
    text = text.replace(key["e"], "e")
    text = text.replace(key["f"], "f")
    text = text.replace(key["g"], "g")
    text = text.replace(key["h"], "h")
    text = text.replace(key["i"], "i")
    text = text.replace(key["j"], "j")
    text = text.replace(key["k"], "k")
    text = text.replace(key["l"], "l")
    text = text.replace(key["m"], "m")
    text = text.replace(key["n"], "n")
    text = text.replace(key["o"], "o")
    text = text.replace(key["p"], "p")
    text = text.replace(key["q"], "q")
    text = text.replace(key["r"], "r")
    text = text.replace(key["s"], "s")
    text = text.replace(key["t"], "t")
    text = text.replace(key["u"], "u")
    text = text.replace(key["v"], "v")
    text = text.replace(key["w"], "w")
    text = text.replace(key["x"], "x")
    text = text.replace(key["y"], "y")
    text = text.replace(key["z"], "z")

    text = text.replace(key["capital_a"], "A")
    text = text.replace(key["capital_b"], "B")
    text = text.replace(key["capital_c"], "C")
    text = text.replace(key["capital_d"], "D")
    text = text.replace(key["capital_e"], "E")
    text = text.replace(key["capital_f"], "F")
    text = text.replace(key["capital_g"], "G")
    text = text.replace(key["capital_h"], "H")
    text = text.replace(key["capital_i"], "I")
    text = text.replace(key["capital_j"], "J")
    text = text.replace(key["capital_k"], "K")
    text = text.replace(key["capital_l"], "L")
    text = text.replace(key["capital_m"], "M")
    text = text.replace(key["capital_n"], "N")
    text = text.replace(key["capital_o"], "O")
    text = text.replace(key["capital_p"], "P")
    text = text.replace(key["capital_q"], "Q")
    text = text.replace(key["capital_r"], "R")
    text = text.replace(key["capital_s"], "S")
    text = text.replace(key["capital_t"], "T")
    text = text.replace(key["capital_u"], "U")
    text = text.replace(key["capital_v"], "V")
    text = text.replace(key["capital_w"], "W")
    text = text.replace(key["capital_x"], "X")
    text = text.replace(key["capital_y"], "Y")
    text = text.replace(key["capital_z"], "Z")

    text = text.replace(key["digit_0"], "0")
    text = text.replace(key["digit_1"], "1")
    text = text.replace(key["digit_2"], "2")
    text = text.replace(key["digit_3"], "3")
    text = text.replace(key["digit_4"], "4")
    text = text.replace(key["digit_5"], "5")
    text = text.replace(key["digit_6"], "6")
    text = text.replace(key["digit_7"], "7")
    text = text.replace(key["digit_8"], "8")
    text = text.replace(key["digit_9"], "9")

    text = text.replace(key["space"], " ")
    text = text.replace(key["period"], ".")
    text = text.replace(key["comma"], ",")
    text = text.replace(key["apostrophe"], "'")
    text = text.replace(key["question_mark"], "?")
    text = text.replace(key["exclamation_mark"], "!")
    text = text.replace(key["hyphen"], "-")
    text = text.replace(key["equals"], "=")
    text = text.replace(key["underscore"], "_")

    console.print(f"[i]Deciphered[/i]: {text}")
