def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

if __name__ == "__main__":
    print("imported from:", __name__)
else:
    print('Nothing')