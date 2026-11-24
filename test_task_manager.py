
import json
import storage


def test_load_empty_tasks(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "tasks.json")
    assert storage.load_tasks() == []


def test_save_and_load_tasks(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "tasks.json")

    tasks = [
        {
            "id": 1,
            "title": "Learn Python",
            "due": "2026-12-13",
            "status": "pending"
        }
    ]

    storage.save_tasks(tasks)
    assert storage.load_tasks() == tasks


def test_saved_file_contains_json(tmp_path, monkeypatch):
    file_path = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "DATA_FILE", file_path)

    storage.save_tasks([{"id": 1, "title": "Test"}])

    with open(file_path, "r") as file:
        data = json.load(file)

    assert data[0]["title"] == "Test"
