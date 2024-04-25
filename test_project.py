from project import create, update, delete

def test_create(monkeypatch):
    user_input = "Example Show"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    watchlist, count = [], 0
    watchlist, count = create(watchlist, count)
    assert len(watchlist) == 1
    assert watchlist[0]["ID"] == 1

def test_update(monkeypatch):
    show_id_input = "1"
    new_status_input = "Watching"
    monkeypatch.setattr('builtins.input', lambda prompt: show_id_input if "ID" in prompt else new_status_input)
    watchlist = [{"ID": 1, "Show": "Example Show", "Status": "Watchlist"}]
    updated_watchlist = update(watchlist)
    assert updated_watchlist[0]["Status"] == "Watching"


def test_delete(monkeypatch):
    user_input = "1"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    watchlist = [{"ID": 1, "Show": "Example Show", "Status": "Watchlist"}]
    updated_watchlist = delete(watchlist)
    assert len(updated_watchlist) == 0








