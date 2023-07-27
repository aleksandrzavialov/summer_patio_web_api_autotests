def relative_from_root(path: str):
    import summerpatio_web_autotests
    from pathlib import Path

    return (
        Path(summerpatio_web_autotests.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
