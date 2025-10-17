from base64 import b64decode, b64encode
from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

from tciph.key.characters import characters
from tciph.utils.console import console


def gen_key():
    with open("key.py", "w") as f:
        f.write(characters.strip("\n"))

    console.print(f"[b][*][/b] Key generated")


def key_check():
    if not Path("key.py").is_file():
        gen_key()


def load_key():
    from key import (
        A,
        B,
        C,
        D,
        E,
        F,
        G,
        H,
        I,
        J,
        K,
        L,
        M,
        N,
        O,
        P,
        Q,
        R,
        S,
        T,
        U,
        V,
        W,
        X,
        Y,
        Z,
        a,
        apostrophe,
        b,
        c,
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
        salt_7,
        salt_8,
        salt_9,
        salt_10,
        salt_11,
        salt_12,
        salt_13,
        salt_14,
        salt_15,
        salt_16,
        salt_17,
        salt_18,
        salt_19,
        salt_20,
        salt_21,
        salt_22,
        salt_23,
        salt_24,
        salt_25,
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


def compress(char):
    return b64encode(char.encode()).decode()


def decompress(char):
    return b64decode(char.encode()).decode()


def cipher():
    key_check()

    key = load_key()

    text = console.input("[i]Cipher[/i]: ")

    text = compress(text)

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

    text = text.replace("A", key["A"])
    text = text.replace("B", key["B"])
    text = text.replace("C", key["C"])
    text = text.replace("D", key["D"])
    text = text.replace("E", key["E"])
    text = text.replace("F", key["F"])
    text = text.replace("G", key["G"])
    text = text.replace("H", key["H"])
    text = text.replace("I", key["I"])
    text = text.replace("J", key["J"])
    text = text.replace("K", key["K"])
    text = text.replace("L", key["L"])
    text = text.replace("M", key["M"])
    text = text.replace("N", key["N"])
    text = text.replace("O", key["O"])
    text = text.replace("P", key["P"])
    text = text.replace("Q", key["Q"])
    text = text.replace("R", key["R"])
    text = text.replace("S", key["S"])
    text = text.replace("T", key["T"])
    text = text.replace("U", key["U"])
    text = text.replace("V", key["V"])
    text = text.replace("W", key["W"])
    text = text.replace("X", key["X"])
    text = text.replace("Y", key["Y"])
    text = text.replace("Z", key["Z"])

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
    text = text.replace("+", key["plus"])
    text = text.replace("/", key["forward_slash"])

    if key["rotate"] == 1:
        text = text[::-1]

    console.print(f"[i]Ciphered[/i]: {text}")


def decipher():
    key_check()

    key = load_key()

    text = console.input("[i]Decipher[/i]: ")

    if key["rotate"] == 1:
        text = text[::-1]

    for x, _ in enumerate(ascii_lowercase):
        text = text.replace(key[f"salt_{x}"], "")

    for char in ascii_lowercase:
        text = text.replace(key[char], char)

    for char in ascii_uppercase:
        text = text.replace(key[char], char)

    for x in range(10):
        text = text.replace(key[f"digit_{x}"], str(x))

    text = text.replace(key["space"], " ")
    text = text.replace(key["period"], ".")
    text = text.replace(key["comma"], ",")
    text = text.replace(key["apostrophe"], "'")
    text = text.replace(key["question_mark"], "?")
    text = text.replace(key["exclamation_mark"], "!")
    text = text.replace(key["hyphen"], "-")
    text = text.replace(key["equals"], "=")
    text = text.replace(key["underscore"], "_")
    text = text.replace(key["plus"], "+")
    text = text.replace(key["forward_slash"], "/")

    text = decompress(text)

    console.print(f"[i]Deciphered[/i]: {text}")


def cipher_file():
    key_check()

    file = console.input("[i]File[/i]: ")

    file = Path(file)

    with open(file, "r") as f:
        text = f.read()

    key = load_key()

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

    text = text.replace("A", key["A"])
    text = text.replace("B", key["B"])
    text = text.replace("C", key["C"])
    text = text.replace("D", key["D"])
    text = text.replace("E", key["E"])
    text = text.replace("F", key["F"])
    text = text.replace("G", key["G"])
    text = text.replace("H", key["H"])
    text = text.replace("I", key["I"])
    text = text.replace("J", key["J"])
    text = text.replace("K", key["K"])
    text = text.replace("L", key["L"])
    text = text.replace("M", key["M"])
    text = text.replace("N", key["N"])
    text = text.replace("O", key["O"])
    text = text.replace("P", key["P"])
    text = text.replace("Q", key["Q"])
    text = text.replace("R", key["R"])
    text = text.replace("S", key["S"])
    text = text.replace("T", key["T"])
    text = text.replace("U", key["U"])
    text = text.replace("V", key["V"])
    text = text.replace("W", key["W"])
    text = text.replace("X", key["X"])
    text = text.replace("Y", key["Y"])
    text = text.replace("Z", key["Z"])

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
    text = text.replace("+", key["plus"])
    text = text.replace("/", key["forward_slash"])

    if key["rotate"] == 1:
        text = text[::-1]

    with open(file, "w") as f:
        f.write(text)


def decipher_file():
    key_check()

    file = console.input("[i]File[/i]: ")

    file = Path(file)

    with open(file, "r") as f:
        text = f.read()

    key = load_key()

    if key["rotate"] == 1:
        text = text[::-1]

    for x, _ in enumerate(ascii_lowercase):
        text = text.replace(key[f"salt_{x}"], "")

    for char in ascii_lowercase:
        text = text.replace(key[char], char)

    for char in ascii_uppercase:
        text = text.replace(key[char], char)

    for x in range(10):
        text = text.replace(key[f"digit_{x}"], str(x))

    text = text.replace(key["space"], " ")
    text = text.replace(key["period"], ".")
    text = text.replace(key["comma"], ",")
    text = text.replace(key["apostrophe"], "'")
    text = text.replace(key["question_mark"], "?")
    text = text.replace(key["exclamation_mark"], "!")
    text = text.replace(key["hyphen"], "-")
    text = text.replace(key["equals"], "=")
    text = text.replace(key["underscore"], "_")
    text = text.replace(key["plus"], "+")
    text = text.replace(key["forward_slash"], "/")

    with open(file, "w") as f:
        f.write(text)
