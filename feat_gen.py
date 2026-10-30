def featGen(data: list[str]) -> list[str]:
    feature = lambda fe: [
        (i, f.replace("#DIS", ""), False) if "#DIS" or "DIS" in f else (i, f, True)
        for i, f in enumerate(fe)
    ]
    return "\n".join([f"{i}. {d}" for i, d, en in feature(data) if en])
