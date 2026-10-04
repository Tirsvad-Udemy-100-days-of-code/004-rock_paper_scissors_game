import pytest

from rock_paper_scissors import game


@pytest.mark.parametrize(
    ("user", "computer", "expected"),
    [
        (0, 0, game.DRAW),
        (1, 1, game.DRAW),
        (2, 2, game.DRAW),
        (0, 2, game.WIN),   # rock beats scissors
        (1, 0, game.WIN),   # paper beats rock
        (2, 1, game.WIN),   # scissors beats paper
        (2, 0, game.LOSE),
        (0, 1, game.LOSE),
        (1, 2, game.LOSE),
    ],
)
def test_determine_result(user, computer, expected):
    assert game.determine_result(user, computer) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [("0", 0), (" 1 ", 1), ("2", 2), ("3", None), ("-1", None), ("rock", None), ("", None)],
)
def test_parse_choice(text, expected):
    assert game.parse_choice(text) == expected


def test_main_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "9")
    game.main()
    assert "invalid" in capsys.readouterr().out


def test_main_win(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    monkeypatch.setattr(game.random, "randint", lambda a, b: 2)
    game.main()
    assert "You win!" in capsys.readouterr().out


def test_colorize_title_disabled_returns_plain():
    assert game.colorize_title(enabled=False) == game.TITLE


def test_colorize_title_enabled_colors_each_word():
    out = game.colorize_title(enabled=True)
    for color in game.TITLE_COLORS:
        assert color in out
    assert out.count(game.RESET) == len(game.TITLE.strip().splitlines())
