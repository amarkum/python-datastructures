"""unittest.mock — patching, MagicMock, and side effects."""

from unittest.mock import MagicMock, patch, call


def fetch_user(user_id, db):
    return db.get(user_id)


def send_email(recipient, message, mailer):
    return mailer.send(to=recipient, body=message)


if __name__ == "__main__":
    print("=== MagicMock ===")
    mock_db = MagicMock()
    mock_db.get.return_value = {"id": 1, "name": "Alice"}
    result = fetch_user(1, mock_db)
    print(result)
    mock_db.get.assert_called_once_with(1)

    print("\n=== patch context manager ===")
    mock_mailer = MagicMock()
    mock_mailer.send.return_value = True
    with patch("builtins.print") as mock_print:
        print("this is mocked")
        mock_print.assert_called_once_with("this is mocked")

    print("\n=== side_effect ===")
    mock = MagicMock()
    mock.side_effect = [1, 2, 3]
    print(mock(), mock(), mock())

    print("\n=== assert call sequence ===")
    logger = MagicMock()
    logger.info("started")
    logger.info("done")
    logger.info.assert_has_calls([call("started"), call("done")])

    print("\n=== send_email with mock ===")
    mailer = MagicMock()
    send_email("bob@example.com", "Hello", mailer)
    mailer.send.assert_called_with(to="bob@example.com", body="Hello")
