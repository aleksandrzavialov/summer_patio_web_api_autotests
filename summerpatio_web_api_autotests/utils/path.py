def relative_from_root(path: str):
    import summerpatio_web_api_autotests
    from pathlib import Path

    return (
        Path(summerpatio_web_api_autotests.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )

