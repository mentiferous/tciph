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

    key_value = load_key()

    text = console.input("[i]Cipher[/i]: ")

    text = text.replace(
        "a", f"{key_value['salt_0']}{key_value['a']}{key_value['salt_0']}"
    )
    text = text.replace(
        "b", f"{key_value['salt_1']}{key_value['b']}{key_value['salt_1']}"
    )
    text = text.replace(
        "c", f"{key_value['salt_2']}{key_value['c']}{key_value['salt_2']}"
    )
    text = text.replace("d", key_value["d"])
    text = text.replace("e", key_value["e"])
    text = text.replace("f", key_value["f"])
    text = text.replace("g", key_value["g"])
    text = text.replace("h", key_value["h"])
    text = text.replace("i", key_value["i"])
    text = text.replace("j", key_value["j"])
    text = text.replace("k", key_value["k"])
    text = text.replace("l", key_value["l"])
    text = text.replace("m", key_value["m"])
    text = text.replace("n", key_value["n"])
    text = text.replace("o", key_value["o"])
    text = text.replace("p", key_value["p"])
    text = text.replace("q", key_value["q"])
    text = text.replace("r", key_value["r"])
    text = text.replace("s", key_value["s"])
    text = text.replace("t", key_value["t"])
    text = text.replace("u", key_value["u"])
    text = text.replace("v", key_value["v"])
    text = text.replace("w", key_value["w"])
    text = text.replace("x", key_value["x"])
    text = text.replace("y", key_value["y"])
    text = text.replace("z", key_value["z"])

    text = text.replace("A", key_value["capital_a"])
    text = text.replace("B", key_value["capital_b"])
    text = text.replace("C", key_value["capital_c"])
    text = text.replace("D", key_value["capital_d"])
    text = text.replace("E", key_value["capital_e"])
    text = text.replace("F", key_value["capital_f"])
    text = text.replace("G", key_value["capital_g"])
    text = text.replace("H", key_value["capital_h"])
    text = text.replace("I", key_value["capital_i"])
    text = text.replace("J", key_value["capital_j"])
    text = text.replace("K", key_value["capital_k"])
    text = text.replace("L", key_value["capital_l"])
    text = text.replace("M", key_value["capital_m"])
    text = text.replace("N", key_value["capital_n"])
    text = text.replace("O", key_value["capital_o"])
    text = text.replace("P", key_value["capital_p"])
    text = text.replace("Q", key_value["capital_q"])
    text = text.replace("R", key_value["capital_r"])
    text = text.replace("S", key_value["capital_s"])
    text = text.replace("T", key_value["capital_t"])
    text = text.replace("U", key_value["capital_u"])
    text = text.replace("V", key_value["capital_v"])
    text = text.replace("W", key_value["capital_w"])
    text = text.replace("X", key_value["capital_x"])
    text = text.replace("Y", key_value["capital_y"])
    text = text.replace("Z", key_value["capital_z"])

    text = text.replace("0", key_value["digit_0"])
    text = text.replace("1", key_value["digit_1"])
    text = text.replace("2", key_value["digit_2"])
    text = text.replace("3", key_value["digit_3"])
    text = text.replace("4", key_value["digit_4"])
    text = text.replace("5", key_value["digit_5"])
    text = text.replace("6", key_value["digit_6"])
    text = text.replace("7", key_value["digit_7"])
    text = text.replace("8", key_value["digit_8"])
    text = text.replace("9", key_value["digit_9"])

    text = text.replace(" ", key_value["space"])
    text = text.replace(".", key_value["period"])
    text = text.replace(",", key_value["comma"])
    text = text.replace("'", key_value["apostrophe"])
    text = text.replace("?", key_value["question_mark"])
    text = text.replace("!", key_value["exclamation_mark"])
    text = text.replace("-", key_value["hyphen"])
    text = text.replace("=", key_value["equals"])
    text = text.replace("_", key_value["underscore"])

    if key_value["rotate"] == 1:
        text = text[::-1]

    console.print(f"[i]Ciphered[/i]: {text}")


def decipher():
    key_check()

    key_value = load_key()

    text = console.input("[i]Decipher[/i]: ")

    if key_value["rotate"] == 1:
        text = text[::-1]

    text = text.replace(key_value["salt_0"], "")
    text = text.replace(key_value["salt_1"], "")
    text = text.replace(key_value["salt_2"], "")

    text = text.replace(key_value["a"], "a")
    text = text.replace(key_value["b"], "b")
    text = text.replace(key_value["c"], "c")
    text = text.replace(key_value["d"], "d")
    text = text.replace(key_value["e"], "e")
    text = text.replace(key_value["f"], "f")
    text = text.replace(key_value["g"], "g")
    text = text.replace(key_value["h"], "h")
    text = text.replace(key_value["i"], "i")
    text = text.replace(key_value["j"], "j")
    text = text.replace(key_value["k"], "k")
    text = text.replace(key_value["l"], "l")
    text = text.replace(key_value["m"], "m")
    text = text.replace(key_value["n"], "n")
    text = text.replace(key_value["o"], "o")
    text = text.replace(key_value["p"], "p")
    text = text.replace(key_value["q"], "q")
    text = text.replace(key_value["r"], "r")
    text = text.replace(key_value["s"], "s")
    text = text.replace(key_value["t"], "t")
    text = text.replace(key_value["u"], "u")
    text = text.replace(key_value["v"], "v")
    text = text.replace(key_value["w"], "w")
    text = text.replace(key_value["x"], "x")
    text = text.replace(key_value["y"], "y")
    text = text.replace(key_value["z"], "z")

    text = text.replace(key_value["capital_a"], "A")
    text = text.replace(key_value["capital_b"], "B")
    text = text.replace(key_value["capital_c"], "C")
    text = text.replace(key_value["capital_d"], "D")
    text = text.replace(key_value["capital_e"], "E")
    text = text.replace(key_value["capital_f"], "F")
    text = text.replace(key_value["capital_g"], "G")
    text = text.replace(key_value["capital_h"], "H")
    text = text.replace(key_value["capital_i"], "I")
    text = text.replace(key_value["capital_j"], "J")
    text = text.replace(key_value["capital_k"], "K")
    text = text.replace(key_value["capital_l"], "L")
    text = text.replace(key_value["capital_m"], "M")
    text = text.replace(key_value["capital_n"], "N")
    text = text.replace(key_value["capital_o"], "O")
    text = text.replace(key_value["capital_p"], "P")
    text = text.replace(key_value["capital_q"], "Q")
    text = text.replace(key_value["capital_r"], "R")
    text = text.replace(key_value["capital_s"], "S")
    text = text.replace(key_value["capital_t"], "T")
    text = text.replace(key_value["capital_u"], "U")
    text = text.replace(key_value["capital_v"], "V")
    text = text.replace(key_value["capital_w"], "W")
    text = text.replace(key_value["capital_x"], "X")
    text = text.replace(key_value["capital_y"], "Y")
    text = text.replace(key_value["capital_z"], "Z")

    text = text.replace(key_value["digit_0"], "0")
    text = text.replace(key_value["digit_1"], "1")
    text = text.replace(key_value["digit_2"], "2")
    text = text.replace(key_value["digit_3"], "3")
    text = text.replace(key_value["digit_4"], "4")
    text = text.replace(key_value["digit_5"], "5")
    text = text.replace(key_value["digit_6"], "6")
    text = text.replace(key_value["digit_7"], "7")
    text = text.replace(key_value["digit_8"], "8")
    text = text.replace(key_value["digit_9"], "9")

    text = text.replace(key_value["space"], " ")
    text = text.replace(key_value["period"], ".")
    text = text.replace(key_value["comma"], ",")
    text = text.replace(key_value["apostrophe"], "'")
    text = text.replace(key_value["question_mark"], "?")
    text = text.replace(key_value["exclamation_mark"], "!")
    text = text.replace(key_value["hyphen"], "-")
    text = text.replace(key_value["equals"], "=")
    text = text.replace(key_value["underscore"], "_")

    console.print(f"[i]Deciphered[/i]: {text}")
