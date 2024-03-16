class TestUsers:

    user_without_login = {
        "login": None,
        "password": "1234567"
    }
    user_without_password = {
        "login": "testttttttt",
        "password": ""
    }
    user_with_existing_login = {
        "login": "eqrtttttter",
        "password": "dfghjklklk"
    }
    positive_login = {
        "login": "yeymmcbbkx",
        "password": "ojugthnwnm"
    }
    wrong_login = {
        "login": "0000000",
        "password": "ojugthnwnm"
    }
    wrong_password = {
        "login": "yeymmcbbkx",
        "password": "000000000"
    }
