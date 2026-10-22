from types import SimpleNamespace

from app.ask import ask


class FakeModels:
    def generate_content(self, model, contents):
        usage = SimpleNamespace(prompt_token_count=8, candidates_token_count=5)
        return SimpleNamespace(text=f"回答: {contents}", usage_metadata=usage)


class FakeClient:
    models = FakeModels()


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    monkeypatch.setattr("app.ask.get_api_key", lambda: "test-key")
    monkeypatch.setattr("app.ask.genai.Client", lambda **_kwargs: FakeClient())

    assert ask("質問") == "回答: 質問"

    assert "[usage] input_tokens=8, output_tokens=5" in capsys.readouterr().out