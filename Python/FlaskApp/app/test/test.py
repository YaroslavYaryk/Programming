from manage import client


def test_get():
    res = client.get("/api/posts/")

    assert res.status_code == 200


def test_get_about():
    res = client.get("/about")

    assert res.status_code == 200